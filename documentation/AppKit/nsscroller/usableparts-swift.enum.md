# NSScroller.UsableParts

**Framework**: AppKit  
**Kind**: enum  
**Role**: Enumeration

These constants specify which parts of the scroller are visible.

**Availability**:
- macOS

## Declaration

```swift
enum UsableParts
```

```c
enum NSUsableScrollerParts : NSUInteger;
```

## Topics

### Constants
- [NSScroller.UsableParts.noScrollerParts](./usableparts-swift.enum/noscrollerparts.md)
  Specifies that the scroller has neither a knob nor scroll buttons, only the knob slot.
- [NSScroller.UsableParts.allScrollerParts](./usableparts-swift.enum/allscrollerparts.md)
  Specifies that the scroller has at least a knob, possibly also scroll buttons.
- [NSScroller.UsableParts.onlyScrollerArrows](./usableparts-swift.enum/onlyscrollerarrows.md)
  Specifies that the scroller has only scroll buttons, no knob.
### Initializers
- [init?(rawValue: UInt)](./usableparts-swift.enum/init%28rawvalue%29.md)

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
- [NSScroller.Style](./style.md)
  Constants to specify the scroller style.
- [NSScroller.KnobStyle](./knobstyle-swift.enum.md)
  Specify different knob styles.
- [NSScroller.Part](./part.md)
  These constants specify the different parts of the scroller:


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsscroller/usableparts-swift.enum)*