# max()

**Framework**: Swift  
**Kind**: method  
**Role**: Instance Method

Returns the maximum element in the sequence.

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
@warn_unqualified_access
func max() -> Self.Element?
```

Available when `Element` conforms to `Comparable`.

## Return Value

The sequence’s maximum element. If the sequence has no elements, returns `nil`.

## Discussion

This example finds the largest value in an array of height measurements.

```swift
let heights = [67.5, 65.7, 64.3, 61.1, 58.5, 60.3, 64.9]
let greatestHeight = heights.max()
print(greatestHeight)
// Prints "Optional(67.5)"
```

> **Complexity**: O(*n*), where *n* is the length of the sequence.

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
- [func last(where: (Self.Element) throws -> Bool) rethrows -> Self.Element?](./last%28where%29.md)
  Returns the last element of the sequence that satisfies the given predicate.
- [func lastIndex(of: Self.Element) -> Self.Index?](./lastindex%28of%29.md)
  Returns the last index where the specified value appears in the collection.
- [func lastIndex(where: (Self.Element) throws -> Bool) rethrows -> Self.Index?](./lastindex%28where%29.md)
  Returns the index of the last element in the collection that matches the given predicate.
- [func max<T>(T, T) -> T](./max%28_,_%29.md)
- [func max(by: (Self.Element, Self.Element) throws -> Bool) rethrows -> Self.Element?](./max%28by%29.md)
  Returns the maximum element in the sequence, using the given predicate as the comparison between elements.
- [func min() -> Self.Element?](./min%28%29.md)
  Returns the minimum element in the sequence.
- [func min<T>(T, T) -> T](./min%28_,_%29.md)
- [func min(by: (Self.Element, Self.Element) throws -> Bool) rethrows -> Self.Element?](./min%28by%29.md)
  Returns the minimum element in the sequence, using the given predicate as the comparison between elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/string/max())*