# retrieveCredentials(forBorderAgent:completion:)

**Framework**: ThreadNetwork  
**Kind**: method

Requests Thread credentials for a Border Agent.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
func credentials(forBorderAgentID borderAgentID: Data) async throws -> THCredentials
```

## Mentions

- [Managing Thread network credentials](managing-thread-network-credentials.md)

#### Discussion

> **Note**: You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration: ```swift
func credentials(forBorderAgentID borderAgentID: Data) async throws -> THCredentials
``` For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

The framework identifies the developer by the team ID. When calling this method, you receive credentials for your team ID only.

Call the method as follows:

```swift
func obtainCredentials(borderAgentID: Data) async -> (cred: THCredentials? ,err: Error? ) {
    let client = THClient()
    var credential: THCredentials?
    var err:Error?
    do {
        credential = try await client.credentials(forBorderAgentID: borderAgentID as Data)
    } catch {
        err = error
    }
    return (credential, err)
}
```

## Parameters

- `borderAgentID`: The identifer of a Thread network Border Agent.
- `completion`: The completion handler the framework calls when the credentials become available.

## See Also

- [func isPreferredNetworkAvailable(completion: (Bool) -> Void)](thclient/ispreferrednetworkavailable(completion:).md)
  Indicates whether a preferred network is available.
- [func checkPreferredNetwork(forActiveOperationalDataset: Data, completion: (Bool) -> Void)](thclient/checkpreferrednetwork(foractiveoperationaldataset:completion:).md)
  Determines if the essential operating parameters match the preferred network’s parameters.
- [func retrieveCredentials(forExtendedPANID: Data, completion: (THCredentials?, (any Error)?) -> Void)](thclient/retrievecredentials(forextendedpanid:completion:).md)
  Requests Thread credentials for an extended Personal Area Network (PAN) ID.
- [func retrieveAllCredentials((Set<THCredentials>?, (any Error)?) -> Void)](thclient/retrieveallcredentials(_:).md)
  Requests all Thread credentials from the framework.
- [func retrievePreferredCredentials((THCredentials?, (any Error)?) -> Void)](thclient/retrievepreferredcredentials(_:).md)
  Requests Thread credentials for the preferred network.
- [func retrieveAllActiveCredentials((Set<THCredentials>?, (any Error)?) -> Void)](thclient/retrieveallactivecredentials(_:).md)
  Returns a set of the active credentials.


---

*[View on Apple Developer](https://developer.apple.com/documentation/threadnetwork/thclient/retrievecredentials(forborderagent:completion:))*