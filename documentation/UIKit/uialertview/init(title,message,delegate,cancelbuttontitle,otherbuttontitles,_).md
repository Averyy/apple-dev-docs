# init(title:message:delegate:cancelButtonTitle:otherButtonTitles:_:)

**Framework**: UIKit  
**Kind**: init  
**Role**: Initializer

Creates an alert view with the specified values.

**Availability**:
- iOS 2.0+ - Deprecated in 9.0
- iPadOS 2.0+ - Deprecated in 9.0
- Mac Catalyst 2.0+ - Deprecated in 9.0

> **Deprecated**: For more information, see [`UIAlertView`](../uialertview.md).

## Declaration

```swift
@MainActor
@preconcurrency convenience init(title: String, message: String, delegate: (any UIAlertViewDelegate)?, cancelButtonTitle: String?, otherButtonTitles firstButtonTitle: String, _ moreButtonTitles: String...)
```

## See Also

### Creating alert views
- [convenience init(title: String?, message: String?, delegate: Any?, cancelButtonTitle: String?)](./init%28title,message,delegate,cancelbuttontitle%29.md)
  Convenience method for initializing an alert view.
- [init(frame: CGRect)](./init%28frame%29.md)
  Creates an alert view with the specified frame.
- [init?(coder: NSCoder)](./init%28coder%29.md)
  Creates an alert view from data in an unarchiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uialertview/init(title:message:delegate:cancelbuttontitle:otherbuttontitles:_:))*