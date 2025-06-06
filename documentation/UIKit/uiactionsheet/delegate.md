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
weak var delegate: (any UIActionSheetDelegate)? { get set }
```

#### Discussion

For a list of methods your delegate object can implement, see [`UIActionSheetDelegate`](uiactionsheetdelegate.md).

## See Also

- [var title: String](uiactionsheet/title.md)
  The string that appears in the receiver’s title bar.
- [var isVisible: Bool](uiactionsheet/isvisible.md)
  A Boolean value that indicates whether the receiver is displayed.
- [var actionSheetStyle: UIActionSheetStyle](uiactionsheet/actionsheetstyle.md)
  The receiver’s presentation style.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiactionsheet/delegate)*