# first(where:)

**Framework**: Swift  
**Kind**: method  
**Role**: Instance Method

Returns the first element of the sequence that satisfies the given predicate.

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
func first(where predicate: (Self.Element) throws -> Bool) rethrows -> Self.Element?
```

## Return Value

The first element of the sequence that satisfies `predicate`, or `nil` if there is no element that satisfies `predicate`.

## Discussion

The following example uses the `first(where:)` method to find the first negative number in an array of integers:

```swift
let numbers = [3, 7, 4, -2, 9, -6, 10, 1]
if let firstNegative = numbers.first(where: { $0 < 0 }) {
    print("The first negative number is \(firstNegative).")
}
// Prints "The first negative number is -2."
```

> **Complexity**: O(*n*), where *n* is the length of the sequence.

## Parameters

- `predicate`: A closure that takes an element of the sequence as its argument and returns a Boolean value indicating whether the element is a match.

## See Also

### Finding Elements
- [subscript(Set<Element>.Index) -> Element](./subscript%28_%29.md)
  Accesses the member at the given position.
- [func contains(where: (Self.Element) throws -> Bool) rethrows -> Bool](./contains%28where%29.md)
  Returns a Boolean value indicating whether the sequence contains an element that satisfies the given predicate.
- [func allSatisfy((Self.Element) throws -> Bool) rethrows -> Bool](./allsatisfy%28_%29.md)
  Returns a Boolean value indicating whether every element of a sequence satisfies a given predicate.
- [func firstIndex(of: Element) -> Set<Element>.Index?](./firstindex%28of%29.md)
  Returns the index of the given element in the set, or `nil` if the element is not a member of the set.
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

*[View on Apple Developer](https://developer.apple.com/documentation/swift/set/first(where:))*