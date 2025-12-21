# NSLayoutConstraint

**Framework**: UIKit  
**Kind**: class

The relationship between two user interface objects that must be satisfied by the constraint-based layout system.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class NSLayoutConstraint
```

#### Overview

Each constraint is a linear equation with the following format:

```objc
item1.attribute1 = multiplier × item2.attribute2 + constant
```

In this equation, `attribute1` and `attribute2` are the variables that Auto Layout can adjust when solving these constraints. The other values are defined when you create the constraint. For example, if you’re defining the relative position of two buttons, you might say “the leading edge of the second button should be 8 points after the trailing edge of the first button.” The linear equation for this relationship is shown below:

```objc
// positive values move to the right in left-to-right languages like English.
button2.leading = 1.0 × button1.trailing + 8.0
```

Auto Layout then modifies the values of the specified leading and trailing edges until both sides of the equation are equal. Note that Auto Layout does not simply assign the value of the right side of this equation to the left side. Instead, the system can modify either attribute or both attributes as needed to solve for this constraint.

The fact that constraints are equations (and not assignment operators) means that you can switch the order of the items in the equation as needed to more clearly express the desired relationship. However, if you switch the order, you must also invert the multiplier and constant. For example, the following two equations produce identical constraints:

```objc
// These equations produce identical constraints
button2.leading = 1.0 × button1.trailing + 8.0
button1.trailing = 1.0 × button2.leading - 8.0
```

A valid layout is defined as a set of constraints with one and only one possible solution. Valid layouts are also referred to as a nonambiguous, nonconflicting layouts. Constraints with more than one solution are ambiguous. Constraints with no valid solutions are conflicting. For more information on resolving ambiguous and conflicting constraints, see [`Types of Errors`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/AutolayoutPG/TypesofErrors.html#//apple_ref/doc/uid/TP40010853-CH17) in [`Auto Layout Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/AutolayoutPG/index.html#//apple_ref/doc/uid/TP40010853).

Additionally, constraints are not limited to equality relationships. They can also use greater than or equal to (>=) or less than or equal to (<=) to describe the relationship between the two attributes. Constraints also have priorities between 1 and 1,000. Constraints with a priority of 1,000 are required. All priorities less than 1,000 are optional. By default, all constraints are required (priority = 1,000).

After solving for the required constraints, Auto Layout tries to solve all the optional constraints in priority order from highest to lowest. If it cannot solve for an optional constraint, it tries to come as close as possible to the desired result, and then moves on to the next constraint.

