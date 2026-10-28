# init(title:style:handler:)

**Framework**: UIKit  
**Kind**: init  
**Role**: Initializer

Creates a peek quick action using a specified title, style, and handler.

**Availability**:
- iOS 9.0+ - Deprecated in 13.0
- iPadOS 9.0+ - Deprecated in 13.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- tvOS 9.0+ - Deprecated in 13.0

> **Deprecated**: For more information, see [`UIPreviewAction`](../uipreviewaction.md).

## Declaration

```swift
convenience init(title: String, style: UIPreviewAction.Style, handler: @escaping (UIPreviewAction, UIViewController) -> Void)
```

```objc
+ (instancetype) actionWithTitle:(NSString *) title style:(UIPreviewActionStyle) style handler:(void (^)(UIPreviewAction *action, UIViewController *previewViewController)) handler;
```

## Return Value

A newly-created peek quick action.

## Parameters

- `title`: The quick action’s title.
- `style`: The quick action’s style. For a complete list of styles, see the `UIPreviewActionStyle` enumeration in *UIPreviewActionItem Protocol Reference*.
- `handler`: A block that is called when the user selects the peek quick action. The block takes the following parameters:

  - **action**: The peek quick action selected by the user.
  - **previewViewController**: The view controller displayed as the peek.

## See Also

### Creating a peek quick action
- [var handler: (any UIPreviewActionItem, UIViewController) -> Void](./handler.md)
  The block called when the peek quick action is selected by the user.
- [UIPreviewAction.Style](./style.md)
  The style for a peek quick action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipreviewaction/init(title:style:handler:))*