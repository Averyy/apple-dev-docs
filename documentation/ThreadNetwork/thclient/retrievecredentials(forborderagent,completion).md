# retrieveCredentials(forBorderAgent:completion:)

**Framework**: ThreadNetwork  
**Kind**: method  
**Role**: Instance Method

Requests Thread credentials for a Border Agent.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
func retrieveCredentials(forBorderAgent borderAgentID: Data, completion: @escaping @Sendable (THCredentials?, (any Error)?) -> Void)
```

```swift
func credentials(forBorderAgentID borderAgentID: Data) async throws -> THCredentials
```

```objc
- (void) retrieveCredentialsForBorderAgent:(NSData *) borderAgentID completion:(void (^)(THCredentials *credentials, NSError *error)) completion;
```

## Mentions

- [Managing Thread network credentials](../managing-thread-network-credentials.md)

#### Discussion

> **Concurrency note**: You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration:
>
> ```swift
> func credentials(forBorderAgentID borderAgentID: Data) async throws -> THCredentials
> ```
>
> For information about concurrency and asynchronous code in Swift, see [Calling Objective-C APIs Asynchronously](../../Swift/calling-objective-c-apis-asynchronously.md).

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

### Retrieving Credentials
- [func isPreferredNetworkAvailable(completion: (Bool) -> Void)](./ispreferrednetworkavailable%28completion%29.md)
  Indicates whether a preferred network is available.
- [func checkPreferredNetwork(forActiveOperationalDataset: Data, completion: (Bool) -> Void)](./checkpreferrednetwork%28foractiveoperationaldataset,completion%29.md)
  Determines if the essential operating parameters match the preferred network’s parameters.
- [func retrieveCredentials(forExtendedPANID: Data, completion: (THCredentials?, (any Error)?) -> Void)](./retrievecredentials%28forextendedpanid,completion%29.md)
  Requests Thread credentials for an extended Personal Area Network (PAN) ID.
- [func retrieveAllCredentials((Set<THCredentials>?, (any Error)?) -> Void)](./retrieveallcredentials%28_%29.md)
  Requests all Thread credentials from the framework.
- [func retrievePreferredCredentials((THCredentials?, (any Error)?) -> Void)](./retrievepreferredcredentials%28_%29.md)
  Requests Thread credentials for the preferred network.
- [func retrieveAllActiveCredentials((Set<THCredentials>?, (any Error)?) -> Void)](./retrieveallactivecredentials%28_%29.md)
  Returns a set of the active credentials.


---

*[View on Apple Developer](https://developer.apple.com/documentation/threadnetwork/thclient/retrievecredentials(forborderagent:completion:))*