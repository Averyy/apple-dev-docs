# NSFocusRingPlacement

**Framework**: AppKit  
**Kind**: enum  
**Role**: Enumeration

Constants that indicate how the system draws the focus ring.

**Availability**:
- macOS

## Declaration

```swift
enum NSFocusRingPlacement
```

```c
enum NSFocusRingPlacement : NSUInteger;
```

## Topics

### Constants
- [NSFocusRingPlacement.above](./nsfocusringplacement/above.md)
  Draw the focus ring over an image.
- [NSFocusRingPlacement.below](./nsfocusringplacement/below.md)
  Draw the focus ring under text.
- [NSFocusRingPlacement.only](./nsfocusringplacement/only.md)
  Draw the focus ring if you don’t have an image or text.
### Options for Drawing
- [func set()](./nsfocusringplacement/set%28%29.md)
  Specifies how the system draws the focus ring.
### Initializers
- [init?(rawValue: UInt)](./nsfocusringplacement/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Drawing Focus Rings
- [func set()](./nsfocusringplacement/set%28%29.md)
  Specifies how the system draws the focus ring.
- [enum NSFocusRingType](./nsfocusringtype.md)
  Constants that describe the style of the focus ring.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfocusringplacement)*