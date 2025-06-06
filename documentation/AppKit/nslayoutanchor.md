# NSLayoutAnchor

**Framework**: Appkit  
**Kind**: class

A factory class for creating layout constraint objects using a fluent API.

**Availability**:
- macOS 10.11+

## Declaration

```swift
class NSLayoutAnchor<AnchorType> where AnchorType : AnyObject
```

#### Overview

Use these constraints to programatically define your layout using Auto Layout. Instead of creating [`NSLayoutConstraint`](nslayoutconstraint.md) objects directly, start with an [`NSView`](nsview.md) or [`NSLayoutGuide`](nslayoutguide.md) object you wish to constrain, and select one of that object’s anchor properties. These properties correspond to the main [`NSLayoutConstraint.Attribute`](nslayoutconstraint/attribute.md) values used in Auto Layout, and provide an appropriate [`NSLayoutAnchor`](nslayoutanchor.md) subclass for creating constraints to that attribute. Use the anchor’s methods to construct your constraint.

As you can see from these examples, the [`NSLayoutAnchor`](nslayoutanchor.md) class provides several advantages over using the [`NSLayoutConstraint`](nslayoutconstraint.md) API directly.

- The code is cleaner, more concise, and easier to read.
- The [`NSLayoutConstraint.Attribute`](nslayoutconstraint/attribute.md) subclasses provide additional type checking, preventing you from creating invalid constraints.

> **Note**:  While the [`NSLayoutAnchor`](nslayoutanchor.md) class provides additional type checking, it is still possible to create invalid constraints. For example, the compiler allows you to constrain one view’s [`leadingAnchor`](nsview/leadinganchor.md) with another view’s [`leftAnchor`](nsview/leftanchor.md), since they are both [`NSLayoutXAxisAnchor`](nslayoutxaxisanchor.md) instances. However, Auto Layout does not allow constraints that mix leading and trailing attributes with left or right attributes. As a result, this constraint crashes at runtime.

For more information on the anchor properties, see [`bottomAnchor`](nsview/bottomanchor.md) in the [`NSView`](nsview.md) or [`NSLayoutGuide`](nslayoutguide.md).

> **Note**:  You never use the [`NSLayoutAnchor`](nslayoutanchor.md) class directly. Instead, use one of its subclasses, based on the type of constraint you wish to create. - Use [`NSLayoutXAxisAnchor`](nslayoutxaxisanchor.md) to create horizontal constraints.
- Use [`NSLayoutYAxisAnchor`](nslayoutyaxisanchor.md) to create vertical constraints.
- Use [`NSLayoutDimension`](nslayoutdimension.md) to create constraints that affect the view’s height or width. However, since you access [`NSLayoutAnchor`](nslayoutanchor.md) objects using the anchor properties of an [`NSView`](nsview.md) or [`NSLayoutGuide`](nslayoutguide.md), a correct subclass is automatically provided.

## Topics

### Building constraints
- [func constraint(equalTo: NSLayoutAnchor<AnchorType>) -> NSLayoutConstraint](nslayoutanchor/constraint(equalto:).md)
  Returns a constraint that defines one item’s attribute as equal to another.
- [func constraint(equalTo: NSLayoutAnchor<AnchorType>, constant: CGFloat) -> NSLayoutConstraint](nslayoutanchor/constraint(equalto:constant:).md)
  Returns a constraint that defines one item’s attribute as equal to another item’s attribute plus a constant offset.
- [func constraint(greaterThanOrEqualTo: NSLayoutAnchor<AnchorType>) -> NSLayoutConstraint](nslayoutanchor/constraint(greaterthanorequalto:).md)
  Returns a constraint that defines one item’s attribute as greater than or equal to another.
- [func constraint(greaterThanOrEqualTo: NSLayoutAnchor<AnchorType>, constant: CGFloat) -> NSLayoutConstraint](nslayoutanchor/constraint(greaterthanorequalto:constant:).md)
  Returns a constraint that defines one item’s attribute as greater than or equal to another item’s attribute plus a constant offset.
- [func constraint(lessThanOrEqualTo: NSLayoutAnchor<AnchorType>) -> NSLayoutConstraint](nslayoutanchor/constraint(lessthanorequalto:).md)
  Returns a constraint that defines one item’s attribute as less than or equal to another.
- [func constraint(lessThanOrEqualTo: NSLayoutAnchor<AnchorType>, constant: CGFloat) -> NSLayoutConstraint](nslayoutanchor/constraint(lessthanorequalto:constant:).md)
  Returns a constraint that defines one item’s attribute as less than or equal to another item’s attribute plus a constant offset.
### Debugging the anchor
- [var constraintsAffectingLayout: [NSLayoutConstraint]](nslayoutanchor/constraintsaffectinglayout.md)
  The constraints that impact the layout of the anchor.
- [var hasAmbiguousLayout: Bool](nslayoutanchor/hasambiguouslayout.md)
  A Boolean value indicating whether the constraints impacting the anchor specify its location ambiguously.
- [var name: String](nslayoutanchor/name.md)
  The name assigned to the anchor for debugging purposes.
- [var item: AnyObject?](nslayoutanchor/item.md)
  The layout item used to calculate the anchor’s position.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [NSLayoutDimension](nslayoutdimension.md)
- [NSLayoutXAxisAnchor](nslayoutxaxisanchor.md)
- [NSLayoutYAxisAnchor](nslayoutyaxisanchor.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class NSLayoutXAxisAnchor](nslayoutxaxisanchor.md)
  A factory class for creating horizontal layout constraint objects using a fluent API.
- [class NSLayoutYAxisAnchor](nslayoutyaxisanchor.md)
  A factory class for creating vertical layout constraint objects using a fluent API.


---

*[View on Apple Developer](https://developer.apple.com/documentation/AppKit/nslayoutanchor)*