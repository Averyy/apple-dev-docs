# lastIndex(where:)

**Framework**: Swift  
**Kind**: method

Returns the index of the last element in the collection that matches the given predicate.

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
func lastIndex(where predicate: (Self.Element) throws -> Bool) rethrows -> Self.Index?
```

#### Return Value

The index of the last element in the collection that matches `predicate`, or `nil` if no elements match.

#### Discussion

You can use the predicate to find an element of a type that doesn’t conform to the `Equatable` protocol or to find an element that matches particular criteria. This example finds the index of the last name that begins with the letter 

```swift
let students = ["Kofi", "Abena", "Peter", "Kweku", "Akosua"]
if let i = students.lastIndex(where: { $0.hasPrefix("A") }) {
    print("\(students[i]) starts with 'A'!")
}
// Prints "Akosua starts with 'A'!"
```

> **Note**: O(), where  is the length of the collection.

O(), where  is the length of the collection.

## Parameters

- `predicate`: A closure that takes an element as its argument   and returns a Boolean value that indicates whether the passed element   represents a match.

## See Also

- [func contains(Self.Element) -> Bool](string/contains(_:).md)
  Returns a Boolean value indicating whether the sequence contains the given element.
- [func allSatisfy((Self.Element) throws -> Bool) rethrows -> Bool](string/allsatisfy(_:).md)
  Returns a Boolean value indicating whether every element of a sequence satisfies a given predicate.
- [func contains(where: (Self.Element) throws -> Bool) rethrows -> Bool](string/contains(where:).md)
  Returns a Boolean value indicating whether the sequence contains an element that satisfies the given predicate.
- [func first(where: (Self.Element) throws -> Bool) rethrows -> Self.Element?](string/first(where:).md)
  Returns the first element of the sequence that satisfies the given predicate.
- [func firstIndex(of: Self.Element) -> Self.Index?](string/firstindex(of:).md)
  Returns the first index where the specified value appears in the collection.
- [func firstIndex(where: (Self.Element) throws -> Bool) rethrows -> Self.Index?](string/firstindex(where:).md)
  Returns the first index in which an element of the collection satisfies the given predicate.
- [func last(where: (Self.Element) throws -> Bool) rethrows -> Self.Element?](string/last(where:).md)
  Returns the last element of the sequence that satisfies the given predicate.
- [func lastIndex(of: Self.Element) -> Self.Index?](string/lastindex(of:).md)
  Returns the last index where the specified value appears in the collection.
- [func max() -> Self.Element?](string/max.md)
  Returns the maximum element in the sequence.
- [func max<T>(T, T) -> T](string/max(_:_:).md)
- [func max(by: (Self.Element, Self.Element) throws -> Bool) rethrows -> Self.Element?](string/max(by:).md)
  Returns the maximum element in the sequence, using the given predicate as the comparison between elements.
- [func min() -> Self.Element?](string/min.md)
  Returns the minimum element in the sequence.
- [func min<T>(T, T) -> T](string/min(_:_:).md)
- [func min(by: (Self.Element, Self.Element) throws -> Bool) rethrows -> Self.Element?](string/min(by:).md)
  Returns the minimum element in the sequence, using the given predicate as the comparison between elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/string/lastindex(where:))*