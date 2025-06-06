# handler

**Framework**: UIKit  
**Kind**: property

The block called when the peek quick action is selected by the user.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+

## Declaration

```swift
@MainActor
var handler: (any UIPreviewActionItem, UIViewController) -> Void { get }
```

#### Discussion

The handler is set when the peek quick action is instantiated; it is immutable.

## See Also

- [convenience init(title: String, style: UIPreviewAction.Style, handler: (UIPreviewAction, UIViewController) -> Void)](uipreviewaction/init(title:style:handler:).md)
  Creates a peek quick action using a specified title, style, and handler.
- [UIPreviewAction.Style](uipreviewaction/style.md)
  The style for a peek quick action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipreviewaction/handler)*