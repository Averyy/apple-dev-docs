# stickSize

**Framework**: Touch Controller  
**Kind**: property  
**Role**: Instance Property

The size (width, height) of the thumbstick stick itself in points.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
var stickSize: CGSize { get set }
```

```objc
@property (nonatomic, assign) CGSize stickSize;
```

## See Also

### Inspecting the descriptor
- [var backgroundContents: TCControlContents?](./backgroundcontents.md)
  The contents for the background of the thumbstick.
- [var hidesWhenNotPressed: Bool](./hideswhennotpressed.md)
  Whether to hide the thumbstick when it is not being pressed.
- [var highlightDuration: TimeInterval](./highlightduration.md)
  The time it takes for a highlight to fade away, in seconds.
- [var label: TCControlLabel](./label.md)
  The label associated with the thumbstick.
- [var offset: CGPoint](./offset.md)
  The control’s offset from the anchor, which determines its position.
- [var size: CGSize](./size.md)
  The size (width, height) of the thumbstick in points.
- [var stickContents: TCControlContents?](./stickcontents.md)
  The contents for the thumbstick itself.
- [var zIndex: Int](./zindex.md)
  The z-index of the thumbstick. A lower z-index is drawn first.


---

*[View on Apple Developer](https://developer.apple.com/documentation/touchcontroller/tcthumbstickdescriptor/sticksize)*