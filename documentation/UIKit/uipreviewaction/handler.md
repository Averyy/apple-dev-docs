# handler

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The block called when the peek quick action is selected by the user.

**Availability**:
- iOS 9.0+ - Deprecated in 13.0
- iPadOS 9.0+ - Deprecated in 13.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- tvOS 9.0+ - Deprecated in 13.0

> **Deprecated**: For more information, see [`UIPreviewAction`](../uipreviewaction.md).

## Declaration

```swift
var handler: (any UIPreviewActionItem, UIViewController) -> Void { get }
```

```objc
@property (nonatomic, copy, readonly) void (^)(id<UIPreviewActionItem>, UIViewController *) handler;
```

## Discussion

The handler is set when the peek quick action is instantiated; it is immutable.

## See Also

### Creating a peek quick action
- [convenience init(title: String, style: UIPreviewAction.Style, handler: (UIPreviewAction, UIViewController) -> Void)](./init%28title,style,handler%29.md)
  Creates a peek quick action using a specified title, style, and handler.
- [UIPreviewAction.Style](./style.md)
  The style for a peek quick action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipreviewaction/handler)*