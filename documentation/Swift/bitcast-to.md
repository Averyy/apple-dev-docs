# bitCast(_:to:)

**Framework**: Swift  
**Kind**: func

Returns the bits of the given instance, interpreted as having the specified type.

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
func bitCast<T, U>(_ original: T, to type: U.Type) -> U where T : ConvertibleToBytes, U : ConvertibleFromBytes
```

#### Return Value

A new instance of type `U`, cast from `original`.

#### Discussion

`T` and `U` must have the same-sized memory representation. If they don’t, this function will trap.

## Parameters

- `original`: The instance to cast to `type`.
- `type`: The type to cast `original` to.

## See Also

- [typealias FullyInhabited](fullyinhabited.md)
  A protocol for types whose memory can safely be written as or read from raw bytes.
- [protocol ConvertibleFromBytes](convertiblefrombytes.md)
  A protocol for types whose memory can safely be populated from raw bytes, resulting in a valid instance.
- [protocol ConvertibleToBytes](convertibletobytes.md)
  A protocol for types whose memory can safely be read as individual raw bytes.
- [enum ByteOrder](byteorder.md)
  A byte ordering in memory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/bitcast(_:to:))*