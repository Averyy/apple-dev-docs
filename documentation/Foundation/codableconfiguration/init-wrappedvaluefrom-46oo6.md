# init(wrappedValue:from:)

**Framework**: Foundation  
**Kind**: init

Creates a codable configuration wrapper for the given value, using the given configuration provider type.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
init(wrappedValue: T, from configurationProvider: ConfigurationProvider.Type)
```

## Parameters

- `wrappedValue`: The underlying value to make codable, using data from the configuration provider.
- `configurationProvider`: The type of the configuration provider, which provides additional information to encode  .

## See Also

- [init(wrappedValue: T)](codableconfiguration/init(wrappedvalue:).md)
  Creates a codable configuration wrapper for the given value.
- [init(wrappedValue: T, from: KeyPath<AttributeScopes, ConfigurationProvider.Type>)](codableconfiguration/init(wrappedvalue:from:)-8mkxk.md)
  Creates a codable configuration wrapper for the given value, using given configuration provider type identified by key path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/codableconfiguration/init(wrappedvalue:from:)-46oo6)*