# isVisible

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the receiver is displayed.

**Availability**:
- iOS 2.0+ - Deprecated in 9.0
- iPadOS 2.0+ - Deprecated in 9.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: For more information, see [`UIAlertView`](../uialertview.md).

## Declaration

```swift
var isVisible: Bool { get }
```

```objc
@property (nonatomic, readonly, getter=isVisible) BOOL visible;
```

## Discussion

If [`true`](../../Swift/true.md), the receiver is displayed; otherwise, [`false`](../../Swift/false.md).

## See Also

### Setting properties
- [var delegate: AnyObject?](./delegate.md)
  The receiver’s delegate or `nil` if it doesn’t have a delegate.
- [var alertViewStyle: UIAlertViewStyle](./alertviewstyle.md)
  The kind of alert displayed to the user.
- [var title: String](./title.md)
  The string that appears in the receiver’s title bar.
- [var message: String?](./message.md)
  Descriptive text that provides more details than the title.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uialertview/isvisible)*