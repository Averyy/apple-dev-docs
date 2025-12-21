# contents

**Framework**: Touch Controller  
**Kind**: property

The contents for the touchpad.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Declaration

```swift
var contents: TCControlContents? { get set }
```

#### Discussion

May be `nil`.

## See Also

- [var highlightDuration: TimeInterval](tctouchpaddescriptor/highlightduration.md)
  The time it takes for a highlight to fade away, in seconds.
- [var label: TCControlLabel](tctouchpaddescriptor/label.md)
  The label associated with the touchpad.
- [var offset: CGPoint](tctouchpaddescriptor/offset.md)
  The control’s offset from the anchor, which determines its position.
- [var reportsRelativeValues: Bool](tctouchpaddescriptor/reportsrelativevalues.md)
  A Boolean value that represents the touchpad reports deltas.
- [var size: CGSize](tctouchpaddescriptor/size.md)
  The size (width, height) of the touchpad in points.
- [var zIndex: Int](tctouchpaddescriptor/zindex.md)
  The z-index of the touchpad. A lower z-index is drawn first.


---

*[View on Apple Developer](https://developer.apple.com/documentation/touchcontroller/tctouchpaddescriptor/contents)*