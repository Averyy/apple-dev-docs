# UICollectionView.SupplementaryRegistration.Handler

**Framework**: UIKit  
**Kind**: typealias  
**Role**: Type Alias

A closure that handles the supplementary view registration and configuration.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- tvOS 14.0+
- visionOS

## Declaration

```swift
typealias Handler = (Supplementary, String, IndexPath) -> Void
```

## See Also

### Creating a supplementary registration
- [init(elementKind: String, handler: UICollectionView.SupplementaryRegistration<Supplementary>.Handler)](./init%28elementkind,handler%29.md)
  Creates a supplementary registration for the specified element kind with a registration handler.
- [init(supplementaryNib: UINib, elementKind: String, handler: UICollectionView.SupplementaryRegistration<Supplementary>.Handler)](./init%28supplementarynib,elementkind,handler%29.md)
  Creates a supplementary registration for the specified element kind with a registration handler and nib file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionview/supplementaryregistration/handler)*