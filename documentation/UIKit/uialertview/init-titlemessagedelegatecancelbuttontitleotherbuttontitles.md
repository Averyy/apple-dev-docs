# init(title:message:delegate:cancelButtonTitle:otherButtonTitles:_:)

**Framework**: UIKit  
**Kind**: init

Creates an alert view with the specified values.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst ?+

## Declaration

```swift
@MainActor
@preconcurrency convenience init(title: String, message: String, delegate: (any UIAlertViewDelegate)?, cancelButtonTitle: String?, otherButtonTitles firstButtonTitle: String, _ moreButtonTitles: String...)
```

## See Also

- [convenience init(title: String?, message: String?, delegate: Any?, cancelButtonTitle: String?)](uialertview/init(title:message:delegate:cancelbuttontitle:).md)
  Convenience method for initializing an alert view.
- [init(frame: CGRect)](uialertview/init(frame:).md)
  Creates an alert view with the specified frame.
- [init?(coder: NSCoder)](uialertview/init(coder:).md)
  Creates an alert view from data in an unarchiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uialertview/init(title:message:delegate:cancelbuttontitle:otherbuttontitles:_:))*