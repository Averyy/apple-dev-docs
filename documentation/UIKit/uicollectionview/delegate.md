# delegate

**Framework**: UIKit  
**Kind**: property

The object that acts as the delegate of the collection view.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
weak var delegate: (any UICollectionViewDelegate)? { get set }
```

#### Discussion

The delegate must adopt the [`UICollectionViewDelegate`](uicollectionviewdelegate.md) protocol. The delegate object is responsible for managing selection behavior and interactions with individual items.

## See Also

- [protocol UICollectionViewDelegate](uicollectionviewdelegate.md)
  The methods adopted by the object you use to manage user interactions with items in a collection view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionview/delegate)*