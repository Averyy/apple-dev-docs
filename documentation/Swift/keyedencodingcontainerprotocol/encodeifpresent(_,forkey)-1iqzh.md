# encodeIfPresent(_:forKey:)

**Framework**: Swift  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Encodes the given value for the given key if it is not `nil`.

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
mutating func encodeIfPresent(_ value: Int8?, forKey key: Self.Key) throws
```

#### Discussion

> **Throws**: `EncodingError.invalidValue` if the given value is invalid in the current context for this format.

## Parameters

- `value`: The value to encode.
- `key`: The key to associate the value with.

## Default Implementations

### KeyedEncodingContainerProtocol Implementations
- [func encodeIfPresent(Double?, forKey: Self.Key) throws](./encodeifpresent%28_,forkey%29-1g1z4.md)
  Encodes the given value for the given key if it is not `nil`.
- [func encodeIfPresent(UInt?, forKey: Self.Key) throws](./encodeifpresent%28_,forkey%29-1lv6o.md)
  Encodes the given value for the given key if it is not `nil`.
- [func encodeIfPresent(UInt16?, forKey: Self.Key) throws](./encodeifpresent%28_,forkey%29-1lz0j.md)
  Encodes the given value for the given key if it is not `nil`.
- [func encodeIfPresent(Int128?, forKey: Self.Key) throws](./encodeifpresent%28_,forkey%29-1r6ai.md)
  Encodes the given value for the given key if it is not `nil`.
- [func encodeIfPresent(UInt8?, forKey: Self.Key) throws](./encodeifpresent%28_,forkey%29-2dwj5.md)
  Encodes the given value for the given key if it is not `nil`.
- [func encodeIfPresent(UInt64?, forKey: Self.Key) throws](./encodeifpresent%28_,forkey%29-3lhrl.md)
  Encodes the given value for the given key if it is not `nil`.
- [func encodeIfPresent(Int32?, forKey: Self.Key) throws](./encodeifpresent%28_,forkey%29-4a2u7.md)
  Encodes the given value for the given key if it is not `nil`.
- [func encodeIfPresent(Float?, forKey: Self.Key) throws](./encodeifpresent%28_,forkey%29-4d89n.md)
  Encodes the given value for the given key if it is not `nil`.
- [func encodeIfPresent(UInt128?, forKey: Self.Key) throws](./encodeifpresent%28_,forkey%29-4kvt4.md)
  Encodes the given value for the given key if it is not `nil`.
- [func encodeIfPresent<T>(T?, forKey: Self.Key) throws](./encodeifpresent%28_,forkey%29-4p5p4.md)
  Encodes the given value for the given key if it is not `nil`.
- [func encodeIfPresent(String?, forKey: Self.Key) throws](./encodeifpresent%28_,forkey%29-5jh2r.md)
  Encodes the given value for the given key if it is not `nil`.
- [func encodeIfPresent(Int16?, forKey: Self.Key) throws](./encodeifpresent%28_,forkey%29-6xbjj.md)
  Encodes the given value for the given key if it is not `nil`.
- [func encodeIfPresent(Bool?, forKey: Self.Key) throws](./encodeifpresent%28_,forkey%29-7rynx.md)
  Encodes the given value for the given key if it is not `nil`.
- [func encodeIfPresent(UInt32?, forKey: Self.Key) throws](./encodeifpresent%28_,forkey%29-8i0us.md)
  Encodes the given value for the given key if it is not `nil`.
- [func encodeIfPresent(Int?, forKey: Self.Key) throws](./encodeifpresent%28_,forkey%29-8m92m.md)
  Encodes the given value for the given key if it is not `nil`.
- [func encodeIfPresent(Int64?, forKey: Self.Key) throws](./encodeifpresent%28_,forkey%29-9sui2.md)
  Encodes the given value for the given key if it is not `nil`.
- [func encodeIfPresent(Int8?, forKey: Self.Key) throws](./encodeifpresent%28_,forkey%29-yaxk.md)
  Encodes the given value for the given key if it is not `nil`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/keyedencodingcontainerprotocol/encodeifpresent(_:forkey:)-1iqzh)*