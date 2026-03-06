# init(capacity:initializingWith:)

**Framework**: Swift  
**Kind**: init

Creates an array with the specified capacity, and then calls the given closure with an output span covering the array’s uninitialized memory.

**Availability**:
- iOS 12.2+
- iPadOS 12.2+
- Mac Catalyst 12.2+
- macOS 10.14.4+
- tvOS 12.2+
- visionOS 1.0+
- watchOS 5.2+

## Declaration

```swift
init<E>(capacity: Int, initializingWith initializer: (inout OutputSpan<Element>) throws(E) -> Void) throws(E) where E : Error
```

#### Discussion

Inside the closure, initialize elements by appending to the `OutputSpan`. The `OutputSpan` keeps track of memory’s initialization state, ensuring safety. Its `count` at the end of the closure will become the `count` of the newly-initialized array.

> **Note**: While the resulting array may have a capacity larger than the requested amount, the `OutputSpan` passed to the closure will cover exactly the number of elements requested.

## Parameters

- `capacity`: The number of elements to allocate space for in the new array.
- `initializer`: A closure that initializes the elements of the new array. - Parameters: - span: An `OutputSpan` covering uninitialized memory with space for the specified number of elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/contiguousarray/init(capacity:initializingwith:))*