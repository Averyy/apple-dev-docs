# init(repeating:count:)

**Framework**: Swift  
**Kind**: init

Creates a new array containing the specified number of a single, repeated value.

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
init(repeating repeatedValue: Element, count: Int)
```

#### Discussion

Here’s an example of creating an array initialized with five strings containing the letter .

```swift
let fiveZs = Array(repeating: "Z", count: 5)
print(fiveZs)
// Prints "["Z", "Z", "Z", "Z", "Z"]"
```

## Parameters

- `repeatedValue`: The element to repeat.
- `count`: The number of times to repeat the value passed in the    parameter.   must be zero or greater.

## See Also

- [init()](array/init.md)
  Creates a new, empty array.
- [init<S>(S)](array/init(_:)-1ip9h.md)
  Creates a new instance of a collection containing the elements of a sequence.
- [init<S>(S)](array/init(_:)-236cl.md)
  Creates an array containing the elements of a sequence.
- [init(unsafeUninitializedCapacity: Int, initializingWith: (inout UnsafeMutableBufferPointer<Element>, inout Int) throws -> Void) rethrows](array/init(unsafeuninitializedcapacity:initializingwith:).md)
  Creates an array with the specified capacity, then calls the given closure with a buffer covering the array’s uninitialized memory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/array/init(repeating:count:))*