# init()

**Framework**: GameplayKit  
**Kind**: init  
**Role**: Initializer

Initializes a new entity object.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
init()
```

```objc
- (instancetype) init;
```

## Return Value

A new entity object.

## Discussion

If you create a [`GKEntity`](../gkentity.md) subclass and define any additional initializers, you must delegate to this initializer. You do not need to subclass [`GKEntity`](../gkentity.md) to use Entity-Component architecture—generally, you should create a custom entity class only when you need a place to store state or resources that are shared by multiple components.

For more information, see [GameplayKit Programming Guide](https://developer.apple.com/library/archive/documentation/General/Conceptual/GameplayKit_Guide/index.html#//apple_ref/doc/uid/TP40015172).

## See Also

### Creating an Entity
- [+ entity](./entity.md)
  Creates a new entity object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkentity/init())*