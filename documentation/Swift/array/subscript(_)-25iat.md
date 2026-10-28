# subscript(_:)

**Framework**: Swift  
**Kind**: subscript  
**Role**: Instance Subscript

Accesses the element at the specified position.

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
subscript(index: Int) -> Element { get set }
```

## Overview

The following example uses indexed subscripting to update an array’s second element. After assigning the new value (`"Butler"`) at a specific position, that value is immediately available at that same position.

```swift
var streets = ["Adams", "Bryant", "Channing", "Douglas", "Evarts"]
streets[1] = "Butler"
print(streets[1])
// Prints "Butler"
```

> **Complexity**: Reading an element from an array is O(1). Writing is O(1) unless the array’s storage is shared with another array or uses a bridged `NSArray` instance as its storage, in which case writing is O(*n*), where *n* is the length of the array.

## Parameters

- `index`: The position of the element to access. `index` must be greater than or equal to `startIndex` and less than `endIndex`.

## See Also

### Accessing Elements
- [var first: Self.Element?](./first.md)
  The first element of the collection.
- [var last: Self.Element?](./last.md)
  The last element of the collection.
- [subscript(Range<Int>) -> ArraySlice<Element>](./subscript%28_%29-53fvb.md)
  Accesses a contiguous subrange of the array’s elements.
- [subscript<R>(R) -> Self.SubSequence](./subscript%28_%29-3kwny.md)
- [subscript<R>(R) -> Self.SubSequence](./subscript%28_%29-4h7rl.md)
  Accesses the contiguous subrange of the collection’s elements specified by a range expression.
- [subscript(UnboundedRange) -> Self.SubSequence](./subscript%28_%29-3pmfg.md)
- [func randomElement() -> Self.Element?](./randomelement%28%29.md)
  Returns a random element of the collection.
- [func randomElement<T>(using: inout T) -> Self.Element?](./randomelement%28using%29.md)
  Returns a random element of the collection, using the given generator as a source for randomness.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/array/subscript(_:)-25iat)*