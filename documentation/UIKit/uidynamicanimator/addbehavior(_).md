# addBehavior(_:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Adds a dynamic behavior to a dynamic animator.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
func addBehavior(_ behavior: UIDynamicBehavior)
```

```objc
- (void) addBehavior:(UIDynamicBehavior *) behavior;
```

## Parameters

- `behavior`: The dynamic behavior instance you are adding.

  The dynamic animator ignores your use of this method if you:

  - Provide a `nil` value
  - Provide a behavior instance that you’ve already added to the animator at the same level in the behavior hierarchy

  > ❗ **Important**:  The dynamic animator raises an exception if you provide a behavior instance that you’ve already added to the animator at a different level in the behavior hierarchy.

## See Also

### Initializing and managing a dynamic animator
- [init(referenceView: UIView)](./init%28referenceview%29.md)
  Initializes a dynamic animator with a specified view as its reference view.
- [convenience init(collectionViewLayout: UICollectionViewLayout)](./init%28collectionviewlayout%29.md)
  Initializes a dynamic animator with a specified collection view layout.
- [func items(in: CGRect) -> [any UIDynamicItem]](./items%28in%29.md)
  Returns the dynamic items, from the animator’s behaviors, that intersect a specified rectangle.
- [func removeBehavior(UIDynamicBehavior)](./removebehavior%28_%29.md)
  Removes a specified dynamic behavior from a dynamic animator.
- [func removeAllBehaviors()](./removeallbehaviors%28%29.md)
  Removes all of the dynamic behaviors from a dynamic animator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidynamicanimator/addbehavior(_:))*