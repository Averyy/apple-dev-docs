# init(collectionViewLayout:)

**Framework**: UIKit  
**Kind**: init

Initializes a dynamic animator with a specified collection view layout.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
convenience init(collectionViewLayout layout: UICollectionViewLayout)
```

#### Return Value

The initialized dynamic animator, or `nil` if there was a problem initializing the object.

#### Discussion

When you initialize a dynamic animator with this method, the behaviors (and their dynamic items) that you add to the animator employ the collection view layout’s coordinate system.

## Parameters

- `layout`: The collection view layout for the dynamic animator, serving as the reference view for a dynamic animator in collection-view mode.

## See Also

- [init(referenceView: UIView)](uidynamicanimator/init(referenceview:).md)
  Initializes a dynamic animator with a specified view as its reference view.
- [func items(in: CGRect) -> [any UIDynamicItem]](uidynamicanimator/items(in:).md)
  Returns the dynamic items, from the animator’s behaviors, that intersect a specified rectangle.
- [func addBehavior(UIDynamicBehavior)](uidynamicanimator/addbehavior(_:).md)
  Adds a dynamic behavior to a dynamic animator.
- [func removeBehavior(UIDynamicBehavior)](uidynamicanimator/removebehavior(_:).md)
  Removes a specified dynamic behavior from a dynamic animator.
- [func removeAllBehaviors()](uidynamicanimator/removeallbehaviors.md)
  Removes all of the dynamic behaviors from a dynamic animator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidynamicanimator/init(collectionviewlayout:))*