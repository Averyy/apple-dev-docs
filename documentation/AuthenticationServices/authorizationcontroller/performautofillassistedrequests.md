# performAutoFillAssistedRequests(_:)

**Framework**: Authentication Services  
**Kind**: method

Performs an AutoFill-assisted authorization request from the provided array.

**Availability**:
- iOS 16.4+
- iPadOS 16.4+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func performAutoFillAssistedRequests(_ requests: [ASAuthorizationRequest]) async throws -> ASAuthorizationResult
```

#### Return Value

The request’s outcome. For more information, see [`ASAuthorizationResult`](asauthorizationresult.md).

#### Discussion

To perform AutoFill-assisted authorization requests, add the appropriate [`textContentType(_:)`](https://developer.apple.com/documentation/SwiftUI/View/textContentType(_:)-ufdv) to any sign-in related fields, such as those for usernames and passwords:

```swift
TextField("Username", text: $username)
    .textContentType(.username)
```

Then use [`task(priority:_:)`](https://developer.apple.com/documentation/SwiftUI/View/task(priority:_:)) or [`task(id:priority:_:)`](https://developer.apple.com/documentation/SwiftUI/View/task(id:priority:_:)) to perform the requests when the view appears:

```swift
.task {
    // Create the authorization requests.
    async let requests = makeAutoFillAuthorizationRequests()
    // Perform the request and await its result.
    let result = try await authorizationController
        .performAutoFillAssistedRequests(requests)
    switch result {
        // Process the request's result.
    }
}
```

## Parameters

- `requests`: An array of supported authorization requests.

## See Also

- [func performAutoFillAssistedRequest(ASAuthorizationRequest) async throws -> ASAuthorizationResult](authorizationcontroller/performautofillassistedrequest(_:).md)
  Performs an AutoFill-assisted authorization request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/authorizationcontroller/performautofillassistedrequests(_:))*