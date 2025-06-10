# CAConstraintLayoutManager

**Framework**: Core Animation  
**Kind**: class

An object that provides a constraint-based layout manager.

**Availability**:
- Mac Catalyst 13.1+
- macOS 10.5+

## Declaration

```swift
class CAConstraintLayoutManager
```

#### Overview

You use the shared instance of this object by assigning it to the [`layoutManager`](calayer/layoutmanager.md) property of any layer objects to which you have added constraints. During a layout update, Core Animation uses the layout manager to update the size and position of the sublayers based on the registered set of constraints.

Constraints let you define a set of geometric relationships between a layer and its sibling layers or between a layer and its superlayer. These relationships are expressed using constraint objects, which are instances of the [`CAConstraint`](caconstraint.md) class. When creating constraints, you can reference a layer by name using that object’s [`name`](calayer/name.md) property. You can also use the special name `superlayer` to refer to the layer’s superlayer.

The following example shows how you can use [`CAConstraintLayoutManager`](caconstraintlayoutmanager.md) to create a layer containing two constrained sublayers: `leftLayer` and `rightLayer`. A series of [`CAConstraint`](caconstraint.md) objects are created so that the sublayers match their superlayer’s height and are half of its width. `leftConstraint` matches the [`CAConstraintAttribute.minX`](caconstraintattribute/minx.md) attribute and `rightConstraint` matches the [`CAConstraintAttribute.maxX`](caconstraintattribute/maxx.md) attribute.

The end result is that the two sublayers are always laid out so that `leftLayer` fills the left half of `layer` and `rightLayer` fills the right half of layer.

```swift
let layer = CALayer()
let heightConstraint = CAConstraint(attribute: .height,
                                    relativeTo: "superlayer",
                                    attribute: .height)
    
let widthConstraint = CAConstraint(attribute: .width,
                                   relativeTo: "superlayer",
                                   attribute: .width,
                                   scale: 0.5,
                                   offset: 0)
     
let leftConstraint = CAConstraint(attribute: .minX,
                                  relativeTo: "superlayer",
                                  attribute: .minX)
     
let rightConstraint = CAConstraint(attribute: .maxX,
                                   relativeTo: "superlayer",
                                   attribute: .maxX)
    
let bottomConstraint = CAConstraint(attribute: .minY,
                                    relativeTo: "superlayer",
                                    attribute: .minY)   
     
let leftLayer = CALayer()
leftLayer.frame = CGRect(x: 0, y: 0, width: 20, height: 20)
layer.addSublayer(leftLayer)
leftLayer.constraints = [heightConstraint, widthConstraint, 
                         leftConstraint, bottomConstraint]
leftLayer.backgroundColor = NSColor.red.cgColor
  
let rightLayer = CALayer()
layer.addSublayer(rightLayer)
rightLayer.constraints = [heightConstraint, widthConstraint, 
                          rightConstraint, bottomConstraint]
rightLayer.backgroundColor = NSColor.blue.cgColor
    
layer.layoutManager = CAConstraintLayoutManager()
```

> ❗ **Important**:  It is possible to specify a set of constraints that will cause layout to fail. For example, layout may fail if your constraints contain a circular dependency. When that happens, the behavior of the layout manager is undefined.

This class is not meant to be subclassed.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CALayoutManager](calayoutmanager.md)
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class CALayer](calayer.md)
  An object that manages image-based content and allows you to perform animations on that content.
- [protocol CALayerDelegate](calayerdelegate.md)
  Methods your app can implement to respond to layer-related events.
- [class CAConstraint](caconstraint.md)
  A representation of a single layout constraint between two layers.
- [protocol CALayoutManager](calayoutmanager.md)
  Methods that allow an object to manage the layout of a layer and its sublayers.
- [protocol CAAction](caaction.md)
  An interface that allows instances to respond to actions triggered by a Core Animation layer change.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/caconstraintlayoutmanager)*