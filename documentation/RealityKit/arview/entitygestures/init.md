# init(_:)

**Framework**: RealityKit  
**Kind**: init

Creates a new set from a finite sequence of items.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+

## Declaration

```swift
init<S>(_ sequence: S) where S : Sequence, Self.Element == S.Element
```

#### Discussion

Use this initializer to create a new set from an existing sequence, like an array or a range:

```None
let validIndices = Set(0..<7).subtracting([2, 4, 5])
print(validIndices)
// Prints "[6, 0, 1, 3]"
```

## Parameters

- `sequence`: The elements to use as members of the new set.

## See Also

- [init()](arview/entitygestures/init.md)
  Creates an empty option set.
- [init(arrayLiteral: Self.Element...)](arview/entitygestures/init(arrayliteral:).md)
  Creates a set containing the elements of the given array literal.
- [ARView.EntityGestures.Element](arview/entitygestures/element.md)
  The element type of the option set.
- [ARView.EntityGestures.ArrayLiteralElement](arview/entitygestures/arrayliteralelement.md)
  The type of the elements of an array literal.
- [init(rawValue: Int)](arview/entitygestures/init(rawvalue:).md)
  Creates a new option set from the given raw value.
- [let rawValue: Int](arview/entitygestures/rawvalue-swift.property.md)
  The corresponding value of the raw type.
- [ARView.EntityGestures.RawValue](arview/entitygestures/rawvalue-swift.typealias.md)
  The raw type that can be used to represent all values of the conforming type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/arview/entitygestures/init(_:))*