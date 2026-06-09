# init(rawCapacity:initializingWith:)

**Framework**: Foundation  
**Kind**: init

Creates a data instance with the specified capacity, and then calls the given closure with an output span covering the instance’s uninitialized memory.

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
init<E>(rawCapacity capacity: Int, initializingWith initializer: @_lifetime(span: copy span) (inout OutputRawSpan) throws(E) -> Void) throws(E) where E : Error
```

#### Discussion

Inside the closure, initialize elements by appending to the `OutputRawSpan`. The `OutputRawSpan` keeps track of the initialized memory, ensuring safety. Its `count` at the end of the closure will become the `count` of the newly-initialized instance of `Data`.

> **Note**: While the resulting `Data` may have a capacity larger than the requested amount, the `OutputRawSpan` passed to the closure will cover exactly the number of bytes requested.

## Parameters

- `capacity`: The number of bytes to allocate space for in the new `Data`.
- `initializer`: A closure to initialize the allocated memory. - Parameters: - span: An `OutputRawSpan` covering uninitialized memory with space for the specified number of bytes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/data/init(rawcapacity:initializingwith:))*