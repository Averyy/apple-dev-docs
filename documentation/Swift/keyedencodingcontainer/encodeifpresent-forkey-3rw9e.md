# encodeIfPresent(_:forKey:)

**Framework**: Swift  
**Kind**: method

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
mutating func encodeIfPresent(_ value: UInt32?, forKey key: KeyedEncodingContainer<K>.Key) throws
```

#### Discussion

> **Note**: `EncodingError.invalidValue` if the given value is invalid in the current context for this format.

`EncodingError.invalidValue` if the given value is invalid in the current context for this format.

## Parameters

- `value`: The value to encode.
- `key`: The key to associate the value with.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/keyedencodingcontainer/encodeifpresent(_:forkey:)-3rw9e)*