# decode(_:from:format:configuration:)

**Framework**: Foundation  
**Kind**: method

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
func decode<T>(_ type: T.Type, from data: Data, format: inout PropertyListDecoder.PropertyListFormat, configuration: T.DecodingConfiguration) throws -> T where T : DecodableWithConfiguration
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/propertylistdecoder/decode(_:from:format:configuration:)-1frbk)*