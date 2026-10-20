# NSColor.SystemEffect

**Framework**: AppKit  
**Kind**: enum  
**Role**: Enumeration

Constants for user interactions that change the appearance of a view or control.

**Availability**:
- macOS 10.14+

## Declaration

```swift
enum SystemEffect
```

```c
enum NSColorSystemEffect : NSInteger;
```

## Topics

### Appearances
- [NSColor.SystemEffect.none](./systemeffect/none.md)
  No additional effects.
- [NSColor.SystemEffect.pressed](./systemeffect/pressed.md)
  The color that indicates the item was pressed.
- [NSColor.SystemEffect.deepPressed](./systemeffect/deeppressed.md)
  The color that indicates the item received a deep press.
- [NSColor.SystemEffect.disabled](./systemeffect/disabled.md)
  The color that indicates the item is disabled.
- [NSColor.SystemEffect.rollover](./systemeffect/rollover.md)
  The color that indicates the mouse rolled over the item.
### Initializers
- [init?(rawValue: Int)](./systemeffect/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Applying specific appearances to colors
- [func withSystemEffect(NSColor.SystemEffect) -> NSColor](./withsystemeffect%28_%29.md)
  Returns a new color object that represents the current color modified to include the specified visual effect.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolor/systemeffect)*