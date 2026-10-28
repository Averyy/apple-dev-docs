# init(title:message:delegate:cancelButtonTitle:)

**Framework**: UIKit  
**Kind**: init  
**Role**: Initializer

Convenience method for initializing an alert view.

**Availability**:
- iOS 2.0+ - Deprecated in 9.0
- iPadOS 2.0+ - Deprecated in 9.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: For more information, see [`UIAlertView`](../uialertview.md).

## Declaration

```swift
convenience init(title: String?, message: String?, delegate: Any?, cancelButtonTitle: String?)
```

```objc
- (instancetype) initWithTitle:(NSString *) title message:(NSString *) message delegate:(id) delegate cancelButtonTitle:(NSString *) cancelButtonTitle otherButtonTitles:(NSString *) otherButtonTitles;
```

## Return Value

Newly initialized alert view.

## Parameters

- `title`: The string that appears in the receiver’s title bar.
- `message`: Descriptive text that provides more details than the title.
- `delegate`: The receiver’s delegate or `nil` if it doesn’t have a delegate.
- `cancelButtonTitle`: The title of the cancel button or `nil` if there’s no cancel button.

  Using this argument is equivalent to setting the cancel button index to the value returned by invoking [`addButton(withTitle:)`](./addbutton%28withtitle%29.md) specifying this title.

## See Also

### Creating alert views
- [convenience init(title: String, message: String, delegate: (any UIAlertViewDelegate)?, cancelButtonTitle: String?, otherButtonTitles: String, String...)](./init%28title,message,delegate,cancelbuttontitle,otherbuttontitles,_%29.md)
  Creates an alert view with the specified values.
- [init(frame: CGRect)](./init%28frame%29.md)
  Creates an alert view with the specified frame.
- [init?(coder: NSCoder)](./init%28coder%29.md)
  Creates an alert view from data in an unarchiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uialertview/init(title:message:delegate:cancelbuttontitle:))*