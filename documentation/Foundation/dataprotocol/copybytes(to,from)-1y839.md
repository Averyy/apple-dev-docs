# copyBytes(to:from:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Copies a range of the bytes from the type into a raw memory buffer.

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
func copyBytes<R>(to: UnsafeMutableRawBufferPointer, from: R) -> Int where R : RangeExpression, Self.Index == R.Bound
```

#### Return Value

The number of bytes copied.

#### Discussion

The following example copies the source bytes that the provided range identifies into the beginning of the specified raw memory buffer:

```swift
let source: [UInt8] = [0, 1, 2]
var dest: [UInt8] = [0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF]
_ = dest.withUnsafeMutableBytes { destBufferPtr in
    source.copyBytes(to: destBufferPtr, from: 1...2)
}
// dest = [0x01, 0x02, 0xFF, 0xFF, 0xFF, 0xFF]
```

## Parameters

- `to`: A pointer to the raw memory buffer you want to copy the bytes into.
- `from`: The range of bytes to copy.

## Default Implementations

### DataProtocol Implementations
- [func copyBytes<R>(to: UnsafeMutableRawBufferPointer, from: R) -> Int](./copybytes%28to,from%29-2u470.md)
  Copies a range of the bytes from the type into a raw memory buffer.
- [func copyBytes<DestinationType, R>(to: UnsafeMutableBufferPointer<DestinationType>, from: R)](./copybytes%28to,from%29-44inx.md)
  Copies a range of the bytes from the type into a typed memory buffer.
- [func copyBytes<DestinationType, R>(to: UnsafeMutableBufferPointer<DestinationType>, from: R) -> Int](./copybytes%28to,from%29-9bgoo.md)
  Copies a range of the bytes from the type into a typed memory buffer.

## See Also

### Copying Underlying Bytes
- [func copyBytes<DestinationType>(to: UnsafeMutableBufferPointer<DestinationType>) -> Int](./copybytes%28to%29-52wps.md)
  Copies the bytes of data from the type into a typed memory buffer.
- [func copyBytes(to: UnsafeMutableRawBufferPointer) -> Int](./copybytes%28to%29-3mk27.md)
  Copies the bytes of data from the type into a raw memory buffer.
- [func copyBytes<DestinationType>(to: UnsafeMutableBufferPointer<DestinationType>, count: Int) -> Int](./copybytes%28to,count%29-6krsm.md)
  Copies the provided number of bytes from the start of the type into  a typed memory buffer.
- [func copyBytes(to: UnsafeMutableRawBufferPointer, count: Int) -> Int](./copybytes%28to,count%29-29t5.md)
  Copies the provided number of bytes from the start of the type into a raw memory buffer.
- [func copyBytes<DestinationType, R>(to: UnsafeMutableBufferPointer<DestinationType>, from: R) -> Int](./copybytes%28to,from%29-1ol47.md)
  Copies a range of the bytes from the type into a typed memory buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/dataprotocol/copybytes(to:from:)-1y839)*