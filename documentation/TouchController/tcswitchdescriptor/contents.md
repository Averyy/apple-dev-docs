# contents

**Framework**: Touch Controller  
**Kind**: property

The contents for the switch in its normal state.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Declaration

```swift
var contents: TCControlContents? { get set }
```

#### Discussion

This value can be `nil`.

## See Also

- [var highlightDuration: TimeInterval](tcswitchdescriptor/highlightduration.md)
  The time it takes for a highlight to fade away, in seconds.
- [var label: TCControlLabel](tcswitchdescriptor/label.md)
  The label you associate with the switch.
- [var offset: CGPoint](tcswitchdescriptor/offset.md)
  The control’s offset from the anchor, which determines its position.
- [var size: CGSize](tcswitchdescriptor/size.md)
  The size (width, height) of the switch in points.
- [var switchedOnContents: TCControlContents?](tcswitchdescriptor/switchedoncontents.md)
  The contents for the switch when it is switched on.
- [var zIndex: Int](tcswitchdescriptor/zindex.md)
  The z-index of the switch. A lower z-index is drawn first.


---

*[View on Apple Developer](https://developer.apple.com/documentation/touchcontroller/tcswitchdescriptor/contents)*