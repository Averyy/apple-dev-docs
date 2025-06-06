# remembersLastFocusedIndexPath

**Framework**: UIKit  
**Kind**: property

A Boolean value that indicates whether the collection view automatically assigns the focus to the item at the last focused index path.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var remembersLastFocusedIndexPath: Bool { get set }
```

#### Discussion

When this property is set to [`true`](https://developer.apple.com/documentation/swift/true), the collection view remembers which index path was focused when focus leaves the collection view. When it receives the focus again, the collection view automatically redirects that focus back to the previously focused index path. The default value of this property is [`false`](https://developer.apple.com/documentation/swift/false).

The effects of this property may be ignored during or immediately after a view controller transition, such as a presentation dismissal or navigation stack pop. In such cases, the view controller attempts to restore focus to the item that was focused prior to the transition (for example, prior to the view controller being presented or pushed), which can take precedence over the effects of this property. To learn how to control or disable this behavior in the view controller, see [`restoresFocusAfterTransition`](uiviewcontroller/restoresfocusaftertransition.md).

## See Also

- [var allowsFocus: Bool](uicollectionview/allowsfocus.md)
  A Boolean value that determines whether the collection view allows its cells to become focused.
- [var allowsFocusDuringEditing: Bool](uicollectionview/allowsfocusduringediting.md)
  A Boolean value that determines whether the collection view allows its cells to become focused in edit mode.
- [var selectionFollowsFocus: Bool](uicollectionview/selectionfollowsfocus.md)
  A Boolean value that triggers an automatic selection when focus moves to a cell.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionview/rememberslastfocusedindexpath)*