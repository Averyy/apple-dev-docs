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

- [init()](arview/renderoptions-swift.struct/init.md)
  Creates an empty option set.
- [init(arrayLiteral: Self.Element...)](arview/renderoptions-swift.struct/init(arrayliteral:).md)
  Creates a set containing the elements of the given array literal.
- [ARView.RenderOptions.Element](arview/renderoptions-swift.struct/element.md)
  The element type of the option set.
- [ARView.RenderOptions.ArrayLiteralElement](arview/renderoptions-swift.struct/arrayliteralelement.md)
  The type of the elements of an array literal.
- [init(rawValue: UInt)](arview/renderoptions-swift.struct/init(rawvalue:).md)
  Creates a new option set from the given raw value.
- [ARView.RenderOptions.RawValue](arview/renderoptions-swift.struct/rawvalue-swift.typealias.md)
  The raw type that can be used to represent all values of the conforming type.
- [let rawValue: UInt](arview/renderoptions-swift.struct/rawvalue-swift.property.md)
  The corresponding value of the raw type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/arview/renderoptions-swift.struct/init(_:))*