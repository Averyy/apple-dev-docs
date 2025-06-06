# constraint(equalTo:multiplier:)

**Framework**: UIKit  
**Kind**: method

Returns a constraint that defines the anchor’s size attribute as equal to the specified anchor multiplied by the constant.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func constraint(equalTo anchor: NSLayoutDimension, multiplier m: CGFloat) -> NSLayoutConstraint
```

#### Return Value

An [`NSLayoutConstraint`](nslayoutconstraint.md) object that defines the attribute represented by this layout anchor as equal to the attribute represented by the `anchor` parameter multiplied by the `m` constant.

#### Discussion

This method defines the relationship `first attribute = m * second attribute`. Where `first attribute` is the layout attribute represented by the anchor receiving this method call, and `second attribute` is the layout attribute represented by the `anchor` parameter.

The constraints produced by the following two examples are identical.

## Parameters

- `anchor`: A dimension anchor from a  ,  , or   object.
- `m`: The multiplier constant for the constraint.

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nslayoutdimension/constraint(equalto:multiplier:))*