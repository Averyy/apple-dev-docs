# adjustsImageWhenHighlighted

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that determines whether the image changes when the button is highlighted.

**Availability**:
- iOS 2.0+ - Deprecated in 15.0
- iPadOS 2.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- tvOS 2.0+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: Use [`configurationUpdateHandler`](./configurationupdatehandler-swift.property.md) instead.

## Declaration

```swift
var adjustsImageWhenHighlighted: Bool { get set }
```

```objc
@property (nonatomic) BOOL adjustsImageWhenHighlighted;
```

## Discussion

If [`true`](../../Swift/true.md), the image is drawn lighter when the button is highlighted. The default value is [`true`](../../Swift/true.md).

## See Also

### Deprecated button presentation
- [var adjustsImageWhenDisabled: Bool](./adjustsimagewhendisabled.md)
  A Boolean value that determines whether the image changes when the button is disabled.
- [var showsTouchWhenHighlighted: Bool](./showstouchwhenhighlighted.md)
  A Boolean value that determines whether tapping the button causes it to glow.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibutton/adjustsimagewhenhighlighted)*