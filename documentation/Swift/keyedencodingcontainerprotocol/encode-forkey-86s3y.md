# encode(_:forKey:)

**Framework**: Swift  
**Kind**: method  
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
mutating func encode(_ value: UInt, forKey key: Self.Key) throws
```

#### Discussion

> **Note**: `EncodingError.invalidValue` if the given value is invalid in the current context for this format.

## Parameters

- `value`: The value to encode.
- `key`: The key to associate the value with.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/keyedencodingcontainerprotocol/encode(_:forkey:)-86s3y)*