# delegate

**Framework**: UIKit  
**Kind**: property

The receiver’s delegate or `nil` if it doesn’t have a delegate.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
weak var delegate: AnyObject? { get set }
```

#### Discussion

See [`UIAlertViewDelegate`](uialertviewdelegate.md) for the methods this delegate should implement.

## See Also

- [var alertViewStyle: UIAlertViewStyle](uialertview/alertviewstyle.md)
  The kind of alert displayed to the user.
- [var title: String](uialertview/title.md)
  The string that appears in the receiver’s title bar.
- [var message: String?](uialertview/message.md)
  Descriptive text that provides more details than the title.
- [var isVisible: Bool](uialertview/isvisible.md)
  A Boolean value that indicates whether the receiver is displayed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uialertview/delegate)*