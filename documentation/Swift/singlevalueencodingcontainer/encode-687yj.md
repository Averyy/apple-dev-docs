# encode(_:)

**Framework**: Swift  
**Kind**: method  
**Required**: Yes

Encodes a single value of the given type.

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
mutating func encode<T>(_ value: T) throws where T : Encodable
```

#### Discussion

> **Note**: `EncodingError.invalidValue` if the given value is invalid in the current context for this format.

`EncodingError.invalidValue` if the given value is invalid in the current context for this format.

> **Note**: May not be called after a previous `self.encode(_:)` call.

May not be called after a previous `self.encode(_:)` call.

## Parameters

- `value`: The value to encode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/singlevalueencodingcontainer/encode(_:)-687yj)*