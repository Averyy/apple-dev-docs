# items

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

Returns the set of dynamic items you’ve added to the collision behavior.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var items: [any UIDynamicItem] { get }
```

```objc
@property (nonatomic, copy, readonly) NSArray<id<UIDynamicItem>> * items;
```

## See Also

### Initializing and managing a collision behavior
- [func addItem(any UIDynamicItem)](./additem%28_%29.md)
  Adds a dynamic item to the collision behavior’s item array.
- [init(items: [any UIDynamicItem])](./init%28items%29.md)
  Initializes a collision behavior with an array of dynamic items.
- [func removeItem(any UIDynamicItem)](./removeitem%28_%29.md)
  Removes a specific dynamic item from the collision behavior.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollisionbehavior/items)*