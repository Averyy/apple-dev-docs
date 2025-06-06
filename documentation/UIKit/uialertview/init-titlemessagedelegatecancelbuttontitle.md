# init(title:message:delegate:cancelButtonTitle:)

**Framework**: UIKit  
**Kind**: init

Convenience method for initializing an alert view.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
convenience init(title: String?, message: String?, delegate: Any?, cancelButtonTitle: String?)
```

#### Return Value

Newly initialized alert view.

## Parameters

- `title`: The string that appears in the receiver’s title bar.
- `message`: Descriptive text that provides more details than the title.
- `delegate`: The receiver’s delegate or   if it doesn’t have a delegate.
- `cancelButtonTitle`: Using this argument is equivalent to setting the cancel button index to the value returned by invoking   specifying this title.

## See Also

- [convenience init(title: String, message: String, delegate: (any UIAlertViewDelegate)?, cancelButtonTitle: String?, otherButtonTitles: String, String...)](uialertview/init(title:message:delegate:cancelbuttontitle:otherbuttontitles:_:).md)
  Creates an alert view with the specified values.
- [init(frame: CGRect)](uialertview/init(frame:).md)
  Creates an alert view with the specified frame.
- [init?(coder: NSCoder)](uialertview/init(coder:).md)
  Creates an alert view from data in an unarchiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uialertview/init(title:message:delegate:cancelbuttontitle:))*