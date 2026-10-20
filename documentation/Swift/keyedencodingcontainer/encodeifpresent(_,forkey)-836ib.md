# encodeIfPresent(_:forKey:)

**Framework**: Swift  
**Kind**: method

Encodes the given value for the given key if it is not `nil`.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
mutating func encodeIfPresent(_ value: Int128?, forKey key: Self.Key) throws
```

#### Discussion

> **Note**: `EncodingError.invalidValue` if the given value is invalid in the current context for this format.

## Parameters

- `value`: The value to encode.
- `key`: The key to associate the value with.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/keyedencodingcontainer/encodeifpresent(_:forkey:)-836ib)*