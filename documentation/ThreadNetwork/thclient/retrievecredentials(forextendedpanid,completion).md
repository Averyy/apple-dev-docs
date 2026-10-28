# retrieveCredentials(forExtendedPANID:completion:)

**Framework**: ThreadNetwork  
**Kind**: method  
**Role**: Instance Method

Requests Thread credentials for an extended Personal Area Network (PAN) ID.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
func retrieveCredentials(forExtendedPANID extendedPANID: Data, completion: @escaping @Sendable (THCredentials?, (any Error)?) -> Void)
```

```swift
func credentials(forExtendedPANID extendedPANID: Data) async throws -> THCredentials
```

```objc
- (void) retrieveCredentialsForExtendedPANID:(NSData *) extendedPANID completion:(void (^)(THCredentials *credentials, NSError *error)) completion;
```

## Discussion

> **Concurrency note**: You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration:
>
> ```swift
> func credentials(forExtendedPANID extendedPANID: Data) async throws -> THCredentials
> ```
>
> For information about concurrency and asynchronous code in Swift, see [Calling Objective-C APIs Asynchronously](../../Swift/calling-objective-c-apis-asynchronously.md).

When calling this method, an alert appears asking for user permission to access credentials.

Call the method as follows:

```swift
func obtainCredentials(xpanID: Data) async -> (cred: THCredentials? ,err: Error? ) {
    let client = THClient()
    var credential: THCredentials?
    var err:Error?
    do {
        credential = try await client.credentials(forExtendedPANID: xpanID as Data)
    } catch {
        err = error
    }
    return (credential, err)
}
```

## Parameters

- `extendedPANID`: The extended PAN identifier.
- `completion`: The completion handler the framework calls when the credentials become available.

## See Also

### Retrieving Credentials
- [func isPreferredNetworkAvailable(completion: (Bool) -> Void)](./ispreferrednetworkavailable%28completion%29.md)
  Indicates whether a preferred network is available.
- [func checkPreferredNetwork(forActiveOperationalDataset: Data, completion: (Bool) -> Void)](./checkpreferrednetwork%28foractiveoperationaldataset,completion%29.md)
  Determines if the essential operating parameters match the preferred network’s parameters.
- [func retrieveCredentials(forBorderAgent: Data, completion: (THCredentials?, (any Error)?) -> Void)](./retrievecredentials%28forborderagent,completion%29.md)
  Requests Thread credentials for a Border Agent.
- [func retrieveAllCredentials((Set<THCredentials>?, (any Error)?) -> Void)](./retrieveallcredentials%28_%29.md)
  Requests all Thread credentials from the framework.
- [func retrievePreferredCredentials((THCredentials?, (any Error)?) -> Void)](./retrievepreferredcredentials%28_%29.md)
  Requests Thread credentials for the preferred network.
- [func retrieveAllActiveCredentials((Set<THCredentials>?, (any Error)?) -> Void)](./retrieveallactivecredentials%28_%29.md)
  Returns a set of the active credentials.


---

*[View on Apple Developer](https://developer.apple.com/documentation/threadnetwork/thclient/retrievecredentials(forextendedpanid:completion:))*