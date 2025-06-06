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

- [init()](collisiongroup/init.md)
  Creates an empty option set.
- [init(rawValue: UInt32)](collisiongroup/init(rawvalue:).md)
  Creates a collision group from a raw value.
- [init(arrayLiteral: Self.Element...)](collisiongroup/init(arrayliteral:).md)
  Creates a set containing the elements of the given array literal.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/collisiongroup/init(_:))*