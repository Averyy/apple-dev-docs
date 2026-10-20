# init(referenceView:)

**Framework**: UIKit  
**Kind**: init  
**Role**: Initializer

Initializes a dynamic animator with a specified view as its reference view.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
init(referenceView view: UIView)
```

```objc
- (instancetype) initWithReferenceView:(UIView *) view;
```

#### Return Value

The initialized dynamic animator, or `nil` if there was a problem initializing the object.

#### Discussion

When you initialize a dynamic animator with this method, the behaviors (and their dynamic items) that you add to the animator employ the reference view’s coordinate system.

## Parameters

- `view`: The view for the dynamic animator, called the *reference view*.

## See Also

### Initializing and managing a dynamic animator
- [convenience init(collectionViewLayout: UICollectionViewLayout)](./init%28collectionviewlayout%29.md)
  Initializes a dynamic animator with a specified collection view layout.
- [func items(in: CGRect) -> [any UIDynamicItem]](./items%28in%29.md)
  Returns the dynamic items, from the animator’s behaviors, that intersect a specified rectangle.
- [func addBehavior(UIDynamicBehavior)](./addbehavior%28_%29.md)
  Adds a dynamic behavior to a dynamic animator.
- [func removeBehavior(UIDynamicBehavior)](./removebehavior%28_%29.md)
  Removes a specified dynamic behavior from a dynamic animator.
- [func removeAllBehaviors()](./removeallbehaviors%28%29.md)
  Removes all of the dynamic behaviors from a dynamic animator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidynamicanimator/init(referenceview:))*