# preferredMaxLayoutWidth

**Framework**: AppKit  
**Kind**: property

The maximum width of the text field’s intrinsic content size.

**Availability**:
- macOS 10.8+

## Declaration

```swift
@MainActor
var preferredMaxLayoutWidth: CGFloat { get set }
```

#### Discussion

If the text field wraps, the intrinsic height is large enough to show the entire text contents at that width.

The default value is `0`, indicating no maximum preferred width.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextfield/preferredmaxlayoutwidth)*