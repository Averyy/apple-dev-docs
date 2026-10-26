# constraintWithAttribute:relativeTo:attribute:scale:offset:

**Framework**: Core Animation  
**Kind**: method  
**Role**: Type Method

Creates and returns an `CAConstraint` object with the specified parameters.

**Availability**:
- Mac Catalyst 13.1+
- macOS 10.5+

## Declaration

```objc
+ (instancetype) constraintWithAttribute:(CAConstraintAttribute) attr relativeTo:(NSString *) srcId attribute:(CAConstraintAttribute) srcAttr scale:(CGFloat) m offset:(CGFloat) c;
```

#### Return Value

A new `CAConstraint` object with the specified parameters.

#### Discussion

The value for the constraint is calculated as ((`srcAttr` * scale) + offset).

## Parameters

- `attr`: The attribute of the layer for which to create a new constraint.
- `srcId`: The name of the layer that this constraint is calculated relative to.
- `srcAttr`: The attribute of `srcLayer` the constraint is calculated relative to.
- `m`: The amount to scale the value of `srcAttr`.
- `c`: The offset from the `srcAttr`.

## See Also

### Related Documentation
- [Core Animation Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CoreAnimation_guide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40004514)
### Create a New Constraint
- [convenience init(attribute: CAConstraintAttribute, relativeTo: String, attribute: CAConstraintAttribute, offset: CGFloat)](./init%28attribute,relativeto,attribute,offset%29.md)
  Creates and returns an `CAConstraint` object with the specified parameters.
- [convenience init(attribute: CAConstraintAttribute, relativeTo: String, attribute: CAConstraintAttribute)](./init%28attribute,relativeto,attribute%29.md)
  Creates and returns an `CAConstraint` object with the specified parameters.
- [init(attribute: CAConstraintAttribute, relativeTo: String, attribute: CAConstraintAttribute, scale: CGFloat, offset: CGFloat)](./init%28attribute,relativeto,attribute,scale,offset%29.md)
  Returns an `CAConstraint` object with the specified parameters. Designated initializer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/caconstraint/constraintwithattribute:relativeto:attribute:scale:offset:)*