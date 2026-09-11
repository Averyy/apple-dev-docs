# load(fromByteOffset:as:_:)

**Framework**: Swift  
**Kind**: method

Returns a value constructed from the raw memory at the specified offset.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
func load<T>(fromByteOffset offset: Int, as type: T.Type, _ byteOrder: ByteOrder) -> T where T : ConvertibleFromBytes, T : FixedWidthInteger
```

#### Return Value

A new value of type `T`, read from `offset`.

#### Discussion

The range of bytes required to construct a value of type `T` starting at `offset` must be completely within the span. `offset` is not required to be aligned for `T`.

## Parameters

- `offset`: The offset from the beginning of this span, in bytes. `offset` must be nonnegative.
- `type`: The type of the instance to create.
- `byteOrder`: The order in which the bytes will be decoded.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/mutablerawspan/load(frombyteoffset:as:_:))*