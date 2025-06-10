# UICollectionView.SupplementaryRegistration.Handler

**Framework**: UIKit  
**Kind**: typealias

A closure that handles the supplementary view registration and configuration.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst ?+
- tvOS 14.0+
- visionOS ?+

## Declaration

```swift
typealias Handler = (Supplementary, String, IndexPath) -> Void
```

## See Also

- [init(elementKind: String, handler: UICollectionView.SupplementaryRegistration<Supplementary>.Handler)](uicollectionview/supplementaryregistration/init(elementkind:handler:).md)
  Creates a supplementary registration for the specified element kind with a registration handler.
- [init(supplementaryNib: UINib, elementKind: String, handler: UICollectionView.SupplementaryRegistration<Supplementary>.Handler)](uicollectionview/supplementaryregistration/init(supplementarynib:elementkind:handler:).md)
  Creates a supplementary registration for the specified element kind with a registration handler and nib file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionview/supplementaryregistration/handler)*