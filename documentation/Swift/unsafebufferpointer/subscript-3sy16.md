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
subscript(i: Int) -> Element { get }
```

#### Overview

The following example uses the buffer pointer’s subscript to access every other element of the buffer:

```swift
let numbers = [1, 2, 3, 4, 5]
let sum = numbers.withUnsafeBufferPointer { buffer -> Int in
    var result = 0
    for i in stride(from: buffer.startIndex, to: buffer.endIndex, by: 2) {
        result += buffer[i]
    }
    return result
}
// 'sum' == 9
```

> **Note**: Bounds checks for `i` are performed only in debug mode.

## Parameters

- `i`: The position of the element to access.   must be in the   range  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/unsafebufferpointer/subscript(_:)-3sy16)*