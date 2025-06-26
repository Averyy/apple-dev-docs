# AnchorStateEvents.DidFailToAnchor.Reason

**Framework**: RealityKit  
**Kind**: enum

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
enum Reason
```

## Topics

### Enumeration Cases
- [AnchorStateEvents.DidFailToAnchor.Reason.addAnchorFailed](anchorstateevents/didfailtoanchor/reason-swift.enum/addanchorfailed.md)
  anchor fails to be added, due to anchor tracking provider error
- [AnchorStateEvents.DidFailToAnchor.Reason.anchorNotSupported](anchorstateevents/didfailtoanchor/reason-swift.enum/anchornotsupported.md)
  anchor fails because the anchor type is not supported by the hardware configuration
- [AnchorStateEvents.DidFailToAnchor.Reason.maximumLimitReached](anchorstateevents/didfailtoanchor/reason-swift.enum/maximumlimitreached.md)
  anchor fails to be added, due to anchor tracking provider reaching its maximum anchor limit
- [AnchorStateEvents.DidFailToAnchor.Reason.unspecified](anchorstateevents/didfailtoanchor/reason-swift.enum/unspecified.md)
  anchor fails with no specified reason

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/anchorstateevents/didfailtoanchor/reason-swift.enum)*