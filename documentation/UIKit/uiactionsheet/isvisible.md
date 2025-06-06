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

- [var delegate: (any UIActionSheetDelegate)?](uiactionsheet/delegate.md)
  The receiver’s delegate or `nil` if it doesn’t have a delegate.
- [var title: String](uiactionsheet/title.md)
  The string that appears in the receiver’s title bar.
- [var actionSheetStyle: UIActionSheetStyle](uiactionsheet/actionsheetstyle.md)
  The receiver’s presentation style.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiactionsheet/isvisible)*