# init(unsafeUninitializedCapacity:initializingWith:)

**Framework**: Swift  
**Kind**: init

Creates an array with the specified capacity, then calls the given closure with a buffer covering the array’s uninitialized memory.

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
init(unsafeUninitializedCapacity: Int, initializingWith initializer: (inout UnsafeMutableBufferPointer<Element>, inout Int) throws -> Void) rethrows
```

#### Discussion

Inside the closure, set the `initializedCount` parameter to the number of elements that are initialized by the closure. The memory in the range `buffer[0..<initializedCount]` must be initialized at the end of the closure’s execution, and the memory in the range `buffer[initializedCount...]` must be uninitialized. This postcondition must hold even if the `initializer` closure throws an error.

> **Note**: While the resulting array may have a capacity larger than the requested amount, the buffer passed to the closure will cover exactly the requested number of elements.

## Parameters

- `unsafeUninitializedCapacity`: The number of elements to allocate   space for in the new array.
- `initializer`: A closure that initializes elements and sets the count   of the new array.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/contiguousarray/init(unsafeuninitializedcapacity:initializingwith:))*