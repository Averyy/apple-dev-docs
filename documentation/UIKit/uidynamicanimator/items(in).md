# items(in:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Returns the dynamic items, from the animator’s behaviors, that intersect a specified rectangle.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
func items(in rect: CGRect) -> [any UIDynamicItem]
```

```objc
- (NSArray<id<UIDynamicItem>> *) itemsInRect:(CGRect) rect;
```

#### Return Value

The dynamic items, from the animator’s behaviors, that intersect the specified rectangle.

#### Discussion

The coordinate system that pertains to the `rect` parameter depends on how you initialized the animator, as described in the Overview in this document.

## Parameters

- `rect`: The rectangle you are interested in.

## See Also

### Initializing and managing a dynamic animator
- [init(referenceView: UIView)](./init%28referenceview%29.md)
  Initializes a dynamic animator with a specified view as its reference view.
- [convenience init(collectionViewLayout: UICollectionViewLayout)](./init%28collectionviewlayout%29.md)
  Initializes a dynamic animator with a specified collection view layout.
- [func addBehavior(UIDynamicBehavior)](./addbehavior%28_%29.md)
  Adds a dynamic behavior to a dynamic animator.
- [func removeBehavior(UIDynamicBehavior)](./removebehavior%28_%29.md)
  Removes a specified dynamic behavior from a dynamic animator.
- [func removeAllBehaviors()](./removeallbehaviors%28%29.md)
  Removes all of the dynamic behaviors from a dynamic animator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidynamicanimator/items(in:))*