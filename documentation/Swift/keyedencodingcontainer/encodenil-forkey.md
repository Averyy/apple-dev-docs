# encodeNil(forKey:)

**Framework**: Swift  
**Kind**: method

Encodes a null value for the given key.

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
mutating func encodeNil(forKey key: KeyedEncodingContainer<K>.Key) throws
```

#### Discussion

> **Note**: `EncodingError.invalidValue` if a null value is invalid in the current context for this format.

## Parameters

- `key`: The key to associate the value with.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/keyedencodingcontainer/encodenil(forkey:))*