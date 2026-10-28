# actionSheetStyle

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The receiver’s presentation style.

**Availability**:
- iOS 2.0+ - Deprecated in 8.3
- iPadOS 2.0+ - Deprecated in 8.3
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: For more information, see [`UIActionSheet`](../uiactionsheet.md).

## Declaration

```swift
var actionSheetStyle: UIActionSheetStyle { get set }
```

```objc
@property (nonatomic) UIActionSheetStyle actionSheetStyle;
```

## Discussion

This property determines how the action sheet looks when it is presented. For a list of possible values, see the [`UIActionSheetStyle`](../uiactionsheetstyle.md) constants.

## See Also

### Setting properties
- [var delegate: (any UIActionSheetDelegate)?](./delegate.md)
  The receiver’s delegate or `nil` if it doesn’t have a delegate.
- [var title: String](./title.md)
  The string that appears in the receiver’s title bar.
- [var isVisible: Bool](./isvisible.md)
  A Boolean value that indicates whether the receiver is displayed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiactionsheet/actionsheetstyle)*