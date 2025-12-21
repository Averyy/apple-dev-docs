# encode(_:)

**Framework**: Network  
**Kind**: method  
**Required**: Yes

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
func encode<T>(_ value: T) throws -> Data where T : Encodable
```

#### Return Value

Encoded data or throws an error if unable to encode

## Parameters

- `value`: An encodable value to encode


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/networkencoder/encode(_:))*