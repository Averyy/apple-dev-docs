# allowsFocusDuringEditing

**Framework**: UIKit  
**Kind**: property

A Boolean value that determines whether the collection view allows its cells to become focused in edit mode.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var allowsFocusDuringEditing: Bool { get set }
```

#### Discussion

If you implement [`collectionView(_:canFocusItemAt:)`](uicollectionviewdelegate/collectionview(_:canfocusitemat:).md), its return value takes precedence over the value of this property.

The system determines the default value of this property according to the platform and other properties of the collection view.

## See Also

- [var allowsFocus: Bool](uicollectionview/allowsfocus.md)
  A Boolean value that determines whether the collection view allows its cells to become focused.
- [var selectionFollowsFocus: Bool](uicollectionview/selectionfollowsfocus.md)
  A Boolean value that triggers an automatic selection when focus moves to a cell.
- [var remembersLastFocusedIndexPath: Bool](uicollectionview/rememberslastfocusedindexpath.md)
  A Boolean value that indicates whether the collection view automatically assigns the focus to the item at the last focused index path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionview/allowsfocusduringediting)*