# delegate

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The receiver’s delegate or `nil` if it doesn’t have a delegate.

**Availability**:
- iOS 2.0+ - Deprecated in 9.0
- iPadOS 2.0+ - Deprecated in 9.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: For more information, see [`UIAlertView`](../uialertview.md).

## Declaration

```swift
weak var delegate: AnyObject? { get set }
```

```objc
@property (nonatomic, weak, nullable) id delegate;
```

#### Discussion

See [`UIAlertViewDelegate`](../uialertviewdelegate.md) for the methods this delegate should implement.

## See Also

### Setting properties
- [var alertViewStyle: UIAlertViewStyle](./alertviewstyle.md)
  The kind of alert displayed to the user.
- [var title: String](./title.md)
  The string that appears in the receiver’s title bar.
- [var message: String?](./message.md)
  Descriptive text that provides more details than the title.
- [var isVisible: Bool](./isvisible.md)
  A Boolean value that indicates whether the receiver is displayed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uialertview/delegate)*