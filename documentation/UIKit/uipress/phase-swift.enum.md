# UIPress.Phase

**Framework**: UIKit  
**Kind**: enum  
**Role**: Enumeration

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

```c
enum UIPressPhase : NSInteger;
```

## Topics

### Constants
- [UIPress.Phase.began](./phase-swift.enum/began.md)
  A physical button was pressed.
- [UIPress.Phase.changed](./phase-swift.enum/changed.md)
  A button moved, or the force property changed.
- [UIPress.Phase.stationary](./phase-swift.enum/stationary.md)
  A button was pressed but hasn’t moved since the previous event.
- [UIPress.Phase.ended](./phase-swift.enum/ended.md)
  A button was released.
- [UIPress.Phase.cancelled](./phase-swift.enum/cancelled.md)
  The system canceled tracking for the button.
### Initializers
- [init?(rawValue: Int)](./phase-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Constants
- [UIPress.PressType](./presstype.md)
  Constants that represent buttons that a person can press.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipress/phase-swift.enum)*