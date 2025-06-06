# init(_:)

**Framework**: Swift  
**Kind**: init

Creates a new instance of a collection containing the elements of a sequence.

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
init<S>(_ elements: S) where S : Sequence, Self.Element == S.Element
```

## Parameters

- `elements`: The sequence of elements for the new collection.

## See Also

- [init()](array/init.md)
  Creates a new, empty array.
- [init<S>(S)](array/init(_:)-236cl.md)
  Creates an array containing the elements of a sequence.
- [init(repeating: Element, count: Int)](array/init(repeating:count:).md)
  Creates a new array containing the specified number of a single, repeated value.
- [init(unsafeUninitializedCapacity: Int, initializingWith: (inout UnsafeMutableBufferPointer<Element>, inout Int) throws -> Void) rethrows](array/init(unsafeuninitializedcapacity:initializingwith:).md)
  Creates an array with the specified capacity, then calls the given closure with a buffer covering the array’s uninitialized memory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/array/init(_:)-1ip9h)*