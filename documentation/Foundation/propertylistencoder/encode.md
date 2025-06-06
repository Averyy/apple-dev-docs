# encode(_:)

**Framework**: Foundation  
**Kind**: method

Returns a property list that represents an encoded version of the value you supply.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func encode<Value>(_ value: Value) throws -> Data where Value : Encodable
```

#### Discussion

If there’s a problem encoding the value you supply, this method throws an error based on the type of problem:

- The value fails to encode, or contains a nested value that fails to encode—this method throws the corresponding error.
- The value can’t be encoded as a property list—this method throws the [`EncodingError.invalidValue(_:_:)`](https://developer.apple.com/documentation/Swift/EncodingError/invalidValue(_:_:)) error.

## Parameters

- `value`: The value to encode as a property list.

## See Also

- [init()](propertylistencoder/init.md)
  Creates a new, reusable property list encoder with the default formatting settings.
- [func encode<T, C>(T, configuration: C.Type) throws -> Data](propertylistencoder/encode(_:configuration:)-4biuh.md)
- [func encode<T>(T, configuration: T.EncodingConfiguration) throws -> Data](propertylistencoder/encode(_:configuration:)-5ee8q.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/propertylistencoder/encode(_:))*