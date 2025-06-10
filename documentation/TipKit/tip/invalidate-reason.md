# invalidate(reason:)

**Framework**: TipKit  
**Kind**: method

Permanently invalidates a tip and prevents it from displaying.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
func invalidate(reason: Self.InvalidationReason)
```

## Parameters

- `reason`: The reason for the tip’s invalidation. The tip’s   returns this value after invalidation.

## See Also

- [func resetEligibility() async](tip/reseteligibility.md)
  Reset a previously invalidated tip.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tipkit/tip/invalidate(reason:))*