# removeBehavior(_:)

**Framework**: UIKit  
**Kind**: method

Removes a specified dynamic behavior from a dynamic animator.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
func removeBehavior(_ behavior: UIDynamicBehavior)
```

## Parameters

- `behavior`: The dynamic animator ignores your use of this method if you:

## See Also

- [init(referenceView: UIView)](uidynamicanimator/init(referenceview:).md)
  Initializes a dynamic animator with a specified view as its reference view.
- [convenience init(collectionViewLayout: UICollectionViewLayout)](uidynamicanimator/init(collectionviewlayout:).md)
  Initializes a dynamic animator with a specified collection view layout.
- [func items(in: CGRect) -> [any UIDynamicItem]](uidynamicanimator/items(in:).md)
  Returns the dynamic items, from the animator’s behaviors, that intersect a specified rectangle.
- [func addBehavior(UIDynamicBehavior)](uidynamicanimator/addbehavior(_:).md)
  Adds a dynamic behavior to a dynamic animator.
- [func removeAllBehaviors()](uidynamicanimator/removeallbehaviors.md)
  Removes all of the dynamic behaviors from a dynamic animator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidynamicanimator/removebehavior(_:))*