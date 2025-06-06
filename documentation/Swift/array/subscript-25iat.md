# subscript(_:)

**Framework**: Swift  
**Kind**: subscript

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

#### Overview

The following example uses indexed subscripting to update an array’s second element. After assigning the new value (`"Butler"`) at a specific position, that value is immediately available at that same position.

```swift
var streets = ["Adams", "Bryant", "Channing", "Douglas", "Evarts"]
streets[1] = "Butler"
print(streets[1])
// Prints "Butler"
```

> **Note**: Reading an element from an array is O(1). Writing is O(1) unless the array’s storage is shared with another array or uses a bridged `NSArray` instance as its storage, in which case writing is O(), where  is the length of the array.

## Parameters

- `index`: The position of the element to access.   must be   greater than or equal to   and less than  .

## See Also

- [var first: Self.Element?](array/first.md)
  The first element of the collection.
- [var last: Self.Element?](array/last.md)
  The last element of the collection.
- [subscript(Range<Int>) -> ArraySlice<Element>](array/subscript(_:)-53fvb.md)
  Accesses a contiguous subrange of the array’s elements.
- [subscript<R>(R) -> Self.SubSequence](array/subscript(_:)-3kwny.md)
- [subscript<R>(R) -> Self.SubSequence](array/subscript(_:)-4h7rl.md)
  Accesses the contiguous subrange of the collection’s elements specified by a range expression.
- [subscript((UnboundedRange_) -> ()) -> Self.SubSequence](array/subscript(_:)-3pmfg.md)
- [func randomElement() -> Self.Element?](array/randomelement.md)
  Returns a random element of the collection.
- [func randomElement<T>(using: inout T) -> Self.Element?](array/randomelement(using:).md)
  Returns a random element of the collection, using the given generator as a source for randomness.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/array/subscript(_:)-25iat)*