# shuffled(using:)

**Framework**: Swift  
**Kind**: method

Returns the elements of the sequence, shuffled using the given generator as a source for randomness.

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
func shuffled<T>(using generator: inout T) -> [Self.Element] where T : RandomNumberGenerator
```

#### Return Value

An array of this sequence’s elements in a shuffled order.

#### Discussion

You use this method to randomize the elements of a sequence when you are using a custom random number generator. For example, you can shuffle the numbers between `0` and `9` by calling the `shuffled(using:)` method on that range:

```swift
let numbers = 0...9
let shuffledNumbers = numbers.shuffled(using: &myGenerator)
// shuffledNumbers == [8, 9, 4, 3, 2, 6, 7, 0, 5, 1]
```

> **Note**: O(), where  is the length of the sequence.

> **Note**: The algorithm used to shuffle a sequence may change in a future version of Swift. If you’re passing a generator that results in the same shuffled order each time you run your program, that sequence may change when your program is compiled using a different version of Swift.

## Parameters

- `generator`: The random number generator to use when shuffling   the sequence.

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
- [func shuffled() -> [Self.Element]](array/shuffled.md)
  Returns the elements of the sequence, shuffled.
- [func partition(by: (Self.Element) throws -> Bool) rethrows -> Self.Index](array/partition(by:)-90po8.md)
  Reorders the elements of the collection such that all the elements that match the given predicate are after all the elements that don’t match.
- [func swapAt(Self.Index, Self.Index)](array/swapat(_:_:).md)
  Exchanges the values at the specified indices of the collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/array/shuffled(using:))*