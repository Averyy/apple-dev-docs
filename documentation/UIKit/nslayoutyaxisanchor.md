# NSLayoutYAxisAnchor

**Framework**: UIKit  
**Kind**: class

A factory class for creating vertical layout constraint objects using a fluent API.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class NSLayoutYAxisAnchor
```

#### Overview

[`NSLayoutYAxisAnchor`](nslayoutyaxisanchor.md) adds type information to the methods inherited from [`NSLayoutAnchor`](nslayoutanchor.md). Specifically, the generic methods declared by [`NSLayoutAnchor`](nslayoutanchor.md) must now take a matching [`NSLayoutYAxisAnchor`](nslayoutyaxisanchor.md) object.

For more information on using layout anchors, see [`NSLayoutAnchor`](nslayoutanchor.md).

## Topics

### Building system spacing constraints
- [func constraint(equalToSystemSpacingBelow: NSLayoutYAxisAnchor, multiplier: CGFloat) -> NSLayoutConstraint](nslayoutyaxisanchor/constraint(equaltosystemspacingbelow:multiplier:).md)
  Returns a constraint that defines the specific distance at which the current anchor is positioned below the specified anchor.
- [func constraint(greaterThanOrEqualToSystemSpacingBelow: NSLayoutYAxisAnchor, multiplier: CGFloat) -> NSLayoutConstraint](nslayoutyaxisanchor/constraint(greaterthanorequaltosystemspacingbelow:multiplier:).md)
  Returns a constraint that defines the minimum distance by which the current anchor is positioned below the specified anchor.
- [func constraint(lessThanOrEqualToSystemSpacingBelow: NSLayoutYAxisAnchor, multiplier: CGFloat) -> NSLayoutConstraint](nslayoutyaxisanchor/constraint(lessthanorequaltosystemspacingbelow:multiplier:).md)
  Returns a constraint that defines the maximum distance by which the current anchor is positioned below the specified anchor.
- [Creating self-sizing table view cells](creating-self-sizing-table-view-cells.md)
  Create table view cells that support Dynamic Type and use system spacing constraints to adjust the spacing surrounding text labels.
### Creating a layout dimension
- [func anchorWithOffset(to: NSLayoutYAxisAnchor) -> NSLayoutDimension](nslayoutyaxisanchor/anchorwithoffset(to:).md)
  Creates a layout dimension object from two anchors.

## Relationships

### Inherits From
- [NSLayoutAnchor](nslayoutanchor.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class NSLayoutConstraint](nslayoutconstraint.md)
  The relationship between two user interface objects that must be satisfied by the constraint-based layout system.
- [Auto Layout Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/AutolayoutPG/index.html?language=swift#//apple_ref/doc/uid/TP40010853)
- [class NSLayoutAnchor](nslayoutanchor.md)
  A factory class for creating layout constraint objects using a fluent API.
- [class NSLayoutXAxisAnchor](nslayoutxaxisanchor.md)
  A factory class for creating horizontal layout constraint objects using a fluent API.
- [var NSLAYOUTANCHOR_H: Int32](nslayoutanchor_h.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nslayoutyaxisanchor)*