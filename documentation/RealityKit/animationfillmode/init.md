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

- [init()](animationfillmode/init.md)
  Creates an empty option set.
- [init(arrayLiteral: Self.Element...)](animationfillmode/init(arrayliteral:).md)
  Creates a set containing the elements of the given array literal.
- [init(rawValue: Int8)](animationfillmode/init(rawvalue:).md)
  Creates a fill mode from its backing data type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/animationfillmode/init(_:))*