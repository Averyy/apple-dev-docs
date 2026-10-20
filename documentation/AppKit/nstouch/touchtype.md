# NSTouch.TouchType

**Framework**: AppKit  
**Kind**: enum  
**Role**: Enumeration

A bit mask identifying a direct or indirect touch type.

**Availability**:
- macOS 10.12.2+

## Declaration

```swift
enum TouchType
```

```c
enum NSTouchType : NSInteger;
```

## Topics

### Touch Types
- [NSTouch.TouchType.direct](./touchtype/direct.md)
  A direct touch from a user’s finger on a screen.
- [NSTouch.TouchType.indirect](./touchtype/indirect.md)
  An indirect touch that is not on a screen, like a digitizer touch.
### Initializers
- [init?(rawValue: Int)](./touchtype/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Getting the Touch Type
- [var type: NSTouch.TouchType](./type.md)
  A type of touch from a Touch Bar interaction.
- [NSTouch.TouchTypeMask](./touchtypemask.md)
  A bit mask identifying a direct or indirect touch type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstouch/touchtype)*