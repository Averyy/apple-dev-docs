# init(coder:)

**Framework**: UIKit  
**Kind**: init  
**Role**: Initializer

Creates an alert view from data in an unarchiver.

**Availability**:
- iOS 2.0+ - Deprecated in 9.0
- iPadOS 2.0+ - Deprecated in 9.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: For more information, see [`UIAlertView`](../uialertview.md).

## Declaration

```swift
init?(coder: NSCoder)
```

```objc
- (instancetype) initWithCoder:(NSCoder *) coder;
```

## See Also

### Creating alert views
- [convenience init(title: String?, message: String?, delegate: Any?, cancelButtonTitle: String?)](./init%28title,message,delegate,cancelbuttontitle%29.md)
  Convenience method for initializing an alert view.
- [convenience init(title: String, message: String, delegate: (any UIAlertViewDelegate)?, cancelButtonTitle: String?, otherButtonTitles: String, String...)](./init%28title,message,delegate,cancelbuttontitle,otherbuttontitles,_%29.md)
  Creates an alert view with the specified values.
- [init(frame: CGRect)](./init%28frame%29.md)
  Creates an alert view with the specified frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uialertview/init(coder:))*