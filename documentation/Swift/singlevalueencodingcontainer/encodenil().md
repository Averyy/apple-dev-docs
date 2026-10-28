# encodeNil()

**Framework**: Swift  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Encodes a null value.

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
mutating func encodeNil() throws
```

## Discussion

> **Throws**: `EncodingError.invalidValue` if a null value is invalid in the current context for this format.

> **Precondition**: May not be called after a previous `self.encode(_:)` call.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/singlevalueencodingcontainer/encodenil())*