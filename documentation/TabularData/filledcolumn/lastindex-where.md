# lastIndex(where:)

**Framework**: TabularData  
**Kind**: method

Returns the index of the last element in the collection that matches the given predicate.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
func lastIndex(where predicate: (Self.Element) throws -> Bool) rethrows -> Self.Index?
```

#### Return Value

The index of the last element in the collection that matches `predicate`, or `nil` if no elements match.

#### Discussion

You can use the predicate to find an element of a type that doesn’t conform to the `Equatable` protocol or to find an element that matches particular criteria. This example finds the index of the last name that begins with the letter 

```None
let students = ["Kofi", "Abena", "Peter", "Kweku", "Akosua"]
if let i = students.lastIndex(where: { $0.hasPrefix("A") }) {
    print("\(students[i]) starts with 'A'!")
}
// Prints "Akosua starts with 'A'!"
```

> **Note**: O(), where  is the length of the collection.

## Parameters

- `predicate`: A closure that takes an element as its argument   and returns a Boolean value that indicates whether the passed element   represents a match.

## See Also

- [func lastIndex(of: Self.Element) -> Self.Index?](filledcolumn/lastindex(of:).md)
  Returns the last index where the specified value appears in the collection.
- [func distance(from: Self.Index, to: Self.Index) -> Int](filledcolumn/distance(from:to:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/filledcolumn/lastindex(where:))*