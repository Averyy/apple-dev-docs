# delegate

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The receiver’s delegate or `nil` if it doesn’t have a delegate.

**Availability**:
- iOS 2.0+ - Deprecated in 8.3
- iPadOS 2.0+ - Deprecated in 8.3
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: For more information, see [`UIActionSheet`](../uiactionsheet.md).

## Declaration

```swift
weak var delegate: (any UIActionSheetDelegate)? { get set }
```

```objc
@property (nonatomic, weak, nullable) id<UIActionSheetDelegate> delegate;
```

#### Discussion

For a list of methods your delegate object can implement, see [`UIActionSheetDelegate`](../uiactionsheetdelegate.md).

## See Also

### Setting properties
- [var title: String](./title.md)
  The string that appears in the receiver’s title bar.
- [var isVisible: Bool](./isvisible.md)
  A Boolean value that indicates whether the receiver is displayed.
- [var actionSheetStyle: UIActionSheetStyle](./actionsheetstyle.md)
  The receiver’s presentation style.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiactionsheet/delegate)*