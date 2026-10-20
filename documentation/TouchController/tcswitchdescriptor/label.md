# label

**Framework**: Touch Controller  
**Kind**: property  
**Role**: Instance Property

The label you associate with the switch.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
var label: TCControlLabel { get set }
```

```objc
@property (nonatomic, strong) TCControlLabel * label;
```

## See Also

### Inspecting the descriptor
- [var contents: TCControlContents?](./contents.md)
  The contents for the switch in its normal state.
- [var highlightDuration: TimeInterval](./highlightduration.md)
  The time it takes for a highlight to fade away, in seconds.
- [var offset: CGPoint](./offset.md)
  The control’s offset from the anchor, which determines its position.
- [var size: CGSize](./size.md)
  The size (width, height) of the switch in points.
- [var switchedOnContents: TCControlContents?](./switchedoncontents.md)
  The contents for the switch when it is switched on.
- [var zIndex: Int](./zindex.md)
  The z-index of the switch. A lower z-index is drawn first.


---

*[View on Apple Developer](https://developer.apple.com/documentation/touchcontroller/tcswitchdescriptor/label)*