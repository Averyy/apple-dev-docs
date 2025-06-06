# constraints

**Framework**: Core Animation  
**Kind**: property

The constraints used to position current layer’s sublayers.

**Availability**:
- Mac Catalyst ?+
- macOS ?+

## Declaration

```swift
var constraints: [CAConstraint]? { get set }
```

#### Discussion

macOS apps can use this property to access their layer-based constraints. Before constraints can be applied, you must also assign a [`CAConstraintLayoutManager`](caconstraintlayoutmanager.md) object to the [`layoutManager`](calayer/layoutmanager.md) property of the layer.

iOS apps do not support layer-based constraints.

## See Also

- [func addConstraint(CAConstraint)](calayer/addconstraint(_:).md)
  Adds the specified constraint to the layer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/calayer/constraints)*