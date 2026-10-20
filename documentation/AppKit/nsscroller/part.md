# NSScroller.Part

**Framework**: AppKit  
**Kind**: enum  
**Role**: Enumeration

These constants specify the different parts of the scroller:

**Availability**:
- macOS

## Declaration

```swift
enum Part
```

```c
enum NSScrollerPart : NSUInteger;
```

## Topics

### Constants
- [NSScroller.Part.knob](./part/knob.md)
  Directly to the scroller’s value, as given by [`floatValue`](../nscontrol/floatvalue.md).
- [NSScroller.Part.knobSlot](./part/knobslot.md)
  Directly to the scroller’s value, as given by [`floatValue`](../nscontrol/floatvalue.md).
- [NSScroller.Part.decrementPage](./part/decrementpage.md)
  Up or left by a large amount.
- [NSScroller.Part.incrementPage](./part/incrementpage.md)
  Down or right by a large amount.
- [NSScroller.Part.noPart](./part/nopart.md)
  Don’t scroll at all.
- [NSScroller.Part.decrementLine](./part/decrementline.md)
  Up or left by a small amount.
- [NSScroller.Part.incrementLine](./part/incrementline.md)
  Down or right by a small amount.
### Initializers
- [init?(rawValue: UInt)](./part/init%28rawvalue%29.md)

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
- [NSScroller.UsableParts](./usableparts-swift.enum.md)
  These constants specify which parts of the scroller are visible.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsscroller/part)*