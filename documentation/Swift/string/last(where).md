# last(where:)

**Framework**: Swift  
**Kind**: method  
**Role**: Instance Method

Returns the last element of the sequence that satisfies the given predicate.

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
func last(where predicate: (Self.Element) throws -> Bool) rethrows -> Self.Element?
```

## Return Value

The last element of the sequence that satisfies `predicate`, or `nil` if there is no element that satisfies `predicate`.

## Discussion

This example uses the `last(where:)` method to find the last negative number in an array of integers:

```swift
let numbers = [3, 7, 4, -2, 9, -6, 10, 1]
if let lastNegative = numbers.last(where: { $0 < 0 }) {
    print("The last negative number is \(lastNegative).")
}
// Prints "The last negative number is -6."
```

> **Complexity**: O(*n*), where *n* is the length of the collection.

## Parameters

- `predicate`: A closure that takes an element of the sequence as its argument and returns a Boolean value indicating whether the element is a match.

## See Also

### Finding Characters
- [func contains(Self.Element) -> Bool](./contains%28_%29.md)
  Returns a Boolean value indicating whether the sequence contains the given element.
- [func allSatisfy((Self.Element) throws -> Bool) rethrows -> Bool](./allsatisfy%28_%29.md)
  Returns a Boolean value indicating whether every element of a sequence satisfies a given predicate.
- [func contains(where: (Self.Element) throws -> Bool) rethrows -> Bool](./contains%28where%29.md)
  Returns a Boolean value indicating whether the sequence contains an element that satisfies the given predicate.
- [func first(where: (Self.Element) throws -> Bool) rethrows -> Self.Element?](./first%28where%29.md)
  Returns the first element of the sequence that satisfies the given predicate.
- [func firstIndex(of: Self.Element) -> Self.Index?](./firstindex%28of%29.md)
  Returns the first index where the specified value appears in the collection.
- [func firstIndex(where: (Self.Element) throws -> Bool) rethrows -> Self.Index?](./firstindex%28where%29.md)
  Returns the first index in which an element of the collection satisfies the given predicate.
- [func lastIndex(of: Self.Element) -> Self.Index?](./lastindex%28of%29.md)
  Returns the last index where the specified value appears in the collection.
- [func lastIndex(where: (Self.Element) throws -> Bool) rethrows -> Self.Index?](./lastindex%28where%29.md)
  Returns the index of the last element in the collection that matches the given predicate.
- [func max() -> Self.Element?](./max%28%29.md)
  Returns the maximum element in the sequence.
- [func max<T>(T, T) -> T](./max%28_,_%29.md)
- [func max(by: (Self.Element, Self.Element) throws -> Bool) rethrows -> Self.Element?](./max%28by%29.md)
  Returns the maximum element in the sequence, using the given predicate as the comparison between elements.
- [func min() -> Self.Element?](./min%28%29.md)
  Returns the minimum element in the sequence.
- [func min<T>(T, T) -> T](./min%28_,_%29.md)
- [func min(by: (Self.Element, Self.Element) throws -> Bool) rethrows -> Self.Element?](./min%28by%29.md)
  Returns the minimum element in the sequence, using the given predicate as the comparison between elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/string/last(where:))*