# shuffled()

**Framework**: Swift  
**Kind**: method

Returns the elements of the sequence, shuffled.

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
func shuffled() -> [Self.Element]
```

#### Return Value

A shuffled array of this sequence’s elements.

#### Discussion

For example, you can shuffle the numbers between `0` and `9` by calling the `shuffled()` method on that range:

```swift
let numbers = 0...9
let shuffledNumbers = numbers.shuffled()
// shuffledNumbers == [1, 7, 6, 2, 8, 9, 4, 3, 5, 0]
```

This method is equivalent to calling `shuffled(using:)`, passing in the system’s default random generator.

> **Note**: O(), where  is the length of the sequence.

## See Also

- [func sort()](array/sort.md)
  Sorts the collection in place.
- [func sort(by: (Self.Element, Self.Element) throws -> Bool) rethrows](array/sort(by:).md)
  Sorts the collection in place, using the given predicate as the comparison between elements.
- [func sorted() -> [Self.Element]](array/sorted.md)
  Returns the elements of the sequence, sorted.
- [func sorted(by: (Self.Element, Self.Element) throws -> Bool) rethrows -> [Self.Element]](array/sorted(by:).md)
  Returns the elements of the sequence, sorted using the given predicate as the comparison between elements.
- [func reverse()](array/reverse.md)
  Reverses the elements of the collection in place.
- [func reversed() -> ReversedCollection<Self>](array/reversed.md)
  Returns a view presenting the elements of the collection in reverse order.
- [func shuffle()](array/shuffle.md)
  Shuffles the collection in place.
- [func shuffle<T>(using: inout T)](array/shuffle(using:).md)
  Shuffles the collection in place, using the given generator as a source for randomness.
- [func shuffled<T>(using: inout T) -> [Self.Element]](array/shuffled(using:).md)
  Returns the elements of the sequence, shuffled using the given generator as a source for randomness.
- [func partition(by: (Self.Element) throws -> Bool) rethrows -> Self.Index](array/partition(by:)-90po8.md)
  Reorders the elements of the collection such that all the elements that match the given predicate are after all the elements that don’t match.
- [func swapAt(Self.Index, Self.Index)](array/swapat(_:_:).md)
  Exchanges the values at the specified indices of the collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/array/shuffled())*