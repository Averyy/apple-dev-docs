# dropFirst(_:)

**Framework**: Swift  
**Kind**: method

Returns a sequence containing all but the given number of initial elements.

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
func dropFirst(_ k: Int = 1) -> DropFirstSequence<Self>
```

#### Return Value

A sequence starting after the specified number of elements.

#### Discussion

If the number of elements to drop exceeds the number of elements in the sequence, the result is an empty sequence.

```swift
let numbers = [1, 2, 3, 4, 5]
print(numbers.dropFirst(2))
// Prints "[3, 4, 5]"
print(numbers.dropFirst(10))
// Prints "[]"
```

> **Note**: O(1), with O() deferred to each iteration of the result, where  is the number of elements to drop from the beginning of the sequence.

O(1), with O() deferred to each iteration of the result, where  is the number of elements to drop from the beginning of the sequence.

## Parameters

- `k`: The number of elements to drop from the beginning of   the sequence.   must be greater than or equal to zero.

## See Also

- [func dropLast(Int) -> [Self.Element]](sequence/droplast(_:).md)
  Returns a sequence containing all but the given number of final elements.
- [func drop(while: (Self.Element) throws -> Bool) rethrows -> DropWhileSequence<Self>](sequence/drop(while:).md)
  Returns a sequence by skipping the initial, consecutive elements that satisfy the given predicate.
- [func filter((Self.Element) throws -> Bool) rethrows -> [Self.Element]](sequence/filter(_:)-5y9d2.md)
  Returns an array containing, in order, the elements of the sequence that satisfy the given predicate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/sequence/dropfirst(_:))*