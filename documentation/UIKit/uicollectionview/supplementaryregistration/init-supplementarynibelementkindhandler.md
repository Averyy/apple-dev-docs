# init(supplementaryNib:elementKind:handler:)

**Framework**: UIKit  
**Kind**: init

Creates a supplementary registration for the specified element kind with a registration handler and nib file.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst ?+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
init(supplementaryNib: UINib, elementKind: String, handler: @escaping UICollectionView.SupplementaryRegistration<Supplementary>.Handler)
```

## See Also

- [init(elementKind: String, handler: UICollectionView.SupplementaryRegistration<Supplementary>.Handler)](uicollectionview/supplementaryregistration/init(elementkind:handler:).md)
  Creates a supplementary registration for the specified element kind with a registration handler.
- [UICollectionView.SupplementaryRegistration.Handler](uicollectionview/supplementaryregistration/handler.md)
  A closure that handles the supplementary view registration and configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionview/supplementaryregistration/init(supplementarynib:elementkind:handler:))*