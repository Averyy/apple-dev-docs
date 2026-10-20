# constraints

**Framework**: Core Animation  
**Kind**: property  
**Role**: Instance Property

The constraints used to position current layer’s sublayers.

**Availability**:
- Mac Catalyst 13.1+
- macOS

## Declaration

```swift
var constraints: [CAConstraint]? { get set }
```

```objc
@property (copy, nullable) NSArray<CAConstraint *> * constraints;
```

#### Discussion

macOS apps can use this property to access their layer-based constraints. Before constraints can be applied, you must also assign a [`CAConstraintLayoutManager`](../caconstraintlayoutmanager.md) object to the [`layoutManager`](./layoutmanager.md) property of the layer.

iOS apps do not support layer-based constraints.

## See Also

### Managing layer constraints
- [func addConstraint(CAConstraint)](./addconstraint%28_%29.md)
  Adds the specified constraint to the layer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/calayer/constraints)*