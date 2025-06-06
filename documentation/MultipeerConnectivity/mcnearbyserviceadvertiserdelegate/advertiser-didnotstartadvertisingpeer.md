# advertiser(_:didNotStartAdvertisingPeer:)

**Framework**: Multipeer Connectivity  
**Kind**: method

Called when advertisement fails.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
optional func advertiser(_ advertiser: MCNearbyServiceAdvertiser, didNotStartAdvertisingPeer error: any Error)
```

## Parameters

- `advertiser`: The advertiser object that failed to begin advertising.
- `error`: An error object that indicates what went wrong.


---

*[View on Apple Developer](https://developer.apple.com/documentation/multipeerconnectivity/mcnearbyserviceadvertiserdelegate/advertiser(_:didnotstartadvertisingpeer:))*