# isPreferredNetworkCredentials

**Framework**: ThreadNetwork  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether these credentials belong to the preferred network.

**Availability**:
- iOS 27.3+ (Beta)
- iPadOS 27.3+ (Beta)
- Mac Catalyst 27.3+ (Beta)
- macOS 13.0+
- visionOS 27.3+ (Beta)
- watchOS 27.3+ (Beta)

## Declaration

```swift
var isPreferredNetworkCredentials: Bool { get }
```

```objc
@property (nonatomic, assign, readonly) BOOL isPreferredNetworkCredentials;
```

## Discussion

`YES` when this nearby network is the user/system-preferred network to join, `NO` otherwise.

> **Note**: The value is a snapshot and doesn’t update if the preferred network changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/threadnetwork/thnearbynetworkcredentials/ispreferrednetworkcredentials)*