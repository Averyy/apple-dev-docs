# reportsRelativeValues

**Framework**: Touch Controller  
**Kind**: property

A Boolean value that represents the touchpad reports deltas.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Declaration

```swift
var reportsRelativeValues: Bool { get set }
```

#### Discussion

If `YES`, the touchpad will report delta values as touch moves instead of absolute positions.

## See Also

- [var contents: TCControlContents?](tctouchpaddescriptor/contents.md)
  The contents for the touchpad.
- [var highlightDuration: TimeInterval](tctouchpaddescriptor/highlightduration.md)
  The time it takes for a highlight to fade away, in seconds.
- [var label: TCControlLabel](tctouchpaddescriptor/label.md)
  The label associated with the touchpad.
- [var offset: CGPoint](tctouchpaddescriptor/offset.md)
  The control’s offset from the anchor, which determines its position.
- [var size: CGSize](tctouchpaddescriptor/size.md)
  The size (width, height) of the touchpad in points.
- [var zIndex: Int](tctouchpaddescriptor/zindex.md)
  The z-index of the touchpad. A lower z-index is drawn first.


---

*[View on Apple Developer](https://developer.apple.com/documentation/touchcontroller/tctouchpaddescriptor/reportsrelativevalues)*