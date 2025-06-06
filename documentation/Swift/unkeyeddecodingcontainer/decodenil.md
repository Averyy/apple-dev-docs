# decodeNil()

**Framework**: Swift  
**Kind**: method  
**Required**: Yes

Decodes a null value.

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
mutating func decodeNil() throws -> Bool
```

#### Return Value

Whether the encountered value was null.

#### Discussion

If the value is not null, does not increment currentIndex.

> **Note**: `DecodingError.valueNotFound` if there are no more values to decode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/unkeyeddecodingcontainer/decodenil())*