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
subscript(i: Int) -> Element { get nonmutating set }
```

#### Overview

The following example uses the buffer pointer’s subscript to access and modify the elements of a mutable buffer pointing to the contiguous contents of an array:

```swift
var numbers = [1, 2, 3, 4, 5]
numbers.withUnsafeMutableBufferPointer { buffer in
    for i in stride(from: buffer.startIndex, to: buffer.endIndex - 1, by: 2) {
        let x = buffer[i]
        buffer[i + 1] = buffer[i]
        buffer[i] = x
    }
}
print(numbers)
// Prints "[2, 1, 4, 3, 5]"

Uninitialized memory cannot be initialized to a nontrivial type
using this subscript. Instead, use an initializing method, such as
`initializeElement(at:to:)`
```

> **Note**: Bounds checks for `i` are performed only in debug mode.

Bounds checks for `i` are performed only in debug mode.

## Parameters

- `i`: The position of the element to access.   must be in the   range  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/unsafemutablebufferpointer/subscript(_:)-2vl82)*