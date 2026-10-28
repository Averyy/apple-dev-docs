# decodeIfPresent(_:forKey:)

**Framework**: Swift  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Decodes a value of the given type for the given key, if present.

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
func decodeIfPresent(_ type: UInt.Type, forKey key: Self.Key) throws -> UInt?
```

## Return Value

A decoded value of the requested type, or `nil` if the `Decoder` does not have an entry associated with the given key, or if the value is a null value.

## Discussion

This method returns `nil` if the container does not have a value associated with `key`, or if the value is null. The difference between these states can be distinguished with a `contains(_:)` call.

> **Throws**: `DecodingError.typeMismatch` if the encountered encoded value is not convertible to the requested type.

## Parameters

- `type`: The type of value to decode.
- `key`: The key that the decoded value is associated with.

## Default Implementations

### KeyedDecodingContainerProtocol Implementations
- [func decodeIfPresent(UInt16.Type, forKey: Self.Key) throws -> UInt16?](./decodeifpresent%28_,forkey%29-189q8.md)
  Decodes a value of the given type for the given key, if present.
- [func decodeIfPresent(UInt64.Type, forKey: Self.Key) throws -> UInt64?](./decodeifpresent%28_,forkey%29-1i7qt.md)
  Decodes a value of the given type for the given key, if present.
- [func decodeIfPresent(Int64.Type, forKey: Self.Key) throws -> Int64?](./decodeifpresent%28_,forkey%29-2g0dg.md)
  Decodes a value of the given type for the given key, if present.
- [func decodeIfPresent<T>(T.Type, forKey: Self.Key) throws -> T?](./decodeifpresent%28_,forkey%29-2o9mb.md)
  Decodes a value of the given type for the given key, if present.
- [func decodeIfPresent(UInt8.Type, forKey: Self.Key) throws -> UInt8?](./decodeifpresent%28_,forkey%29-4j3g5.md)
  Decodes a value of the given type for the given key, if present.
- [func decodeIfPresent(Int8.Type, forKey: Self.Key) throws -> Int8?](./decodeifpresent%28_,forkey%29-5vg9.md)
  Decodes a value of the given type for the given key, if present.
- [func decodeIfPresent(Int16.Type, forKey: Self.Key) throws -> Int16?](./decodeifpresent%28_,forkey%29-613fl.md)
  Decodes a value of the given type for the given key, if present.
- [func decodeIfPresent(String.Type, forKey: Self.Key) throws -> String?](./decodeifpresent%28_,forkey%29-6d6xo.md)
  Decodes a value of the given type for the given key, if present.
- [func decodeIfPresent(Bool.Type, forKey: Self.Key) throws -> Bool?](./decodeifpresent%28_,forkey%29-6lga8.md)
  Decodes a value of the given type for the given key, if present.
- [func decodeIfPresent(UInt128.Type, forKey: Self.Key) throws -> UInt128?](./decodeifpresent%28_,forkey%29-6ze9z.md)
  Decodes a value of the given type for the given key, if present.
- [func decodeIfPresent(Int32.Type, forKey: Self.Key) throws -> Int32?](./decodeifpresent%28_,forkey%29-8cej4.md)
  Decodes a value of the given type for the given key, if present.
- [func decodeIfPresent(Double.Type, forKey: Self.Key) throws -> Double?](./decodeifpresent%28_,forkey%29-8l1ao.md)
  Decodes a value of the given type for the given key, if present.
- [func decodeIfPresent(Int128.Type, forKey: Self.Key) throws -> Int128?](./decodeifpresent%28_,forkey%29-8ujl.md)
  Decodes a value of the given type for the given key, if present.
- [func decodeIfPresent(Float.Type, forKey: Self.Key) throws -> Float?](./decodeifpresent%28_,forkey%29-8w7i2.md)
  Decodes a value of the given type for the given key, if present.
- [func decodeIfPresent(UInt32.Type, forKey: Self.Key) throws -> UInt32?](./decodeifpresent%28_,forkey%29-8wk2a.md)
  Decodes a value of the given type for the given key, if present.
- [func decodeIfPresent(Int.Type, forKey: Self.Key) throws -> Int?](./decodeifpresent%28_,forkey%29-fyzb.md)
  Decodes a value of the given type for the given key, if present.
- [func decodeIfPresent(UInt.Type, forKey: Self.Key) throws -> UInt?](./decodeifpresent%28_,forkey%29-g4cp.md)
  Decodes a value of the given type for the given key, if present.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/keyeddecodingcontainerprotocol/decodeifpresent(_:forkey:)-lc54)*