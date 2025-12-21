# stickContents

**Framework**: Touch Controller  
**Kind**: property

The contents for the thumbstick itself.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Declaration

```swift
var stickContents: TCControlContents? { get set }
```

#### Discussion

May be `nil`.

## See Also

- [var backgroundContents: TCControlContents?](tcthumbstickdescriptor/backgroundcontents.md)
  The contents for the background of the thumbstick.
- [var hidesWhenNotPressed: Bool](tcthumbstickdescriptor/hideswhennotpressed.md)
  Whether to hide the thumbstick when it is not being pressed.
- [var highlightDuration: TimeInterval](tcthumbstickdescriptor/highlightduration.md)
  The time it takes for a highlight to fade away, in seconds.
- [var label: TCControlLabel](tcthumbstickdescriptor/label.md)
  The label associated with the thumbstick.
- [var offset: CGPoint](tcthumbstickdescriptor/offset.md)
  The control’s offset from the anchor, which determines its position.
- [var size: CGSize](tcthumbstickdescriptor/size.md)
  The size (width, height) of the thumbstick in points.
- [var stickSize: CGSize](tcthumbstickdescriptor/sticksize.md)
  The size (width, height) of the thumbstick stick itself in points.
- [var zIndex: Int](tcthumbstickdescriptor/zindex.md)
  The z-index of the thumbstick. A lower z-index is drawn first.


---

*[View on Apple Developer](https://developer.apple.com/documentation/touchcontroller/tcthumbstickdescriptor/stickcontents)*