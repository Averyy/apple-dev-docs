# decodeIfPresent(_:)

**Framework**: Swift  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Decodes a value of the given type, if present.

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
mutating func decodeIfPresent(_ type: UInt32.Type) throws -> UInt32?
```

#### Return Value

A decoded value of the requested type, or `nil` if the value is a null value, or if there are no more elements to decode.

#### Discussion

This method returns `nil` if the container has no elements left to decode, or if the value is null. The difference between these states can be distinguished by checking `isAtEnd`.

> **Throws**: `DecodingError.typeMismatch` if the encountered encoded value is not convertible to the requested type.

## Parameters

- `type`: The type of value to decode.

## Default Implementations

### UnkeyedDecodingContainer Implementations
- [func decodeIfPresent(Float.Type) throws -> Float?](./decodeifpresent%28_%29-11drn.md)
  Decodes a value of the given type, if present.
- [func decodeIfPresent(String.Type) throws -> String?](./decodeifpresent%28_%29-1mzxv.md)
  Decodes a value of the given type, if present.
- [func decodeIfPresent(Int64.Type) throws -> Int64?](./decodeifpresent%28_%29-33p27.md)
  Decodes a value of the given type, if present.
- [func decodeIfPresent(UInt.Type) throws -> UInt?](./decodeifpresent%28_%29-3hokf.md)
  Decodes a value of the given type, if present.
- [func decodeIfPresent(Double.Type) throws -> Double?](./decodeifpresent%28_%29-3tuys.md)
  Decodes a value of the given type, if present.
- [func decodeIfPresent(Int.Type) throws -> Int?](./decodeifpresent%28_%29-4b7tu.md)
  Decodes a value of the given type, if present.
- [func decodeIfPresent(UInt16.Type) throws -> UInt16?](./decodeifpresent%28_%29-4bqkd.md)
  Decodes a value of the given type, if present.
- [func decodeIfPresent(Int16.Type) throws -> Int16?](./decodeifpresent%28_%29-5mgpl.md)
  Decodes a value of the given type, if present.
- [func decodeIfPresent(Int8.Type) throws -> Int8?](./decodeifpresent%28_%29-5zug7.md)
  Decodes a value of the given type, if present.
- [func decodeIfPresent(UInt32.Type) throws -> UInt32?](./decodeifpresent%28_%29-64o4m.md)
  Decodes a value of the given type, if present.
- [func decodeIfPresent(UInt8.Type) throws -> UInt8?](./decodeifpresent%28_%29-6k5py.md)
  Decodes a value of the given type, if present.
- [func decodeIfPresent<T>(T.Type) throws -> T?](./decodeifpresent%28_%29-6snuc.md)
  Decodes a value of the given type, if present.
- [func decodeIfPresent(Bool.Type) throws -> Bool?](./decodeifpresent%28_%29-87qsg.md)
  Decodes a value of the given type, if present.
- [func decodeIfPresent(Int32.Type) throws -> Int32?](./decodeifpresent%28_%29-8nfu7.md)
  Decodes a value of the given type, if present.
- [func decodeIfPresent(UInt128.Type) throws -> UInt128?](./decodeifpresent%28_%29-8we74.md)
  Decodes a value of the given type, if present.
- [func decodeIfPresent(UInt64.Type) throws -> UInt64?](./decodeifpresent%28_%29-9tk6h.md)
  Decodes a value of the given type, if present.
- [func decodeIfPresent(Int128.Type) throws -> Int128?](./decodeifpresent%28_%29-o708.md)
  Decodes a value of the given type, if present.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/unkeyeddecodingcontainer/decodeifpresent(_:)-1oxo9)*