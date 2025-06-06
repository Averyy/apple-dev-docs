# dropLast(_:)

**Framework**: Swift  
**Kind**: method

Returns a sequence containing all but the given number of final elements.

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
func dropLast(_ k: Int = 1) -> [Self.Element]
```

#### Return Value

A sequence leaving off the specified number of elements.

#### Discussion

The sequence must be finite. If the number of elements to drop exceeds the number of elements in the sequence, the result is an empty sequence.

```swift
let numbers = [1, 2, 3, 4, 5]
print(numbers.dropLast(2))
// Prints "[1, 2, 3]"
print(numbers.dropLast(10))
// Prints "[]"
```

> **Note**: O(), where  is the length of the sequence.

O(), where  is the length of the sequence.

## See Also

- [func dropFirst(Int) -> DropFirstSequence<Self>](sequence/dropfirst(_:).md)
  Returns a sequence containing all but the given number of initial elements.
- [func drop(while: (Self.Element) throws -> Bool) rethrows -> DropWhileSequence<Self>](sequence/drop(while:).md)
  Returns a sequence by skipping the initial, consecutive elements that satisfy the given predicate.
- [func filter((Self.Element) throws -> Bool) rethrows -> [Self.Element]](sequence/filter(_:)-5y9d2.md)
  Returns an array containing, in order, the elements of the sequence that satisfy the given predicate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/sequence/droplast(_:))*