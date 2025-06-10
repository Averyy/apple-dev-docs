# NSLayoutDimension

**Framework**: UIKit  
**Kind**: class

A factory class for creating size-based layout constraint objects using a fluent API.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class NSLayoutDimension
```

#### Overview

Use these constraints to programmatically define your layout using Auto Layout. All sizes are measured in points. In addition to providing size-specific methods for creating constraints, this class adds type information to the methods inherited from [`NSLayoutAnchor`](nslayoutanchor.md). Specifically, the generic methods declared by [`NSLayoutAnchor`](nslayoutanchor.md) must now take a matching [`NSLayoutDimension`](nslayoutdimension.md) object.

For more information on using layout anchors, see [`NSLayoutAnchor`](nslayoutanchor.md).

## Topics

### Building constraints
- [func constraint(equalTo: NSLayoutDimension, multiplier: CGFloat) -> NSLayoutConstraint](nslayoutdimension/constraint(equalto:multiplier:).md)
  Returns a constraint that defines the anchor’s size attribute as equal to the specified anchor multiplied by the constant.
- [func constraint(equalTo: NSLayoutDimension, multiplier: CGFloat, constant: CGFloat) -> NSLayoutConstraint](nslayoutdimension/constraint(equalto:multiplier:constant:).md)
  Returns a constraint that defines the anchor’s size attribute as equal to the specified size attribute multiplied by a constant plus an offset.
- [func constraint(equalToConstant: CGFloat) -> NSLayoutConstraint](nslayoutdimension/constraint(equaltoconstant:).md)
  Returns a constraint that defines a constant size for the anchor’s size attribute.
- [func constraint(greaterThanOrEqualTo: NSLayoutDimension, multiplier: CGFloat) -> NSLayoutConstraint](nslayoutdimension/constraint(greaterthanorequalto:multiplier:).md)
  Returns a constraint that defines the anchor’s size attribute as greater than or equal to the specified anchor multiplied by the constant.
- [func constraint(greaterThanOrEqualTo: NSLayoutDimension, multiplier: CGFloat, constant: CGFloat) -> NSLayoutConstraint](nslayoutdimension/constraint(greaterthanorequalto:multiplier:constant:).md)
  Returns a constraint that defines the anchor’s size attribute as greater than or equal to the specified anchor multiplied by the constant plus an offset.
- [func constraint(greaterThanOrEqualToConstant: CGFloat) -> NSLayoutConstraint](nslayoutdimension/constraint(greaterthanorequaltoconstant:).md)
  Returns a constraint that defines the minimum size for the anchor’s size attribute.
- [func constraint(lessThanOrEqualTo: NSLayoutDimension, multiplier: CGFloat) -> NSLayoutConstraint](nslayoutdimension/constraint(lessthanorequalto:multiplier:).md)
  Returns a constraint that defines the anchor’s size attribute as less than or equal to the specified anchor multiplied by the constant.
- [func constraint(lessThanOrEqualTo: NSLayoutDimension, multiplier: CGFloat, constant: CGFloat) -> NSLayoutConstraint](nslayoutdimension/constraint(lessthanorequalto:multiplier:constant:).md)
  Returns a constraint that defines the anchor’s size attribute as greater than or equal to the specified anchor multiplied by the constant plus an offset.
- [func constraint(lessThanOrEqualToConstant: CGFloat) -> NSLayoutConstraint](nslayoutdimension/constraint(lessthanorequaltoconstant:).md)
  Returns a constraint that defines the maximum size for the anchor’s size attribute.

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

- [class UILayoutGuide](uilayoutguide.md)
  A rectangular area that can interact with Auto Layout.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nslayoutdimension)*