# currentLayout

**Framework**: UIKit  
**Kind**: property

The collection view’s current layout object.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var currentLayout: UICollectionViewLayout { get }
```

#### Discussion

This object provides the layout attributes representing the initial position of items in the collection view. If you ultimately cancel the transition, the collection view animates its items back to the positions provided by this object.

## See Also

- [var nextLayout: UICollectionViewLayout](uicollectionviewtransitionlayout/nextlayout.md)
  The collection view’s new layout object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewtransitionlayout/currentlayout)*