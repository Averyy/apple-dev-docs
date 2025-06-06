# addConstraint(_:)

**Framework**: Core Animation  
**Kind**: method

Adds the specified constraint to the layer.

**Availability**:
- Mac Catalyst ?+
- macOS ?+

## Declaration

```swift
func addConstraint(_ c: CAConstraint)
```

#### Discussion

In macOS, you typically add constraints to a layer to manage the size and position of that layer’s sublayers. Before constraints can be applied, you must also assign a [`CAConstraintLayoutManager`](caconstraintlayoutmanager.md) object to the [`layoutManager`](calayer/layoutmanager.md) property of the layer. For more information about managing layer-based constraints, see [`Core Animation Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CoreAnimation_guide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40004514).

iOS apps do not support layer-based constraints.

## Parameters

- `c`: The constraint object to add to the receiver’s array of constraint objects.

## See Also

- [var constraints: [CAConstraint]?](calayer/constraints.md)
  The constraints used to position current layer’s sublayers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/calayer/addconstraint(_:))*