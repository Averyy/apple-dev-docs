# items(in:)

**Framework**: UIKit  
**Kind**: method

Returns the dynamic items, from the animator’s behaviors, that intersect a specified rectangle.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
func items(in rect: CGRect) -> [any UIDynamicItem]
```

#### Return Value

The dynamic items, from the animator’s behaviors, that intersect the specified rectangle.

#### Discussion

The coordinate system that pertains to the `rect` parameter depends on how you initialized the animator, as described in the Overview in this document.

## Parameters

- `rect`: The rectangle you are interested in.

## See Also

- [init(referenceView: UIView)](uidynamicanimator/init(referenceview:).md)
  Initializes a dynamic animator with a specified view as its reference view.
- [convenience init(collectionViewLayout: UICollectionViewLayout)](uidynamicanimator/init(collectionviewlayout:).md)
  Initializes a dynamic animator with a specified collection view layout.
- [func addBehavior(UIDynamicBehavior)](uidynamicanimator/addbehavior(_:).md)
  Adds a dynamic behavior to a dynamic animator.
- [func removeBehavior(UIDynamicBehavior)](uidynamicanimator/removebehavior(_:).md)
  Removes a specified dynamic behavior from a dynamic animator.
- [func removeAllBehaviors()](uidynamicanimator/removeallbehaviors.md)
  Removes all of the dynamic behaviors from a dynamic animator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidynamicanimator/items(in:))*