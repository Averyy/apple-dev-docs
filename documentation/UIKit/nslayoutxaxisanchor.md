# NSLayoutXAxisAnchor

**Framework**: UIKit  
**Kind**: class

A factory class for creating horizontal layout constraint objects using a fluent API.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class NSLayoutXAxisAnchor
```

#### Overview

[`NSLayoutXAxisAnchor`](nslayoutxaxisanchor.md) adds type information to the methods inherited from [`NSLayoutAnchor`](nslayoutanchor.md). Specifically, the generic methods declared by [`NSLayoutAnchor`](nslayoutanchor.md) must now take a matching [`NSLayoutXAxisAnchor`](nslayoutxaxisanchor.md) object.

**Swift**:

```swift
// This constraint is valid
cancelButton.leadingAnchor.constraintEqualToAnchor(saveButton.trailingAnchor, constant: 8.0).isActive = true
 
// This constraint generates an incompatible pointer type warning
cancelButton.leadingAnchor.constraintEqualToAnchor(saveButton.topAnchor, constant: 8.0).isActive = true
```

**Objective-C**:

```objc
// This constraint is valid
[self.cancelButton.leadingAnchor constraintEqualToAnchor:self.saveButton.trailingAnchor constant: 8.0].active = true;
 
// This constraint generates an incompatible pointer type warning
[self.cancelButton.leadingAnchor constraintEqualToAnchor:self.saveButton.topAnchor constant: 8.0].active = true;
```

For more information on using layout anchors, see [`NSLayoutAnchor`](nslayoutanchor.md).

## Topics

### Building system spacing constraints
- [func constraint(equalToSystemSpacingAfter: NSLayoutXAxisAnchor, multiplier: CGFloat) -> NSLayoutConstraint](nslayoutxaxisanchor/constraint(equaltosystemspacingafter:multiplier:).md)
  Returns a constraint that defines by how much the current anchor trails the specified anchor.
- [func constraint(greaterThanOrEqualToSystemSpacingAfter: NSLayoutXAxisAnchor, multiplier: CGFloat) -> NSLayoutConstraint](nslayoutxaxisanchor/constraint(greaterthanorequaltosystemspacingafter:multiplier:).md)
  Returns a constraint that defines the minimum amount by which the current anchor trails the specified anchor.
- [func constraint(lessThanOrEqualToSystemSpacingAfter: NSLayoutXAxisAnchor, multiplier: CGFloat) -> NSLayoutConstraint](nslayoutxaxisanchor/constraint(lessthanorequaltosystemspacingafter:multiplier:).md)
  Returns a constraint that defines the maximum amount by which the current anchor trails the specified anchor.
- [Creating self-sizing table view cells](creating-self-sizing-table-view-cells.md)
  Create table view cells that support Dynamic Type and use system spacing constraints to adjust the spacing surrounding text labels.
### Creating a layout dimension
- [func anchorWithOffset(to: NSLayoutXAxisAnchor) -> NSLayoutDimension](nslayoutxaxisanchor/anchorwithoffset(to:).md)
  Creates a layout dimension object from two anchors.

## Relationships

### Inherits From
- [NSLayoutAnchor](nslayoutanchor.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCoding](../foundation/nscoding.md)
- [NSCopying](../foundation/nscopying.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [class NSLayoutConstraint](nslayoutconstraint.md)
  The relationship between two user interface objects that must be satisfied by the constraint-based layout system.
- [Auto Layout Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/AutolayoutPG/index.html?language=swift#//apple_ref/doc/uid/TP40010853)
- [class NSLayoutAnchor](nslayoutanchor.md)
  A factory class for creating layout constraint objects using a fluent API.
- [class NSLayoutYAxisAnchor](nslayoutyaxisanchor.md)
  A factory class for creating vertical layout constraint objects using a fluent API.
- [var NSLAYOUTANCHOR_H: Int32](nslayoutanchor_h.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nslayoutxaxisanchor)*