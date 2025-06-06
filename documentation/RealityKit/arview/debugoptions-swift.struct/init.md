# init(_:)

**Framework**: RealityKit  
**Kind**: init

Creates a new set from a finite sequence of items.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+

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

- [init()](arview/debugoptions-swift.struct/init.md)
  Creates an empty option set.
- [init(arrayLiteral: Self.Element...)](arview/debugoptions-swift.struct/init(arrayliteral:).md)
  Creates a set containing the elements of the given array literal.
- [ARView.DebugOptions.Element](arview/debugoptions-swift.struct/element.md)
  The element type of the option set.
- [ARView.DebugOptions.ArrayLiteralElement](arview/debugoptions-swift.struct/arrayliteralelement.md)
  The type of the elements of an array literal.
- [init(rawValue: Int)](arview/debugoptions-swift.struct/init(rawvalue:).md)
  Create a debug options enumeration from a raw value.
- [let rawValue: Int](arview/debugoptions-swift.struct/rawvalue-swift.property.md)
  Options for drawing overlay content in a scene that aids in debugging the scene.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/arview/debugoptions-swift.struct/init(_:))*