# init(_:)

**Framework**: Swift  
**Kind**: init  
**Role**: Initializer

Creates a new set from a finite sequence of items.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
init<S>(_ sequence: S) where S : Sequence, Self.Element == S.Element
```

#### Discussion

Use this initializer to create a new set from an existing sequence, like an array or a range:

```swift
let validIndices = Set(0..<7).subtracting([2, 4, 5])
print(validIndices)
// Prints "[6, 0, 1, 3]"
```

## Parameters

- `sequence`: The elements to use as members of the new set.

## See Also

### Creating a Set
- [init()](./init%28%29.md)
  Creates an empty set.
- [init(minimumCapacity: Int)](./init%28minimumcapacity%29.md)
  Creates an empty set with preallocated space for at least the specified number of elements.
- [init<Source>(Source)](./init%28_%29.md)
  Creates a new set from a finite sequence of items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/set/init(_:)-9cgks)*