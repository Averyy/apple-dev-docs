# checkPreferredNetwork(forActiveOperationalDataset:completion:)

**Framework**: ThreadNetwork  
**Kind**: method  
**Role**: Instance Method

Determines if the essential operating parameters match the preferred network’s parameters.

**Availability**:
- iOS 15.5+
- iPadOS 15.5+
- Mac Catalyst 15.5+
- macOS 13.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
func checkPreferredNetwork(forActiveOperationalDataset activeOperationalDataSet: Data, completion: @escaping @Sendable (Bool) -> Void)
```

```swift
func isPreferred(forActiveOperationalDataset activeOperationalDataSet: Data) async -> Bool
```

```objc
- (void) checkPreferredNetworkForActiveOperationalDataset:(NSData *) activeOperationalDataSet completion:(void (^)(BOOL isPreferred)) completion;
```

## Mentions

- [Managing Thread network credentials](../managing-thread-network-credentials.md)
- [Configuring a Border Router](../configuring-a-border-router.md)

#### Discussion

> **Concurrency note**: You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration:
>
> ```swift
> func isPreferred(forActiveOperationalDataset activeOperationalDataSet: Data) async -> Bool
> ```
>
> For information about concurrency and asynchronous code in Swift, see [Calling Objective-C APIs Asynchronously](../../Swift/calling-objective-c-apis-asynchronously.md).

Call the method as follows:

```swift
func obtainPreferredNetwork(activeOperationalDataset: Data) async -> (NSString?) {
    let client = THClient()
    var bIsPreferred:Bool?
    bIsPreferred = await client.isPreferred(forActiveOperationalDataset: activeOperationalDataset)
    let str = ((bIsPreferred == true) ?"true" : "false")
    return str as NSString;
}
```

## Parameters

- `activeOperationalDataSet`: The essential operating parameters to compare against the preferred network’s parameters.
- `completion`: The completion handler that returns the result of the comparison.

## See Also

### Retrieving Credentials
- [func isPreferredNetworkAvailable(completion: (Bool) -> Void)](./ispreferrednetworkavailable%28completion%29.md)
  Indicates whether a preferred network is available.
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

*[View on Apple Developer](https://developer.apple.com/documentation/threadnetwork/thclient/checkpreferrednetwork(foractiveoperationaldataset:completion:))*