# copyBytes(to:from:)

**Framework**: Foundation  
**Kind**: method  
**Required**: Yes

Copies a range of the bytes from the type into a typed memory buffer.

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
func copyBytes<DestinationType, R>(to: UnsafeMutableBufferPointer<DestinationType>, from: R) -> Int where R : RangeExpression, Self.Index == R.Bound
```

#### Return Value

The number of bytes copied.

#### Discussion

The following example copies the source bytes that the provided range identifies into the beginning of the specified typed memory buffer:

```swift
let source: [UInt8] = [0, 1, 2]
var dest: [UInt8] = [0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF]
dest.withUnsafeMutableBufferPointer { typedMemBuffer in
    source.copyBytes(to: typedMemBuffer, from: 1...2)
}
// dest = [0x01, 0x02, 0xFF, 0xFF, 0xFF, 0xFF]

```

## Parameters

- `to`: A typed pointer to the buffer you want to copy the bytes into.
- `from`: The range of bytes to copy.

## See Also

- [func copyBytes<DestinationType>(to: UnsafeMutableBufferPointer<DestinationType>) -> Int](dataprotocol/copybytes(to:)-52wps.md)
  Copies the bytes of data from the type into a typed memory buffer.
- [func copyBytes(to: UnsafeMutableRawBufferPointer) -> Int](dataprotocol/copybytes(to:)-3mk27.md)
  Copies the bytes of data from the type into a raw memory buffer.
- [func copyBytes<DestinationType>(to: UnsafeMutableBufferPointer<DestinationType>, count: Int) -> Int](dataprotocol/copybytes(to:count:)-6krsm.md)
  Copies the provided number of bytes from the start of the type into  a typed memory buffer.
- [func copyBytes(to: UnsafeMutableRawBufferPointer, count: Int) -> Int](dataprotocol/copybytes(to:count:)-29t5.md)
  Copies the provided number of bytes from the start of the type into a raw memory buffer.
- [func copyBytes<R>(to: UnsafeMutableRawBufferPointer, from: R) -> Int](dataprotocol/copybytes(to:from:)-1y839.md)
  Copies a range of the bytes from the type into a raw memory buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/dataprotocol/copybytes(to:from:)-1ol47)*