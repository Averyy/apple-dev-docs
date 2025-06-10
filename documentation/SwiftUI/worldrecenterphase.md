# WorldRecenterPhase

**Framework**: SwiftUI  
**Kind**: enum

A type that represents information associated with a phase of a system recenter event. Values of this type are passed to the closure specified in View.onWorldRecenter(action:).

**Availability**:
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
enum WorldRecenterPhase
```

## Topics

### Enumeration Cases
- [WorldRecenterPhase.began](worldrecenterphase/began.md)
  The app has begun to fade out. It is not re-positioned yet.
- [WorldRecenterPhase.ended](worldrecenterphase/ended.md)
  The app has begun to fade in after it has been re-positioned.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/worldrecenterphase)*