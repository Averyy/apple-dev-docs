# firstIndex(of:)

**Framework**: Swift  
**Kind**: method  
**Role**: Instance Method

Returns the index of the given element in the set, or `nil` if the element is not a member of the set.

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
func firstIndex(of member: Element) -> Set<Element>.Index?
```

Available when `Element` conforms to `Hashable`.

## Return Value

The index of `member` if it exists in the set; otherwise, `nil`.

## Discussion

> **Complexity**: O(1)

## Parameters

- `member`: An element to search for in the set.

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
- [func firstIndex(where: (Self.Element) throws -> Bool) rethrows -> Self.Index?](./firstindex%28where%29.md)
  Returns the first index in which an element of the collection satisfies the given predicate.
- [func index(of: Self.Element) -> Self.Index?](./index%28of%29.md)
  Returns the first index where the specified value appears in the collection.
- [func min() -> Self.Element?](./min%28%29.md)
  Returns the minimum element in the sequence.
- [func min(by: (Self.Element, Self.Element) throws -> Bool) rethrows -> Self.Element?](./min%28by%29.md)
  Returns the minimum element in the sequence, using the given predicate as the comparison between elements.
- [func max() -> Self.Element?](./max%28%29.md)
  Returns the maximum element in the sequence.
- [func max(by: (Self.Element, Self.Element) throws -> Bool) rethrows -> Self.Element?](./max%28by%29.md)
  Returns the maximum element in the sequence, using the given predicate as the comparison between elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/set/firstindex(of:))*