# copyBytes(to:count:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Copies the provided number of bytes from the start of the type into a raw memory buffer.

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
@discardableResult
func copyBytes(to: UnsafeMutableRawBufferPointer, count: Int) -> Int
```

## Return Value

The number of bytes copied.

## Discussion

The following example copies the number of bytes that `count` identified from the beginning of the raw memory buffer into the provided raw memory buffer:

```swift
let source: [UInt8] = [0, 1, 2]
var dest: [UInt8] = [0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF]
dest.withUnsafeMutableBytes { destBufferPtr in
    let count = source.copyBytes(to: destBufferPtr, count: 2)
    // count == 2
}
// dest = [0x00, 0x01, 0xFF, 0xFF, 0xFF, 0xFF]
```

## Parameters

- `to`: A  pointer to the raw memory buffer you want to copy the bytes into.
- `count`: The number of bytes to copy.

## Default Implementations

### DataProtocol Implementations
- [func copyBytes(to: UnsafeMutableRawBufferPointer, count: Int) -> Int](./copybytes%28to,count%29-45x1l.md)
  Copies the provided number of bytes from the start of the type into a raw memory buffer.
- [func copyBytes<DestinationType>(to: UnsafeMutableBufferPointer<DestinationType>, count: Int) -> Int](./copybytes%28to,count%29-9wm8s.md)
  Copies the provided number of bytes from the start of the type into a typed memory buffer.

## See Also

### Copying Underlying Bytes
- [func copyBytes<DestinationType>(to: UnsafeMutableBufferPointer<DestinationType>) -> Int](./copybytes%28to%29-52wps.md)
  Copies the bytes of data from the type into a typed memory buffer.
- [func copyBytes(to: UnsafeMutableRawBufferPointer) -> Int](./copybytes%28to%29-3mk27.md)
  Copies the bytes of data from the type into a raw memory buffer.
- [func copyBytes<DestinationType>(to: UnsafeMutableBufferPointer<DestinationType>, count: Int) -> Int](./copybytes%28to,count%29-6krsm.md)
  Copies the provided number of bytes from the start of the type into  a typed memory buffer.
- [func copyBytes<DestinationType, R>(to: UnsafeMutableBufferPointer<DestinationType>, from: R) -> Int](./copybytes%28to,from%29-1ol47.md)
  Copies a range of the bytes from the type into a typed memory buffer.
- [func copyBytes<R>(to: UnsafeMutableRawBufferPointer, from: R) -> Int](./copybytes%28to,from%29-1y839.md)
  Copies a range of the bytes from the type into a raw memory buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/dataprotocol/copybytes(to:count:)-29t5)*