# subscript(_:)

**Framework**: Swift  
**Kind**: subscript

Accesses a contiguous subrange of the buffer’s elements.

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
subscript(bounds: Range<Int>) -> Slice<UnsafeBufferPointer<Element>> { get }
```

#### Overview

The accessed slice uses the same indices for the same elements as the original buffer uses. Always use the slice’s `startIndex` property instead of assuming that its indices start at a particular value.

This example demonstrates getting a slice from a buffer of strings, finding the index of one of the strings in the slice, and then using that index in the original buffer.

```swift
let streets = ["Adams", "Bryant", "Channing", "Douglas", "Evarts"]
streets.withUnsafeBufferPointer { buffer in
    let streetSlice = buffer[2..<buffer.endIndex]
    print(Array(streetSlice))
    // Prints "["Channing", "Douglas", "Evarts"]"
    let index = streetSlice.firstIndex(of: "Evarts")    // 4
    print(buffer[index!])
    // Prints "Evarts"
}
```

> **Note**: Bounds checks for `bounds` are performed only in debug mode.

## Parameters

- `bounds`: A range of the buffer’s indices. The bounds of   the range must be valid indices of the buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/unsafebufferpointer/subscript(_:)-6ynnu)*