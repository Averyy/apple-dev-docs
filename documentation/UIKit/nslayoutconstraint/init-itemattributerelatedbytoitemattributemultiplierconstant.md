# init(item:attribute:relatedBy:toItem:attribute:multiplier:constant:)

**Framework**: UIKit  
**Kind**: init

Creates a constraint that defines the relationship between the specified attributes of the given views.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
convenience init(item view1: Any, attribute attr1: NSLayoutConstraint.Attribute, relatedBy relation: NSLayoutConstraint.Relation, toItem view2: Any?, attribute attr2: NSLayoutConstraint.Attribute, multiplier: CGFloat, constant c: CGFloat)
```

#### Return Value

A constraint object relating the two provided views with the specified relation, attributes, multiplier, and constant.

#### Discussion

Constraints represent linear equations of the form `view1.attr1 <relation> multiplier × view2.attr2 + c`. If the constraint you wish to express does not have a second view and attribute, use `nil` and [`NSLayoutConstraint.Attribute.notAnAttribute`](nslayoutconstraint/attribute/notanattribute.md).

> **Note**:  This method throws an [`invalidArgumentException`](https://developer.apple.com/documentation/Foundation/NSExceptionName/invalidArgumentException) exception if it is used to create an invalid constraint (for example, `view1.top == 0.0 x nil.NotAnAttribute + 200.0` or `view1.top == 1.0 x view2.height + 20.0`). In general, you should use the layout anchor API to programmatically create constraints. This API includes additional type information that can catch many invalid constraints at build time. For more information, see Creating Constraints Using Layout Anchors in [`NSView`](https://developer.apple.com/documentation/AppKit/NSView) or [`UIView`](uiview.md).

## Parameters

- `view1`: The view for the left side of the constraint.
- `attr1`: The attribute of the view for the left side of the constraint.
- `relation`: The relationship between the left side of the constraint and the right side of the constraint.
- `view2`: The view for the right side of the constraint.
- `attr2`: The attribute of the view for the right side of the constraint.
- `multiplier`: The constant multiplied with the attribute on the right side of the constraint as part of getting the modified attribute.
- `c`: The constant added to the multiplied attribute value on the right side of the constraint to yield the final modified attribute.

## See Also

- [class func constraints(withVisualFormat: String, options: NSLayoutConstraint.FormatOptions, metrics: [String : Any]?, views: [String : Any]) -> [NSLayoutConstraint]](nslayoutconstraint/constraints(withvisualformat:options:metrics:views:).md)
  Creates constraints described by an ASCII art-like visual format string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nslayoutconstraint/init(item:attribute:relatedby:toitem:attribute:multiplier:constant:))*