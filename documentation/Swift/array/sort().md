# sort()

**Framework**: Swift  
**Kind**: method  
**Role**: Instance Method

Sorts the collection in place.

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
mutating func sort()
```

Available when `Self` conforms to `RandomAccessCollection` and `Element` conforms to `Comparable`.

#### Discussion

You can sort any mutable collection of elements that conform to the `Comparable` protocol by calling this method. Elements are sorted in ascending order.

Here’s an example of sorting a list of students’ names. Strings in Swift conform to the `Comparable` protocol, so the names are sorted in ascending order according to the less-than operator (`<`).

```swift
var students = ["Kofi", "Abena", "Peter", "Kweku", "Akosua"]
students.sort()
print(students)
// Prints "["Abena", "Akosua", "Kofi", "Kweku", "Peter"]"
```

To sort the elements of your collection in descending order, pass the greater-than operator (`>`) to the `sort(by:)` method.

```swift
students.sort(by: >)
print(students)
// Prints "["Peter", "Kweku", "Kofi", "Akosua", "Abena"]"
```

The sorting algorithm is guaranteed to be stable. A stable sort preserves the relative order of elements that compare as equal.

> **Complexity**: O(*n* log *n*), where *n* is the length of the collection.

## See Also

### Reordering an Array’s Elements
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
- [func shuffle<T>(using: inout T)](./shuffle%28using%29.md)
  Shuffles the collection in place, using the given generator as a source for randomness.
- [func shuffled() -> [Self.Element]](./shuffled%28%29.md)
  Returns the elements of the sequence, shuffled.
- [func shuffled<T>(using: inout T) -> [Self.Element]](./shuffled%28using%29.md)
  Returns the elements of the sequence, shuffled using the given generator as a source for randomness.
- [func partition(by: (Self.Element) throws -> Bool) rethrows -> Self.Index](./partition%28by%29-90po8.md)
  Reorders the elements of the collection such that all the elements that match the given predicate are after all the elements that don’t match.
- [func swapAt(Self.Index, Self.Index)](./swapat%28_,_%29.md)
  Exchanges the values at the specified indices of the collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/array/sort())*