# sourceAttribute

**Framework**: Core Animation  
**Kind**: property  
**Role**: Instance Property

The constraint attribute of the layer the receiver is calculated relative to

**Availability**:
- Mac Catalyst 13.1+
- macOS 10.5+

## Declaration

```swift
var sourceAttribute: CAConstraintAttribute { get }
```

```objc
@property (readonly) CAConstraintAttribute sourceAttribute;
```

## See Also

### Accessing Constraint Values
- [var attribute: CAConstraintAttribute](./attribute.md)
  The attribute the constraint affects.
- [var offset: CGFloat](./offset.md)
  Offset value of the constraint attribute.
- [var scale: CGFloat](./scale.md)
  Scale factor of the constraint attribute.
- [var sourceName: String](./sourcename.md)
  Name of the layer that the constraint is calculated relative to.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/caconstraint/sourceattribute)*