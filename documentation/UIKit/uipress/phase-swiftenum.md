# UIPress.Phase

**Framework**: UIKit  
**Kind**: enum

Constants that represent the phases of a button press.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
enum Phase
```

## Topics

### Constants
- [UIPress.Phase.began](uipress/phase-swift.enum/began.md)
  A physical button was pressed.
- [UIPress.Phase.changed](uipress/phase-swift.enum/changed.md)
  A button moved, or the force property changed.
- [UIPress.Phase.stationary](uipress/phase-swift.enum/stationary.md)
  A button was pressed but hasn’t moved since the previous event.
- [UIPress.Phase.ended](uipress/phase-swift.enum/ended.md)
  A button was released.
- [UIPress.Phase.cancelled](uipress/phase-swift.enum/cancelled.md)
  The system canceled tracking for the button.
### Initializers
- [init?(rawValue: Int)](uipress/phase-swift.enum/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [UIPress.PressType](uipress/presstype.md)
  Constants that represent buttons that a person can press.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipress/phase-swift.enum)*