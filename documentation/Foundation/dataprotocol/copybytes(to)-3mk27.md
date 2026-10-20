# copyBytes(to:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Copies the bytes of data from the type into a raw memory buffer.

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
func copyBytes(to ptr: UnsafeMutableRawBufferPointer) -> Int
```

#### Return Value

The number of bytes copied.

#### Discussion

The following example copies the bytes from the raw memory buffer into the provided raw memory buffer:

```swift
let source: [UInt8] = [0, 1, 2]
var dest: [UInt8] = [0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF]
dest.withUnsafeMutableBytes { destBufferPtr in
    let count = source.copyBytes(to: destBufferPtr)
    // count == 3
}
// dest = [0x00, 0x01, 0x02, 0xFF, 0xFF, 0xFF]

```

## Parameters

- `ptr`: A pointer to the raw memory buffer you want to copy the bytes into.

## See Also

### Copying Underlying Bytes
- [func copyBytes<DestinationType>(to: UnsafeMutableBufferPointer<DestinationType>) -> Int](./copybytes%28to%29-52wps.md)
  Copies the bytes of data from the type into a typed memory buffer.
- [func copyBytes<DestinationType>(to: UnsafeMutableBufferPointer<DestinationType>, count: Int) -> Int](./copybytes%28to,count%29-6krsm.md)
  Copies the provided number of bytes from the start of the type into  a typed memory buffer.
- [func copyBytes(to: UnsafeMutableRawBufferPointer, count: Int) -> Int](./copybytes%28to,count%29-29t5.md)
  Copies the provided number of bytes from the start of the type into a raw memory buffer.
- [func copyBytes<DestinationType, R>(to: UnsafeMutableBufferPointer<DestinationType>, from: R) -> Int](./copybytes%28to,from%29-1ol47.md)
  Copies a range of the bytes from the type into a typed memory buffer.
- [func copyBytes<R>(to: UnsafeMutableRawBufferPointer, from: R) -> Int](./copybytes%28to,from%29-1y839.md)
  Copies a range of the bytes from the type into a raw memory buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/dataprotocol/copybytes(to:)-3mk27)*