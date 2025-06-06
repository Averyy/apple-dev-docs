# prefix(through:)

**Framework**: RealityKit  
**Kind**: method

Returns a subsequence from the start of the collection through the specified position.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- visionOS ?+

## Declaration

```swift
func prefix(through position: Self.Index) -> Self.SubSequence
```

#### Return Value

A subsequence up to, and including, the given position.

#### Discussion

The resulting subsequence  the element at the position specified by the `through` parameter. The following example searches for the index of the number `40` in an array of integers, and then prints the prefix of the array up to, and including, that index:

```None
let numbers = [10, 20, 30, 40, 50, 60]
if let i = numbers.firstIndex(of: 40) {
    print(numbers.prefix(through: i))
}
// Prints "[10, 20, 30, 40]"
```

Using the `prefix(through:)` method is equivalent to using a partial closed range as the collection’s subscript. The subscript notation is preferred over `prefix(through:)`.

```None
if let i = numbers.firstIndex(of: 40) {
    print(numbers[...i])
}
// Prints "[10, 20, 30, 40]"
```

> **Note**: O(1)

O(1)

## Parameters

- `position`: The index of the last element to include in the   resulting subsequence.   must be a valid index of the collection   that is not equal to the   property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/entity/componentset/prefix(through:))*