# init(attribute:relativeTo:attribute:offset:)

**Framework**: Core Animation  
**Kind**: init

Creates and returns an `CAConstraint` object with the specified parameters.

**Availability**:
- Mac Catalyst 13.1+
- macOS 10.5+

## Declaration

```swift
convenience init(attribute attr: CAConstraintAttribute, relativeTo srcId: String, attribute srcAttr: CAConstraintAttribute, offset c: CGFloat)
```

#### Return Value

A new `CAConstraint` object with the specified parameters. The scale of the constraint is set to 1.0.

#### Discussion

The value for the constraint is calculated as (`srcAttr` + `offset`).

## Parameters

- `attr`: The attribute of the layer for which to create a new constraint.
- `srcId`: The name of the layer that this constraint is calculated relative to.
- `srcAttr`: The attribute of   the constraint is calculated relative to.
- `c`: The offset added to the value of  .

## See Also

- [convenience init(attribute: CAConstraintAttribute, relativeTo: String, attribute: CAConstraintAttribute)](caconstraint/init(attribute:relativeto:attribute:).md)
  Creates and returns an `CAConstraint` object with the specified parameters.
- [init(attribute: CAConstraintAttribute, relativeTo: String, attribute: CAConstraintAttribute, scale: CGFloat, offset: CGFloat)](caconstraint/init(attribute:relativeto:attribute:scale:offset:).md)
  Returns an `CAConstraint` object with the specified parameters. Designated initializer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/caconstraint/init(attribute:relativeto:attribute:offset:))*