# contents

**Framework**: Touch Controller  
**Kind**: property  
**Role**: Instance Property

The contents for the touchpad.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
var contents: TCControlContents? { get set }
```

```objc
@property (nonatomic, strong, nullable) TCControlContents * contents;
```

#### Discussion

May be `nil`.

## See Also

### Inspecting the descriptor
- [var highlightDuration: TimeInterval](./highlightduration.md)
  The time it takes for a highlight to fade away, in seconds.
- [var label: TCControlLabel](./label.md)
  The label associated with the touchpad.
- [var offset: CGPoint](./offset.md)
  The control’s offset from the anchor, which determines its position.
- [var reportsRelativeValues: Bool](./reportsrelativevalues.md)
  A Boolean value that represents the touchpad reports deltas.
- [var size: CGSize](./size.md)
  The size (width, height) of the touchpad in points.
- [var zIndex: Int](./zindex.md)
  The z-index of the touchpad. A lower z-index is drawn first.


---

*[View on Apple Developer](https://developer.apple.com/documentation/touchcontroller/tctouchpaddescriptor/contents)*