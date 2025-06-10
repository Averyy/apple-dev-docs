# nextLayout

**Framework**: UIKit  
**Kind**: property

The collection view’s new layout object.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var nextLayout: UICollectionViewLayout { get }
```

#### Discussion

This object provides the layout attributes representing the new position of items in the collection view. If the transition completes as expected, the collection view animates its items to the positions provided by this object.

## See Also

- [var currentLayout: UICollectionViewLayout](uicollectionviewtransitionlayout/currentlayout.md)
  The collection view’s current layout object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewtransitionlayout/nextlayout)*