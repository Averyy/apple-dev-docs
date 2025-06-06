# reverse()

**Framework**: Tabulardata  
**Kind**: method

Reverses the elements of the collection in place.

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
mutating func reverse()
```

#### Discussion

The following example reverses the elements of an array of characters:

```None
var characters: [Character] = ["C", "a", "f", "é"]
characters.reverse()
print(characters)
// Prints "["é", "f", "a", "C"]"
```

> **Note**: O(), where  is the number of elements in the collection.

## See Also

- [func dropLast(Int) -> Self.SubSequence](anycolumn/droplast(_:).md)
  Returns a subsequence containing all but the specified number of final elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/anycolumn/reverse())*