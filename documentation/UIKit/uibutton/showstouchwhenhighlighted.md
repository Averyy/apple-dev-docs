# showsTouchWhenHighlighted

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that determines whether tapping the button causes it to glow.

**Availability**:
- iOS 2.0+ - Deprecated in 15.0
- iPadOS 2.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: The system ignores this when you use [`UIButton.Configuration`](./configuration-swift.struct.md).

## Declaration

```swift
var showsTouchWhenHighlighted: Bool { get set }
```

```objc
@property (nonatomic) BOOL showsTouchWhenHighlighted;
```

## Discussion

If [`true`](../../Swift/true.md), the button glows when tapped; otherwise, it does not. The image and button behavior is not changed by the glow. The default value is [`false`](../../Swift/false.md).

## See Also

### Deprecated button presentation
- [var adjustsImageWhenHighlighted: Bool](./adjustsimagewhenhighlighted.md)
  A Boolean value that determines whether the image changes when the button is highlighted.
- [var adjustsImageWhenDisabled: Bool](./adjustsimagewhendisabled.md)
  A Boolean value that determines whether the image changes when the button is disabled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibutton/showstouchwhenhighlighted)*