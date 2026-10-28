# isPreferredNetworkAvailable(completion:)

**Framework**: ThreadNetwork  
**Kind**: method  
**Role**: Instance Method

Indicates whether a preferred network is available.

**Availability**:
- iOS 16.4+
- iPadOS 16.4+
- Mac Catalyst 16.4+
- macOS 13.0+
- visionOS 1.0+
- watchOS 9.4+

## Declaration

```swift
func isPreferredNetworkAvailable(completion: @escaping @Sendable (Bool) -> Void)
```

```swift
func isPreferredAvailable() async -> Bool
```

```objc
- (void) isPreferredNetworkAvailableWithCompletion:(void (^)(BOOL isPreferredAvailable)) completion;
```

## Mentions

- [Configuring a Border Router](../configuring-a-border-router.md)
- [Managing Thread network credentials](../managing-thread-network-credentials.md)

## Discussion

> **Concurrency note**: You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration:
>
> ```swift
> func isPreferredAvailable() async -> Bool
> ```
>
> For information about concurrency and asynchronous code in Swift, see [Calling Objective-C APIs Asynchronously](../../Swift/calling-objective-c-apis-asynchronously.md).

Call the method as follows:

```swift
func obtainPreferredAvailable() async -> (NSString?) {
    let client = THClient()
    var bIsPreferredAvailable:Bool?
    bIsPreferredAvailable = await client.isPreferredAvailable()
    let str = ((bIsPreferredAvailable == true) ? "true" : "false")
    return str as NSString;
}
```

## Parameters

- `completion`: The completion handler that returns the result of the preferred network status.

## See Also

### Retrieving Credentials
- [func checkPreferredNetwork(forActiveOperationalDataset: Data, completion: (Bool) -> Void)](./checkpreferrednetwork%28foractiveoperationaldataset,completion%29.md)
  Determines if the essential operating parameters match the preferred network’s parameters.
- [func retrieveCredentials(forBorderAgent: Data, completion: (THCredentials?, (any Error)?) -> Void)](./retrievecredentials%28forborderagent,completion%29.md)
  Requests Thread credentials for a Border Agent.
- [func retrieveCredentials(forExtendedPANID: Data, completion: (THCredentials?, (any Error)?) -> Void)](./retrievecredentials%28forextendedpanid,completion%29.md)
  Requests Thread credentials for an extended Personal Area Network (PAN) ID.
- [func retrieveAllCredentials((Set<THCredentials>?, (any Error)?) -> Void)](./retrieveallcredentials%28_%29.md)
  Requests all Thread credentials from the framework.
- [func retrievePreferredCredentials((THCredentials?, (any Error)?) -> Void)](./retrievepreferredcredentials%28_%29.md)
  Requests Thread credentials for the preferred network.
- [func retrieveAllActiveCredentials((Set<THCredentials>?, (any Error)?) -> Void)](./retrieveallactivecredentials%28_%29.md)
  Returns a set of the active credentials.


---

*[View on Apple Developer](https://developer.apple.com/documentation/threadnetwork/thclient/ispreferrednetworkavailable(completion:))*