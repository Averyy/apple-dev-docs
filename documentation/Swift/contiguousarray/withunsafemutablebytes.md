# withUnsafeMutableBytes(_:)

**Framework**: Swift  
**Kind**: method

Calls the given closure with a pointer to the underlying bytes of the array’s mutable contiguous storage.

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
mutating func withUnsafeMutableBytes<R>(_ body: (UnsafeMutableRawBufferPointer) throws -> R) rethrows -> R
```

#### Return Value

The return value, if any, of the `body` closure parameter.

#### Discussion

The array’s `Element` type must be a , which can be copied with just a bit-for-bit copy without any indirection or reference-counting operations. Generally, native Swift types that do not contain strong or weak references are trivial, as are imported C structs and enums.

The following example copies bytes from the `byteValues` array into `numbers`, an array of `Int32`:

```swift
var numbers: [Int32] = [0, 0]
var byteValues: [UInt8] = [0x01, 0x00, 0x00, 0x00, 0x02, 0x00, 0x00, 0x00]

numbers.withUnsafeMutableBytes { destBytes in
    byteValues.withUnsafeBytes { srcBytes in
        destBytes.copyBytes(from: srcBytes)
    }
}
// numbers == [1, 2]
```

> **Note**: This example shows the behavior on a little-endian platform.

The pointer passed as an argument to `body` is valid only for the lifetime of the closure. Do not escape it from the closure for later use.

> ⚠️ **Warning**: Do not rely on anything about the array that is the target of this method during execution of the `body` closure; it might not appear to have its correct value. Instead, use only the `UnsafeMutableRawBufferPointer` argument to `body`.

## Parameters

- `body`: A closure with an    parameter that points to the contiguous storage for the array.   If no such storage exists, it is created. If   has a return value, that value is also   used as the return value for the   method.   The argument is valid only for the duration of the closure’s   execution.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/contiguousarray/withunsafemutablebytes(_:))*