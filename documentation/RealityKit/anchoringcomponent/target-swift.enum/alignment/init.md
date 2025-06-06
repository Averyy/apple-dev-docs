# init(_:)

**Framework**: RealityKit  
**Kind**: init

Creates a new set from a finite sequence of items.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- visionOS ?+

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

- [init()](anchoringcomponent/target-swift.enum/alignment/init.md)
  Creates an empty option set.
- [init(arrayLiteral: Self.Element...)](anchoringcomponent/target-swift.enum/alignment/init(arrayliteral:).md)
  Creates a set containing the elements of the given array literal.
- [init(rawValue: UInt8)](anchoringcomponent/target-swift.enum/alignment/init(rawvalue:).md)
  Creates a new option set from the given raw value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/anchoringcomponent/target-swift.enum/alignment/init(_:))*