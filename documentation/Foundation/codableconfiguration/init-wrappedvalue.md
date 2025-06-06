# init(wrappedValue:)

**Framework**: Foundation  
**Kind**: init

Creates a codable configuration wrapper for the given value.

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
init(wrappedValue: T)
```

#### Discussion

This initializer doesn’t take a `ConfigurationProvider.Type` parameter. As a result, it won’t compile unless the compiler can imply the provider type through other means, such as a generic expression like `@CodableConfiguration<AttributedString, FoundationAttributes>`.

For clarity, use this type’s other initializers, which take the configuration provider type as an explicit parameter.

## Parameters

- `wrappedValue`: The underlying value to make codable.

## See Also

- [init(wrappedValue: T, from: ConfigurationProvider.Type)](codableconfiguration/init(wrappedvalue:from:)-46oo6.md)
  Creates a codable configuration wrapper for the given value, using the given configuration provider type.
- [init(wrappedValue: T, from: KeyPath<AttributeScopes, ConfigurationProvider.Type>)](codableconfiguration/init(wrappedvalue:from:)-8mkxk.md)
  Creates a codable configuration wrapper for the given value, using given configuration provider type identified by key path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/codableconfiguration/init(wrappedvalue:))*