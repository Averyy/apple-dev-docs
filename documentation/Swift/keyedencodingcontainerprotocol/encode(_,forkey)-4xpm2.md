# encode(_:forKey:)

**Framework**: Swift  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Encodes the given value for the given key.

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
mutating func encode(_ value: Bool, forKey key: Self.Key) throws
```

#### Discussion

> **Throws**: `EncodingError.invalidValue` if the given value is invalid in the current context for this format.

## Parameters

- `value`: The value to encode.
- `key`: The key to associate the value with.

## Default Implementations

### KeyedEncodingContainerProtocol Implementations
- [func encode(Int128, forKey: Self.Key) throws](./encode%28_,forkey%29-5igzg.md)
  Encodes the given value for the given key.
- [func encode(UInt128, forKey: Self.Key) throws](./encode%28_,forkey%29-7lntx.md)
  Encodes the given value for the given key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/keyedencodingcontainerprotocol/encode(_:forkey:)-4xpm2)*