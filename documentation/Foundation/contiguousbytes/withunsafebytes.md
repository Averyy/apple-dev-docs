# withUnsafeBytes(_:)

**Framework**: Foundation  
**Kind**: method  
**Required**: Yes

Calls the given closure with a pointer to the underlying bytes of the type’s contiguous storage.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func withUnsafeBytes<R>(_ body: (UnsafeRawBufferPointer) throws -> R) rethrows -> R
```

#### Return Value

The return value, if any, of the body closure parameter.

#### Discussion

The following example copies the bytes from a string encoded using `utf8` into a buffer of `UInt8`:

```swift
let data = "Hello".data(using: .utf8)
var byteBuffer: [UInt8] = []
_ = data?.withUnsafeBytes { buffer in
    byteBuffer.append(contentsOf: buffer)
}

// byteBuffer = [72, 101, 108, 108, 111]
```

## Parameters

- `body`: A closure with an   parameter that points to the contiguous storage for the type. If no such storage exists, the method creates it. If   has a return value, this method also returns that value. The argument is valid only for the duration of the closure’s execution.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/contiguousbytes/withunsafebytes(_:))*