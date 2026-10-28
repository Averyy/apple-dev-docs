# isVisible

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the receiver is displayed.

**Availability**:
- iOS 2.0+ - Deprecated in 8.3
- iPadOS 2.0+ - Deprecated in 8.3
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: For more information, see [`UIActionSheet`](../uiactionsheet.md).

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
- [var delegate: (any UIActionSheetDelegate)?](./delegate.md)
  The receiver’s delegate or `nil` if it doesn’t have a delegate.
- [var title: String](./title.md)
  The string that appears in the receiver’s title bar.
- [var actionSheetStyle: UIActionSheetStyle](./actionsheetstyle.md)
  The receiver’s presentation style.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiactionsheet/isvisible)*