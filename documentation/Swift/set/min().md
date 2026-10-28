# min()

**Framework**: Swift  
**Kind**: method  
**Role**: Instance Method

Returns the minimum element in the sequence.

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
func min() -> Self.Element?
```

Available when `Element` conforms to `Comparable`.

## Return Value

The sequence’s minimum element. If the sequence has no elements, returns `nil`.

## Discussion

This example finds the smallest value in an array of height measurements.

```swift
let heights = [67.5, 65.7, 64.3, 61.1, 58.5, 60.3, 64.9]
let lowestHeight = heights.min()
print(lowestHeight)
// Prints "Optional(58.5)"
```

> **Complexity**: O(*n*), where *n* is the length of the sequence.

## See Also

### Finding Elements
- [subscript(Set<Element>.Index) -> Element](./subscript%28_%29.md)
  Accesses the member at the given position.
- [func contains(where: (Self.Element) throws -> Bool) rethrows -> Bool](./contains%28where%29.md)
  Returns a Boolean value indicating whether the sequence contains an element that satisfies the given predicate.
- [func allSatisfy((Self.Element) throws -> Bool) rethrows -> Bool](./allsatisfy%28_%29.md)
  Returns a Boolean value indicating whether every element of a sequence satisfies a given predicate.
- [func first(where: (Self.Element) throws -> Bool) rethrows -> Self.Element?](./first%28where%29.md)
  Returns the first element of the sequence that satisfies the given predicate.
- [func firstIndex(of: Element) -> Set<Element>.Index?](./firstindex%28of%29.md)
  Returns the index of the given element in the set, or `nil` if the element is not a member of the set.
- [func firstIndex(where: (Self.Element) throws -> Bool) rethrows -> Self.Index?](./firstindex%28where%29.md)
  Returns the first index in which an element of the collection satisfies the given predicate.
- [func index(of: Self.Element) -> Self.Index?](./index%28of%29.md)
  Returns the first index where the specified value appears in the collection.
- [func min(by: (Self.Element, Self.Element) throws -> Bool) rethrows -> Self.Element?](./min%28by%29.md)
  Returns the minimum element in the sequence, using the given predicate as the comparison between elements.
- [func max() -> Self.Element?](./max%28%29.md)
  Returns the maximum element in the sequence.
- [func max(by: (Self.Element, Self.Element) throws -> Bool) rethrows -> Self.Element?](./max%28by%29.md)
  Returns the maximum element in the sequence, using the given predicate as the comparison between elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/set/min())*