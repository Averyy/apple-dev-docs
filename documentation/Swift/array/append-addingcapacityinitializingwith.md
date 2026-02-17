# append(addingCapacity:initializingWith:)

**Framework**: Swift  
**Kind**: method

Grows the array to have enough capacity for the specified number of elements, then calls the closure with an OutputSpan covering the array’s uninitialized memory.

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
mutating func append<E>(addingCapacity uninitializedCount: Int, initializingWith initializer: (inout OutputSpan<Element>) throws(E) -> Void) throws(E) where E : Error
```

#### Discussion

Inside the closure, initialize elements by appending to `span`. It ensures safety by keeping track of the initialization state of the memory At the end of the closure, `span`’s `count` elements will have been appended to the array.

If the closure throws an error, the items appended until that point will remain in the array.

## Parameters

- `uninitializedCount`: The number of new elements the array should have   space for.
- `initializer`: A closure that initializes new elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/array/append(addingcapacity:initializingwith:))*