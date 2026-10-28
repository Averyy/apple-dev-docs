# contents

**Framework**: Touch Controller  
**Kind**: property  
**Role**: Instance Property

The contents for the button in its normal state.

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

## Discussion

This value can be `nil`.

## See Also

### Inspecting the descriptor
- [var highlightDuration: TimeInterval](./highlightduration.md)
  The time it takes for a highlight to fade away, in seconds.
- [var zIndex: Int](./zindex.md)
  The z-index of the button. A lower z-index is drawn first.
- [var label: TCControlLabel](./label.md)
  The label you associate with the button.
- [var offset: CGPoint](./offset.md)
  The control’s offset from the anchor, which determines its position.
- [var size: CGSize](./size.md)
  The size (width, height) of the button in points.


---

*[View on Apple Developer](https://developer.apple.com/documentation/touchcontroller/tcbuttondescriptor/contents)*