# active

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The state of the push behavior’s force: either active or inactive.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var active: Bool { get set }
```

```objc
@property (nonatomic, readwrite) BOOL active;
```

## Discussion

After you’ve added a push behavior to a dynamic animator, use this property to activate or deactivate the behavior’s force (rather than removing and then re-adding the behavior to the animator).

## See Also

### Initializing and managing a push behavior
- [func addItem(any UIDynamicItem)](./additem%28_%29.md)
  Adds a dynamic item to the behavior’s dynamic item array.
- [init(items: [any UIDynamicItem], mode: UIPushBehavior.Mode)](./init%28items,mode%29.md)
  Initializes a push behavior with an array of dynamic items.
- [func removeItem(any UIDynamicItem)](./removeitem%28_%29.md)
  Removes a specific dynamic item from the behavior.
- [var items: [any UIDynamicItem]](./items.md)
  Returns the set of dynamic items you’ve added to the push behavior.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipushbehavior/active)*