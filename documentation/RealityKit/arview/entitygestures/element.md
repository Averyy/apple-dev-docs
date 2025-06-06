# ARView.EntityGestures.Element

**Framework**: RealityKit  
**Kind**: typealias

The element type of the option set.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 14.0+

## Declaration

```swift
typealias Element = ARView.EntityGestures
```

#### Discussion

To inherit all the default implementations from the `OptionSet` protocol, the `Element` type must be `Self`, the default.

## See Also

- [init()](arview/entitygestures/init.md)
  Creates an empty option set.
- [init<S>(S)](arview/entitygestures/init(_:).md)
  Creates a new set from a finite sequence of items.
- [init(arrayLiteral: Self.Element...)](arview/entitygestures/init(arrayliteral:).md)
  Creates a set containing the elements of the given array literal.
- [ARView.EntityGestures.ArrayLiteralElement](arview/entitygestures/arrayliteralelement.md)
  The type of the elements of an array literal.
- [init(rawValue: Int)](arview/entitygestures/init(rawvalue:).md)
  Creates a new option set from the given raw value.
- [let rawValue: Int](arview/entitygestures/rawvalue-swift.property.md)
  The corresponding value of the raw type.
- [ARView.EntityGestures.RawValue](arview/entitygestures/rawvalue-swift.typealias.md)
  The raw type that can be used to represent all values of the conforming type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/arview/entitygestures/element)*