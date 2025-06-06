# sort()

**Framework**: Swift  
**Kind**: method

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

> **Note**: O( log ), where  is the length of the collection.

O( log ), where  is the length of the collection.

## See Also

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
- [func shuffled<T>(using: inout T) -> [Self.Element]](array/shuffled(using:).md)
  Returns the elements of the sequence, shuffled using the given generator as a source for randomness.
- [func partition(by: (Self.Element) throws -> Bool) rethrows -> Self.Index](array/partition(by:)-90po8.md)
  Reorders the elements of the collection such that all the elements that match the given predicate are after all the elements that don’t match.
- [func swapAt(Self.Index, Self.Index)](array/swapat(_:_:).md)
  Exchanges the values at the specified indices of the collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/array/sort())*