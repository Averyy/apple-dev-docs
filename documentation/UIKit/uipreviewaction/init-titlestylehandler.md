# init(title:style:handler:)

**Framework**: UIKit  
**Kind**: init

Creates a peek quick action using a specified title, style, and handler.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+

## Declaration

```swift
@MainActor
convenience init(title: String, style: UIPreviewAction.Style, handler: @escaping (UIPreviewAction, UIViewController) -> Void)
```

#### Return Value

A newly-created peek quick action.

## Parameters

- `title`: The quick action’s title.
- `style`: The quick action’s style. For a complete list of styles, see the   enumeration in  .
- `handler`: A block that is called when the user selects the peek quick action. The block takes the following parameters:

## See Also

- [var handler: (any UIPreviewActionItem, UIViewController) -> Void](uipreviewaction/handler.md)
  The block called when the peek quick action is selected by the user.
- [UIPreviewAction.Style](uipreviewaction/style.md)
  The style for a peek quick action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipreviewaction/init(title:style:handler:))*