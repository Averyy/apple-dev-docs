# KeyedEncodingContainerProtocol

**Framework**: Swift  
**Kind**: protocol

A type that provides a view into an encoder’s storage and is used to hold the encoded properties of an encodable type in a keyed manner.

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
protocol KeyedEncodingContainerProtocol
```

#### Overview

Encoders should provide types conforming to `KeyedEncodingContainerProtocol` for their format.

## Topics

### Associated Types
- [associatedtype Key : CodingKey](keyedencodingcontainerprotocol/key.md)
### Instance Properties
- [var codingPath: [any CodingKey]](keyedencodingcontainerprotocol/codingpath.md)
  The path of coding keys taken to get to this point in encoding.
### Instance Methods
- [func encode(Int16, forKey: Self.Key) throws](keyedencodingcontainerprotocol/encode(_:forkey:)-389ei.md)
  Encodes the given value for the given key.
- [func encode(UInt16, forKey: Self.Key) throws](keyedencodingcontainerprotocol/encode(_:forkey:)-44xki.md)
  Encodes the given value for the given key.
- [func encode(Float, forKey: Self.Key) throws](keyedencodingcontainerprotocol/encode(_:forkey:)-45mw2.md)
  Encodes the given value for the given key.
- [func encode(UInt64, forKey: Self.Key) throws](keyedencodingcontainerprotocol/encode(_:forkey:)-4lg54.md)
  Encodes the given value for the given key.
- [func encode(Bool, forKey: Self.Key) throws](keyedencodingcontainerprotocol/encode(_:forkey:)-4xpm2.md)
  Encodes the given value for the given key.
- [func encode(Int, forKey: Self.Key) throws](keyedencodingcontainerprotocol/encode(_:forkey:)-53bkq.md)
  Encodes the given value for the given key.
- [func encode(Int128, forKey: Self.Key) throws](keyedencodingcontainerprotocol/encode(_:forkey:)-73p1b.md)
  Encodes the given value for the given key.
- [func encode(String, forKey: Self.Key) throws](keyedencodingcontainerprotocol/encode(_:forkey:)-74l0h.md)
  Encodes the given value for the given key.
- [func encode(UInt128, forKey: Self.Key) throws](keyedencodingcontainerprotocol/encode(_:forkey:)-75dqb.md)
  Encodes the given value for the given key.
- [func encode(Int64, forKey: Self.Key) throws](keyedencodingcontainerprotocol/encode(_:forkey:)-7d8l.md)
  Encodes the given value for the given key.
- [func encode(UInt, forKey: Self.Key) throws](keyedencodingcontainerprotocol/encode(_:forkey:)-86s3y.md)
  Encodes the given value for the given key.
- [func encode(UInt8, forKey: Self.Key) throws](keyedencodingcontainerprotocol/encode(_:forkey:)-887jx.md)
  Encodes the given value for the given key.
- [func encode<T>(T, forKey: Self.Key) throws](keyedencodingcontainerprotocol/encode(_:forkey:)-8gl89.md)
  Encodes the given value for the given key.
- [func encode(UInt32, forKey: Self.Key) throws](keyedencodingcontainerprotocol/encode(_:forkey:)-8mwtj.md)
  Encodes the given value for the given key.
- [func encode(Double, forKey: Self.Key) throws](keyedencodingcontainerprotocol/encode(_:forkey:)-8xq4c.md)
  Encodes the given value for the given key.
- [func encode(Int32, forKey: Self.Key) throws](keyedencodingcontainerprotocol/encode(_:forkey:)-9hxpb.md)
  Encodes the given value for the given key.
- [func encode(Int8, forKey: Self.Key) throws](keyedencodingcontainerprotocol/encode(_:forkey:)-qjna.md)
  Encodes the given value for the given key.
- [func encodeConditional<T>(T, forKey: Self.Key) throws](keyedencodingcontainerprotocol/encodeconditional(_:forkey:).md)
  Encodes a reference to the given object only if it is encoded unconditionally elsewhere in the payload (previously, or in the future).
- [func encodeIfPresent(UInt8?, forKey: Self.Key) throws](keyedencodingcontainerprotocol/encodeifpresent(_:forkey:)-1d9dk.md)
  Encodes the given value for the given key if it is not `nil`.
- [func encodeIfPresent(Float?, forKey: Self.Key) throws](keyedencodingcontainerprotocol/encodeifpresent(_:forkey:)-1f6sg.md)
  Encodes the given value for the given key if it is not `nil`.
- [func encodeIfPresent(Int8?, forKey: Self.Key) throws](keyedencodingcontainerprotocol/encodeifpresent(_:forkey:)-1iqzh.md)
  Encodes the given value for the given key if it is not `nil`.
- [func encodeIfPresent(UInt64?, forKey: Self.Key) throws](keyedencodingcontainerprotocol/encodeifpresent(_:forkey:)-1r22b.md)
  Encodes the given value for the given key if it is not `nil`.
- [func encodeIfPresent(Bool?, forKey: Self.Key) throws](keyedencodingcontainerprotocol/encodeifpresent(_:forkey:)-2xq5p.md)
  Encodes the given value for the given key if it is not `nil`.
- [func encodeIfPresent(UInt128?, forKey: Self.Key) throws](keyedencodingcontainerprotocol/encodeifpresent(_:forkey:)-35mgj.md)
  Encodes the given value for the given key if it is not `nil`.
- [func encodeIfPresent(UInt?, forKey: Self.Key) throws](keyedencodingcontainerprotocol/encodeifpresent(_:forkey:)-3j1kl.md)
  Encodes the given value for the given key if it is not `nil`.
- [func encodeIfPresent(Int?, forKey: Self.Key) throws](keyedencodingcontainerprotocol/encodeifpresent(_:forkey:)-4axra.md)
  Encodes the given value for the given key if it is not `nil`.
- [func encodeIfPresent(Int32?, forKey: Self.Key) throws](keyedencodingcontainerprotocol/encodeifpresent(_:forkey:)-5ig1w.md)
  Encodes the given value for the given key if it is not `nil`.
- [func encodeIfPresent(Int16?, forKey: Self.Key) throws](keyedencodingcontainerprotocol/encodeifpresent(_:forkey:)-5uiig.md)
  Encodes the given value for the given key if it is not `nil`.
- [func encodeIfPresent<T>(T?, forKey: Self.Key) throws](keyedencodingcontainerprotocol/encodeifpresent(_:forkey:)-5xhse.md)
  Encodes the given value for the given key if it is not `nil`.
- [func encodeIfPresent(String?, forKey: Self.Key) throws](keyedencodingcontainerprotocol/encodeifpresent(_:forkey:)-68f89.md)
  Encodes the given value for the given key if it is not `nil`.
- [func encodeIfPresent(Double?, forKey: Self.Key) throws](keyedencodingcontainerprotocol/encodeifpresent(_:forkey:)-6xotr.md)
  Encodes the given value for the given key if it is not `nil`.
- [func encodeIfPresent(UInt16?, forKey: Self.Key) throws](keyedencodingcontainerprotocol/encodeifpresent(_:forkey:)-7b7eu.md)
  Encodes the given value for the given key if it is not `nil`.
- [func encodeIfPresent(UInt32?, forKey: Self.Key) throws](keyedencodingcontainerprotocol/encodeifpresent(_:forkey:)-837jy.md)
  Encodes the given value for the given key if it is not `nil`.
- [func encodeIfPresent(Int128?, forKey: Self.Key) throws](keyedencodingcontainerprotocol/encodeifpresent(_:forkey:)-d7xg.md)
  Encodes the given value for the given key if it is not `nil`.
- [func encodeIfPresent(Int64?, forKey: Self.Key) throws](keyedencodingcontainerprotocol/encodeifpresent(_:forkey:)-luij.md)
  Encodes the given value for the given key if it is not `nil`.
- [func encodeNil(forKey: Self.Key) throws](keyedencodingcontainerprotocol/encodenil(forkey:).md)
  Encodes a null value for the given key.
- [func nestedContainer<NestedKey>(keyedBy: NestedKey.Type, forKey: Self.Key) -> KeyedEncodingContainer<NestedKey>](keyedencodingcontainerprotocol/nestedcontainer(keyedby:forkey:).md)
  Stores a keyed encoding container for the given key and returns it.
- [func nestedUnkeyedContainer(forKey: Self.Key) -> any UnkeyedEncodingContainer](keyedencodingcontainerprotocol/nestedunkeyedcontainer(forkey:).md)
  Stores an unkeyed encoding container for the given key and returns it.
- [func superEncoder() -> any Encoder](keyedencodingcontainerprotocol/superencoder.md)
  Stores a new nested container for the default `super` key and returns a new encoder instance for encoding `super` into that container.
- [func superEncoder(forKey: Self.Key) -> any Encoder](keyedencodingcontainerprotocol/superencoder(forkey:).md)
  Stores a new nested container for the given key and returns a new encoder instance for encoding `super` into that container.

## Relationships

### Conforming Types
- [KeyedEncodingContainer](keyedencodingcontainer.md)

## See Also

- [protocol SingleValueEncodingContainer](singlevalueencodingcontainer.md)
  A container that can support the storage and direct encoding of a single non-keyed value.
- [struct KeyedEncodingContainer](keyedencodingcontainer.md)
  A concrete container that provides a view into an encoder’s storage, making the encoded properties of an encodable type accessible by keys.
- [protocol UnkeyedEncodingContainer](unkeyedencodingcontainer.md)
  A type that provides a view into an encoder’s storage and is used to hold the encoded properties of an encodable type sequentially, without keys.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/keyedencodingcontainerprotocol)*