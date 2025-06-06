# constraint(equalToConstant:)

**Framework**: UIKit  
**Kind**: method

Returns a constraint that defines a constant size for the anchor’s size attribute.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func constraint(equalToConstant c: CGFloat) -> NSLayoutConstraint
```

#### Return Value

An [`NSLayoutConstraint`](nslayoutconstraint.md) object that defines a constant size for the attribute associated with this dimension anchor.

#### Discussion

This method defines the relationship `first attribute = c`. Where `first attribute` is the layout attribute represented by the anchor receiving this method call.

The constraints produced by the following two examples are identical.

## Parameters

- `c`: A constant representing the size of the attribute associated with this dimension anchor.

## See Also

- [func constraint(equalTo: NSLayoutDimension, multiplier: CGFloat) -> NSLayoutConstraint](nslayoutdimension/constraint(equalto:multiplier:).md)
  Returns a constraint that defines the anchor’s size attribute as equal to the specified anchor multiplied by the constant.
- [func constraint(equalTo: NSLayoutDimension, multiplier: CGFloat, constant: CGFloat) -> NSLayoutConstraint](nslayoutdimension/constraint(equalto:multiplier:constant:).md)
  Returns a constraint that defines the anchor’s size attribute as equal to the specified size attribute multiplied by a constant plus an offset.
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

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nslayoutdimension/constraint(equaltoconstant:))*