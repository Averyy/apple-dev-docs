# encode(_:configuration:)

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
func encode<T, C>(_ value: T, configuration: C.Type) throws -> Data where T : EncodableWithConfiguration, C : EncodingConfigurationProviding, T.EncodingConfiguration == C.EncodingConfiguration
```

## See Also

- [init()](propertylistencoder/init.md)
  Creates a new, reusable property list encoder with the default formatting settings.
- [func encode<Value>(Value) throws -> Data](propertylistencoder/encode(_:).md)
  Returns a property list that represents an encoded version of the value you supply.
- [func encode<T>(T, configuration: T.EncodingConfiguration) throws -> Data](propertylistencoder/encode(_:configuration:)-5ee8q.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/propertylistencoder/encode(_:configuration:)-4biuh)*