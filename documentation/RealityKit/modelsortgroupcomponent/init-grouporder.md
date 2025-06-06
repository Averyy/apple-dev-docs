# init(group:order:)

**Framework**: RealityKit  
**Kind**: init

Creates a model sort group component.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 1.0+

## Declaration

```swift
init(group: ModelSortGroup, order: Int32)
```

#### Discussion

> ⚠️ **Warning**: Don’t pass `Int32.max` or `Int32.min` to the `order` parameter because the framework reserves these as sentinel values, and using them may trigger erratic behavior.

Don’t pass `Int32.max` or `Int32.min` to the `order` parameter because the framework reserves these as sentinel values, and using them may trigger erratic behavior.

## Parameters

- `group`: A group the component’s entity belongs to.
- `order`: An integer value in the range   that   represents when the renderer draws the model relative to other the   models in its group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/modelsortgroupcomponent/init(group:order:))*