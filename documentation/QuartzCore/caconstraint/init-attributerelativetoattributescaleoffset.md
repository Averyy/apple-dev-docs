# init(attribute:relativeTo:attribute:scale:offset:)

**Framework**: Core Animation  
**Kind**: init

Returns an `CAConstraint` object with the specified parameters. Designated initializer.

**Availability**:
- Mac Catalyst 13.1+
- macOS 10.5+

## Declaration

```swift
init(attribute attr: CAConstraintAttribute, relativeTo srcId: String, attribute srcAttr: CAConstraintAttribute, scale m: CGFloat, offset c: CGFloat)
```

#### Return Value

An initialized constraint object using the specified parameters.

#### Discussion

The value for the constraint is calculated as (`srcAttr` * `scale`) + `offset`).

## Parameters

- `attr`: The attribute of the layer for which to create a new constraint.
- `srcId`: The name of the layer that this constraint is calculated relative to.
- `srcAttr`: The attribute of   the constraint is calculated relative to.
- `m`: The amount to scale the value of  .
- `c`: The offset added to the value of  .

## See Also

- [convenience init(attribute: CAConstraintAttribute, relativeTo: String, attribute: CAConstraintAttribute, offset: CGFloat)](caconstraint/init(attribute:relativeto:attribute:offset:).md)
  Creates and returns an `CAConstraint` object with the specified parameters.
- [convenience init(attribute: CAConstraintAttribute, relativeTo: String, attribute: CAConstraintAttribute)](caconstraint/init(attribute:relativeto:attribute:).md)
  Creates and returns an `CAConstraint` object with the specified parameters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/caconstraint/init(attribute:relativeto:attribute:scale:offset:))*