# encode(_:)

**Framework**: Combine  
**Kind**: method  
**Required**: Yes

Encodes an instance of the indicated type.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
func encode<T>(_ value: T) throws -> Self.Output where T : Encodable
```

## Parameters

- `value`: The instance to encode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/toplevelencoder/encode(_:))*