# order

**Framework**: RealityKit  
**Kind**: property

An integer value that represents when the renderer draws the model relative to other the models in its group.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+ (Beta)
- visionOS 1.0+

## Declaration

```swift
var order: Int32 { get set }
```

#### Discussion

The renderer draws models in ascending order, starting with the components with the smallest value. You can tell the renderer that it only needs to order entities by their depths by setting the component’s [`order`](modelsortgroupcomponent/order.md) property to the sam value for those entities.

> ⚠️ **Warning**: Don’t set `order` to `Int32.max` or `Int32.min` because the framework reserves these as sentinel values, and assigning their values may trigger erratic behavior.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/modelsortgroupcomponent/order)*