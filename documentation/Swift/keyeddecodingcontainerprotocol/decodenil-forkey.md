# decodeNil(forKey:)

**Framework**: Swift  
**Kind**: method  
**Required**: Yes

Decodes a null value for the given key.

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
func decodeNil(forKey key: Self.Key) throws -> Bool
```

#### Return Value

Whether the encountered value was null.

#### Discussion

> **Note**: `DecodingError.keyNotFound` if `self` does not have an entry for the given key.

## Parameters

- `key`: The key that the decoded value is associated with.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/keyeddecodingcontainerprotocol/decodenil(forkey:))*