# Changing Access Controls on User Data

**Framework**: CloudKit

Restrict access to or remove restrictions from a user’s data at their request.

#### Overview

Users can ask you to prevent any further changes to their data that your app stores in CloudKit. Use the `restrict` API that CloudKit Web Services provides to honor those requests. You can remove restrictions at the user’s request by calling the `unrestrict` API.

##### Identify Containers

To be sure that you restrict changes and access to all of a user’s data that your app stores, cross-reference the list of containers your app has access to in Xcode and assemble a list of those containers’ identifiers. [`Identifying an App’s Containers`](identifying-an-app-s-containers.md) describes this process.

The example below stores containers in constants to use later:

```swift
let defaultContainer = CKContainer.default()
let documents = CKContainer(identifier: "iCloud.com.example.myexampleapp.documents")
let settings = CKContainer(identifier: "iCloud.com.example.myexampleapp.settings")
```

##### Create Reusable Api Tokens

The `restrict` API call requires a token each time you call the API. You create an API token once for each container in your app using the CloudKit Dashboard, and reuse it in each API call to a specific container.

Generate a token in the CloudKit Dashboard by visiting the page for each container, then selecting API Access > New Token > Create Token. Tokens are specific to a deployment environment, so you need separate tokens for the production and development environments.

The example below stores tokens in a dictionary for each container to use later:

```swift
let containerAPITokens: [CKContainer: String] = [
    defaultContainer: "<# Token for the default container #>",
    documents: "<# Token for a custom container #>",
    settings: "<# Token for another custom container #>"
]

let containers = Array(containerAPITokens.keys)
```

##### Create Web Authentication Tokens

The `restrict` API call requires a new authentication token each time you call the API, in addition to the reusable API token. The example below shows how to create that token using an instance of [`CKFetchWebAuthTokenOperation`](ckfetchwebauthtokenoperation.md):

```swift
for container in containers {
    guard let apiToken = containerAPITokens[container] else {
        continue
    }
    
    let fetchAuthorization = CKFetchWebAuthTokenOperation(apiToken: apiToken)
    
    fetchAuthorization.fetchWebAuthTokenCompletionBlock = { webToken, error in
        guard let webToken = webToken, error == nil else { return }
        
        restrict(container: container, apiToken: apiToken, webToken: webToken) { error in
            guard error == nil else {
                 print("Restriction failed. Reason: ", error!)
                 return
            }
            print("Restriction succeeded.")
        }
    }
    
    container.privateCloudDatabase.add(fetchAuthorization)
}
```

After you receive the authentication token, you can immediately call the `restrict` API once for each container.

##### Restrict Data Access in Each Container

The example below defines the `restrict(container:apiToken:webToken:completionHandler:)` and `requestRestriction(url:completionHandler:)` methods for the example above to build the network request for the `restrict` API:

```swift
func requestRestriction(url: URL, completionHandler: @escaping (Error?) -> Void) {
    let task = URLSession.shared.dataTask(with: url) { data, response, error in
        if let error = error {
            completionHandler(error)
            return
        }
        guard let httpResponse = response as? HTTPURLResponse,
            (200...299).contains(httpResponse.statusCode) else {
                completionHandler(RestrictError.failure)
                return
        }
        
        print("Restrict result", httpResponse)
        
        // Other than indicating success or failure, the `restrict` API doesn't return actionable data in its response.
        if data != nil {
            completionHandler(nil)
        } else {
            completionHandler(RestrictError.failure)
        }
    }
    task.resume()
}

/// A utility function that percent encodes a token for URL requests.
func encodeToken(_ token: String) -> String {
    return token.addingPercentEncoding(
        withAllowedCharacters: CharacterSet(charactersIn: "+/=").inverted
    ) ?? token
}

/// An error type that represents a failure in the `restrict` API call.
enum RestrictError: Error {
    case failure
}

func restrict(container: CKContainer, apiToken: String, webToken: String, completionHandler: @escaping (Error?) -> Void) {
    let webToken = encodeToken(webToken)
    
    let identifier = container.containerIdentifier!
    let env = "production" // Use "development" during development.
    let baseURL = "https://api.apple-cloudkit.com/database/1/"
    let apiPath = "\(identifier)/\(env)/private/users/restrict"
    let query = "?ckAPIToken=\(apiToken)&ckWebAuthToken=\(webToken)"
    
    let url = URL(string: "\(baseURL)\(apiPath)\(query)")!
    
    requestRestriction(url: url, completionHandler: completionHandler)
}
```

##### Remove Restrictions

When a user requests that you remove restrictions, you use the `unrestrict` API, which performs the opposite operation that the `restrict` API performs.

The example below shows a modified version of the `restrict(container:apiToken:webToken:completionHandler:)` method from the previous example that removes restrictions instead of enabling them:

```swift
func unrestrict(container: CKContainer, apiToken: String, webToken: String, completionHandler: @escaping (Error?) -> Void) {
    let webToken = encodeToken(webToken)
    
    let identifier = container.containerIdentifier!
    let env = "production" // Use "development" during development.
    let baseURL = "https://api.apple-cloudkit.com/database/1/"
    let apiPath = "\(identifier)/\(env)/private/users/unrestrict"
    let query = "?ckAPIToken=\(apiToken)&ckWebAuthToken=\(webToken)"
    
    let url = URL(string: "\(baseURL)\(apiPath)\(query)")!
    
    requestRestriction(url: url, completionHandler: completionHandler)
}
```

A successful call to the `unrestrict(container:apiToken:webToken: completionHandler:)` function (a `nil` error parameter in the completion handler indicates success) means that your app can access and modify user data.

## See Also

- [Encrypting User Data](encrypting-user-data.md)
  Deploy industry-standard security technologies using CloudKit encryption.
- [Providing User Access to CloudKit Data](providing-user-access-to-cloudkit-data.md)
  Provide users access to the data your app stores on their behalf.
- [class CKFetchWebAuthTokenOperation](ckfetchwebauthtokenoperation.md)
  An operation that creates an authentication token for use with CloudKit web services.
- [Responding to Requests to Delete Data](responding-to-requests-to-delete-data.md)
  Provide options for users to delete their CloudKit data from your app.
- [Identifying an App’s Containers](identifying-an-app-s-containers.md)
  Use Xcode’s Project navigator to find the identifiers of active CloudKit containers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/changing-access-controls-on-user-data)*