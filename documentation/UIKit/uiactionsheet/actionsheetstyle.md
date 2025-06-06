# actionSheetStyle

**Framework**: UIKit  
**Kind**: property

The receiver’s presentation style.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
var actionSheetStyle: UIActionSheetStyle { get set }
```

#### Discussion

This property determines how the action sheet looks when it is presented. For a list of possible values, see the [`UIActionSheetStyle`](uiactionsheetstyle.md) constants.

## See Also

- [var delegate: (any UIActionSheetDelegate)?](uiactionsheet/delegate.md)
  The receiver’s delegate or `nil` if it doesn’t have a delegate.
- [var title: String](uiactionsheet/title.md)
  The string that appears in the receiver’s title bar.
- [var isVisible: Bool](uiactionsheet/isvisible.md)
  A Boolean value that indicates whether the receiver is displayed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiactionsheet/actionsheetstyle)*