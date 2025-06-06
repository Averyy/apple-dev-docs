# isVisible

**Framework**: UIKit  
**Kind**: property

A Boolean value that indicates whether the receiver is displayed.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
var isVisible: Bool { get }
```

#### Discussion

If [`true`](https://developer.apple.com/documentation/swift/true), the receiver is displayed; otherwise, [`false`](https://developer.apple.com/documentation/swift/false).

## See Also

- [var delegate: AnyObject?](uialertview/delegate.md)
  The receiver’s delegate or `nil` if it doesn’t have a delegate.
- [var alertViewStyle: UIAlertViewStyle](uialertview/alertviewstyle.md)
  The kind of alert displayed to the user.
- [var title: String](uialertview/title.md)
  The string that appears in the receiver’s title bar.
- [var message: String?](uialertview/message.md)
  Descriptive text that provides more details than the title.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uialertview/isvisible)*