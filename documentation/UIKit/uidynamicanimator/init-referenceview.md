# init(referenceView:)

**Framework**: UIKit  
**Kind**: init

Initializes a dynamic animator with a specified view as its reference view.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
init(referenceView view: UIView)
```

#### Return Value

The initialized dynamic animator, or `nil` if there was a problem initializing the object.

#### Discussion

When you initialize a dynamic animator with this method, the behaviors (and their dynamic items) that you add to the animator employ the reference view’s coordinate system.

## Parameters

- `view`: The view for the dynamic animator, called the  .

## See Also

- [convenience init(collectionViewLayout: UICollectionViewLayout)](uidynamicanimator/init(collectionviewlayout:).md)
  Initializes a dynamic animator with a specified collection view layout.
- [func items(in: CGRect) -> [any UIDynamicItem]](uidynamicanimator/items(in:).md)
  Returns the dynamic items, from the animator’s behaviors, that intersect a specified rectangle.
- [func addBehavior(UIDynamicBehavior)](uidynamicanimator/addbehavior(_:).md)
  Adds a dynamic behavior to a dynamic animator.
- [func removeBehavior(UIDynamicBehavior)](uidynamicanimator/removebehavior(_:).md)
  Removes a specified dynamic behavior from a dynamic animator.
- [func removeAllBehaviors()](uidynamicanimator/removeallbehaviors.md)
  Removes all of the dynamic behaviors from a dynamic animator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidynamicanimator/init(referenceview:))*