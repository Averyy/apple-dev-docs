# constant

**Framework**: AppKit  
**Kind**: property

The constant added to the multiplied second attribute participating in the constraint.

**Availability**:
- macOS 10.7+

## Declaration

```swift
var constant: CGFloat { get set }
```

#### Discussion

Unlike the other properties, the constant can be modified after constraint creation. Setting the constant on an existing constraint performs much better than removing the constraint and adding a new one that’s exactly like the old except that it has a different constant.

## See Also

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
- [var firstAnchor: NSLayoutAnchor<AnyObject>](nslayoutconstraint/firstanchor.md)
  The first anchor that defines the constraint.
- [var secondAnchor: NSLayoutAnchor<AnyObject>?](nslayoutconstraint/secondanchor.md)
  The second anchor that defines the constraint.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nslayoutconstraint/constant)*