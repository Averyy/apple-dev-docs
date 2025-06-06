# showsTouchWhenHighlighted

**Framework**: UIKit  
**Kind**: property

A Boolean value that determines whether tapping the button causes it to glow.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var showsTouchWhenHighlighted: Bool { get set }
```

#### Discussion

If [`true`](https://developer.apple.com/documentation/swift/true), the button glows when tapped; otherwise, it does not. The image and button behavior is not changed by the glow. The default value is [`false`](https://developer.apple.com/documentation/swift/false).

## See Also

- [var adjustsImageWhenHighlighted: Bool](uibutton/adjustsimagewhenhighlighted.md)
  A Boolean value that determines whether the image changes when the button is highlighted.
- [var adjustsImageWhenDisabled: Bool](uibutton/adjustsimagewhendisabled.md)
  A Boolean value that determines whether the image changes when the button is disabled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibutton/showstouchwhenhighlighted)*