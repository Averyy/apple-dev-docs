# size

**Framework**: Touch Controller  
**Kind**: property  
**Role**: Instance Property

The size (width, height) of the touchpad in points.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
var size: CGSize { get set }
```

```objc
@property (nonatomic, assign) CGSize size;
```

## See Also

### Inspecting the descriptor
- [var contents: TCControlContents?](./contents.md)
  The contents for the touchpad.
- [var highlightDuration: TimeInterval](./highlightduration.md)
  The time it takes for a highlight to fade away, in seconds.
- [var label: TCControlLabel](./label.md)
  The label associated with the touchpad.
- [var offset: CGPoint](./offset.md)
  The control’s offset from the anchor, which determines its position.
- [var reportsRelativeValues: Bool](./reportsrelativevalues.md)
  A Boolean value that represents the touchpad reports deltas.
- [var zIndex: Int](./zindex.md)
  The z-index of the touchpad. A lower z-index is drawn first.


---

*[View on Apple Developer](https://developer.apple.com/documentation/touchcontroller/tctouchpaddescriptor/size)*