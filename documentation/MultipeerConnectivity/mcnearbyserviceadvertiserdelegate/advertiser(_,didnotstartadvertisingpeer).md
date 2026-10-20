# advertiser(_:didNotStartAdvertisingPeer:)

**Framework**: Multipeer Connectivity  
**Kind**: method  
**Role**: Instance Method

Called when advertisement fails.

**Availability**:
- iOS 7.0+ - Deprecated in 27.0
- iPadOS 7.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- macOS 10.10+ - Deprecated in 27.0
- tvOS 10.0+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0

> **Deprecated**: Use Network Framework instead

## Declaration

```swift
optional func advertiser(_ advertiser: MCNearbyServiceAdvertiser, didNotStartAdvertisingPeer error: any Error)
```

```objc
- (void) advertiser:(MCNearbyServiceAdvertiser *) advertiser didNotStartAdvertisingPeer:(NSError *) error;
```

## Parameters

- `advertiser`: The advertiser object that failed to begin advertising.
- `error`: An error object that indicates what went wrong.


---

*[View on Apple Developer](https://developer.apple.com/documentation/multipeerconnectivity/mcnearbyserviceadvertiserdelegate/advertiser(_:didnotstartadvertisingpeer:))*