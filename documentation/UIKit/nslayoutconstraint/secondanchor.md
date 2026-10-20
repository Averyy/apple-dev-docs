# secondAnchor

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The second anchor that defines the constraint.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
@NSCopying
var secondAnchor: NSLayoutAnchor<AnyObject>? { get }
```

```objc
@property (copy, readonly, nullable) NSLayoutAnchor * secondAnchor;
```

## See Also

### Accessing constraint data
- [var firstItem: AnyObject?](./firstitem.md)
  The first object participating in the constraint.
- [var firstAttribute: NSLayoutConstraint.Attribute](./firstattribute.md)
  The attribute of the first object participating in the constraint.
- [var relation: NSLayoutConstraint.Relation](./relation-swift.property.md)
  The relation between the two attributes in the constraint.
- [var secondItem: AnyObject?](./seconditem.md)
  The second object participating in the constraint.
- [var secondAttribute: NSLayoutConstraint.Attribute](./secondattribute.md)
  The attribute of the second object participating in the constraint.
- [var multiplier: CGFloat](./multiplier.md)
  The multiplier applied to the second attribute participating in the constraint.
- [var constant: CGFloat](./constant.md)
  The constant added to the multiplied second attribute participating in the constraint.
- [var firstAnchor: NSLayoutAnchor<AnyObject>](./firstanchor.md)
  The first anchor that defines the constraint.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nslayoutconstraint/secondanchor)*