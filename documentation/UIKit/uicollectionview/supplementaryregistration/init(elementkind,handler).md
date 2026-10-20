# init(elementKind:handler:)

**Framework**: UIKit  
**Kind**: init  
**Role**: Initializer

Creates a supplementary registration for the specified element kind with a registration handler.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- tvOS 14.0+
- visionOS

## Declaration

```swift
init(elementKind: String, handler: @escaping UICollectionView.SupplementaryRegistration<Supplementary>.Handler)
```

## See Also

### Creating a supplementary registration
- [init(supplementaryNib: UINib, elementKind: String, handler: UICollectionView.SupplementaryRegistration<Supplementary>.Handler)](./init%28supplementarynib,elementkind,handler%29.md)
  Creates a supplementary registration for the specified element kind with a registration handler and nib file.
- [UICollectionView.SupplementaryRegistration.Handler](./handler.md)
  A closure that handles the supplementary view registration and configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionview/supplementaryregistration/init(elementkind:handler:))*