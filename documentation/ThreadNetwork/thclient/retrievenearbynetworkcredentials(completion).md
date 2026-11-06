# retrieveNearbyNetworkCredentials(completion:)

**Framework**: ThreadNetwork  
**Kind**: method  
**Role**: Instance Method

Retrieves credentials for the active Thread networks nearby.

**Availability**:
- iOS 27.3+ (Beta)
- iPadOS 27.3+ (Beta)
- Mac Catalyst 27.3+ (Beta)
- macOS 13.0+
- visionOS 27.3+ (Beta)
- watchOS 27.3+ (Beta)

## Declaration

```swift
func retrieveNearbyNetworkCredentials(completion: @escaping @Sendable (Set<THNearbyNetworkCredentials>?, (any Error)?) -> Void)
```

```swift
var nearbyNetworkCredentials: Set<THNearbyNetworkCredentials> { get async throws }
```

```objc
- (void) retrieveNearbyNetworkCredentialsWithCompletion:(void (^)(NSSet<THNearbyNetworkCredentials *> *credentials, NSError *error)) completion;
```

## Discussion

You receive all credentials agnostic to team ID. Unlike [`retrieveAllActiveCredentials(_:)`](./retrieveallactivecredentials%28_%29.md), this method returns active credentials on the device regardless of which app actually stored them.

Check the `isPreferredNetworkCredentials` property on each [`THNearbyNetworkCredentials`](../thnearbynetworkcredentials.md) instance to see whether it belongs to the preferred network. It is `NO` on every instance not matching the preferred network.

> **Note**: This method asks for user permission to share available credentials. If user denies the permission then the completion will contain error with code 15.

> **Concurrency Note**: You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration:
>
> ```swift
> var nearbyNetworkCredentials: Set<THNearbyNetworkCredentials> { get async throws }
> ```
>
> For information about concurrency and asynchronous code in Swift, see [Calling Objective-C APIs Asynchronously](../../Swift/calling-objective-c-apis-asynchronously.md).

## Parameters

- `completion`: The completion handler the framework calls when the credentials become available.


---

*[View on Apple Developer](https://developer.apple.com/documentation/threadnetwork/thclient/retrievenearbynetworkcredentials(completion:))*