This combination of inequalities, equalities, and priorities gives you a great amount of flexibility and power. By combining multiple constraints, you can define layouts that dynamically adapt as the size and location of the elements in your user interface change. For some example layouts, see [`Stack Views`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/AutolayoutPG/LayoutUsingStackViews.html#//apple_ref/doc/uid/TP40010853-CH11) in [`Auto Layout Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/AutolayoutPG/index.html#//apple_ref/doc/uid/TP40010853).

## Topics

### Creating constraints
- [class func constraints(withVisualFormat: String, options: NSLayoutConstraint.FormatOptions, metrics: [String : Any]?, views: [String : Any]) -> [NSLayoutConstraint]](nslayoutconstraint/constraints(withvisualformat:options:metrics:views:).md)
  Creates constraints described by an ASCII art-like visual format string.
- [convenience init(item: Any, attribute: NSLayoutConstraint.Attribute, relatedBy: NSLayoutConstraint.Relation, toItem: Any?, attribute: NSLayoutConstraint.Attribute, multiplier: CGFloat, constant: CGFloat)](nslayoutconstraint/init(item:attribute:relatedby:toitem:attribute:multiplier:constant:).md)
  Creates a constraint that defines the relationship between the specified attributes of the given views.
### Activating and deactivating constraints
- [var isActive: Bool](nslayoutconstraint/isactive.md)
  The active state of the constraint.
- [class func activate([NSLayoutConstraint])](nslayoutconstraint/activate(_:).md)
  Activates each constraint in the specified array.
- [class func deactivate([NSLayoutConstraint])](nslayoutconstraint/deactivate(_:).md)
  Deactivates each constraint in the specified array.
### Accessing constraint data
- [var firstItem: AnyObject?](nslayoutconstraint/firstitem.md)
  The first object participating in the constraint.
- [var firstAttribute: NSLayoutConstraint.Attribute](nslayoutconstraint/firstattribute.md)
  The attribute of the first object participating in the constraint.
- [var relation: NSLayoutConstraint.Relation](nslayoutconstraint/relation-swift.property.md)
  The relation between the two attributes in the constraint.
- [var secondItem: AnyObject?](nslayoutconstraint/seconditem.md)
  The second object participating in the constraint.
- [var secondAttribute: NSLayoutConstraint.Attribute](nslayoutconstraint/secondattribute.md)
  The attribute of the second object participating in the constraint.
- [var multiplier: CGFloat](nslayoutconstraint/multiplier.md)
  The multiplier applied to the second attribute participating in the constraint.
- [var constant: CGFloat](nslayoutconstraint/constant.md)
  The constant added to the multiplied second attribute participating in the constraint.
- [var firstAnchor: NSLayoutAnchor<AnyObject>](nslayoutconstraint/firstanchor.md)
  The first anchor that defines the constraint.
- [var secondAnchor: NSLayoutAnchor<AnyObject>?](nslayoutconstraint/secondanchor.md)
  The second anchor that defines the constraint.
### Getting the layout priority
- [var priority: UILayoutPriority](nslayoutconstraint/priority.md)
  The priority of the constraint.
- [struct UILayoutPriority](uilayoutpriority.md)
  The layout priority is used to indicate to the constraint-based layout system which constraints are more important, allowing the system to make appropriate tradeoffs when satisfying the constraints of the system as a whole.
- [NSLayoutConstraint.Priority](../AppKit/NSLayoutConstraint/Priority-swift.struct.md)
  Layout priority used to indicate the relative importance of constraints, allowing Auto Layout to make appropriate tradeoffs when satisfying the constraints of the system as a whole.
### Identifying a constraint
- [var identifier: String?](nslayoutconstraint/identifier.md)
  The name that identifies the constraint.
### Controlling constraint archiving
- [var shouldBeArchived: Bool](nslayoutconstraint/shouldbearchived.md)
  A Boolean value that determines whether the constraint should be archived by its owning view.
### Constants
- [NSLayoutConstraint.Relation](nslayoutconstraint/relation-swift.enum.md)
  The relation between the first attribute and the modified second attribute in a constraint.
- [NSLayoutConstraint.Attribute](nslayoutconstraint/attribute.md)
  The part of the object’s visual representation that should be used to get the value for the constraint.
- [NSLayoutConstraint.FormatOptions](nslayoutconstraint/formatoptions.md)
  A bit mask that specifies both a part of an interface element to align and a direction for the alignment between two interface elements.
- [NSLayoutConstraint.Orientation](../AppKit/NSLayoutConstraint/Orientation.md)
  The layout constraint orientation, either horizontal or vertical, that the constraint uses to enforce layout between objects.
- [NSLayoutConstraint.Axis](nslayoutconstraint/axis.md)
  Keys that specify a horizontal or vertical layout constraint between objects.
- [struct NSEdgeInsets](../Foundation/NSEdgeInsets.md)
  A description of the distance between the edges of two rectangles.
- [var NSLAYOUTCONSTRAINT_H: Int32](nslayoutconstraint_h.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [Positioning content within layout margins](positioning-content-within-layout-margins.md)
  Position views so that they aren’t crowded by other content.
- [Positioning content relative to the safe area](positioning-content-relative-to-the-safe-area.md)
  Position views so that they aren’t obstructed by other content.
- [protocol UILayoutSupport](uilayoutsupport.md)
  A set of methods that provide layout support and access to layout anchors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nslayoutconstraint)*