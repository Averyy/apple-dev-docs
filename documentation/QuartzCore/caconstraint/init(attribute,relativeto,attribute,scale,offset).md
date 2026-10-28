# init(attribute:relativeTo:attribute:scale:offset:)

**Framework**: Core Animation  
**Kind**: init  
**Role**: Initializer

Returns an `CAConstraint` object with the specified parameters. Designated initializer.

**Availability**:
- Mac Catalyst 13.1+
- macOS 10.5+

## Declaration

```swift
init(attribute attr: CAConstraintAttribute, relativeTo srcId: String, attribute srcAttr: CAConstraintAttribute, scale m: CGFloat, offset c: CGFloat)
```

```objc
- (instancetype) initWithAttribute:(CAConstraintAttribute) attr relativeTo:(NSString *) srcId attribute:(CAConstraintAttribute) srcAttr scale:(CGFloat) m offset:(CGFloat) c;
```

## Return Value

An initialized constraint object using the specified parameters.

## Discussion

The value for the constraint is calculated as (`srcAttr` * `scale`) + `offset`).

## Parameters

- `attr`: The attribute of the layer for which to create a new constraint.
- `srcId`: The name of the layer that this constraint is calculated relative to.
- `srcAttr`: The attribute of `srcLayer` the constraint is calculated relative to.
- `m`: The amount to scale the value of `srcAttr`.
- `c`: The offset added to the value of `srcAttr`.

## See Also

### Create a New Constraint
- [convenience init(attribute: CAConstraintAttribute, relativeTo: String, attribute: CAConstraintAttribute, offset: CGFloat)](./init%28attribute,relativeto,attribute,offset%29.md)
  Creates and returns an `CAConstraint` object with the specified parameters.
- [convenience init(attribute: CAConstraintAttribute, relativeTo: String, attribute: CAConstraintAttribute)](./init%28attribute,relativeto,attribute%29.md)
  Creates and returns an `CAConstraint` object with the specified parameters.
- [+ constraintWithAttribute:relativeTo:attribute:scale:offset:](./constraintwithattribute_relativeto_attribute_scale_offset_.md)
  Creates and returns an `CAConstraint` object with the specified parameters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/caconstraint/init(attribute:relativeto:attribute:scale:offset:))*