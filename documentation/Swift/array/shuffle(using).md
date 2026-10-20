# shuffle(using:)

**Framework**: Swift  
**Kind**: method  
**Role**: Instance Method

Shuffles the collection in place, using the given generator as a source for randomness.

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
mutating func shuffle<T>(using generator: inout T) where T : RandomNumberGenerator
```

Available when `Self` conforms to `RandomAccessCollection`.

#### Discussion

You use this method to randomize the elements of a collection when you are using a custom random number generator. For example, you can use the `shuffle(using:)` method to randomly reorder the elements of an array.

```swift
var names = ["Alejandro", "Camila", "Diego", "Luciana", "Luis", "Sofía"]
names.shuffle(using: &myGenerator)
// names == ["Sofía", "Alejandro", "Camila", "Luis", "Diego", "Luciana"]
```

> **Complexity**: O(*n*), where *n* is the length of the collection.

> **Note**: The algorithm used to shuffle a collection may change in a future version of Swift. If you’re passing a generator that results in the same shuffled order each time you run your program, that sequence may change when your program is compiled using a different version of Swift.

## Parameters

- `generator`: The random number generator to use when shuffling the collection.

## See Also

### Reordering an Array’s Elements
- [func sort()](./sort%28%29.md)
  Sorts the collection in place.
- [func sort(by: (Self.Element, Self.Element) throws -> Bool) rethrows](./sort%28by%29.md)
  Sorts the collection in place, using the given predicate as the comparison between elements.
- [func sorted() -> [Self.Element]](./sorted%28%29.md)
  Returns the elements of the sequence, sorted.
- [func sorted(by: (Self.Element, Self.Element) throws -> Bool) rethrows -> [Self.Element]](./sorted%28by%29.md)
  Returns the elements of the sequence, sorted using the given predicate as the comparison between elements.
- [func reverse()](./reverse%28%29.md)
  Reverses the elements of the collection in place.
- [func reversed() -> ReversedCollection<Self>](./reversed%28%29.md)
  Returns a view presenting the elements of the collection in reverse order.
- [func shuffle()](./shuffle%28%29.md)
  Shuffles the collection in place.
- [func shuffled() -> [Self.Element]](./shuffled%28%29.md)
  Returns the elements of the sequence, shuffled.
- [func shuffled<T>(using: inout T) -> [Self.Element]](./shuffled%28using%29.md)
  Returns the elements of the sequence, shuffled using the given generator as a source for randomness.
- [func partition(by: (Self.Element) throws -> Bool) rethrows -> Self.Index](./partition%28by%29-90po8.md)
  Reorders the elements of the collection such that all the elements that match the given predicate are after all the elements that don’t match.
- [func swapAt(Self.Index, Self.Index)](./swapat%28_,_%29.md)
  Exchanges the values at the specified indices of the collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/array/shuffle(using:))*