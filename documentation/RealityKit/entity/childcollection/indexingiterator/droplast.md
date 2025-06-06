# dropLast(_:)

**Framework**: RealityKit  
**Kind**: method

Returns a sequence containing all but the given number of final elements.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- visionOS ?+

## Declaration

```swift
func dropLast(_ k: Int = 1) -> [Self.Element]
```

#### Return Value

A sequence leaving off the specified number of elements.

#### Discussion

The sequence must be finite. If the number of elements to drop exceeds the number of elements in the sequence, the result is an empty sequence.

```None
let numbers = [1, 2, 3, 4, 5]
print(numbers.dropLast(2))
// Prints "[1, 2, 3]"
print(numbers.dropLast(10))
// Prints "[]"
```

> **Note**: O(), where  is the length of the sequence.

O(), where  is the length of the sequence.

## Parameters

- `n`: The number of elements to drop off the end of the   sequence.   must be greater than or equal to zero.

## See Also

- [func dropFirst(Int) -> DropFirstSequence<Self>](entity/childcollection/indexingiterator/dropfirst(_:).md)
  Returns a sequence containing all but the given number of initial elements.
- [func drop(while: (Self.Element) throws -> Bool) rethrows -> DropWhileSequence<Self>](entity/childcollection/indexingiterator/drop(while:).md)
  Returns a sequence by skipping the initial, consecutive elements that satisfy the given predicate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/entity/childcollection/indexingiterator/droplast(_:))*