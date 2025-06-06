# decode(_:from:)

**Framework**: Foundation  
**Kind**: method

Returns a value of the specified type by decoding a property list using the default property list format.

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
func decode<T>(_ type: T.Type, from data: Data) throws -> T where T : Decodable
```

#### Discussion

If the data is not a valid property list, this method throws the [`DecodingError.dataCorrupted(_:)`](https://developer.apple.com/documentation/Swift/DecodingError/dataCorrupted(_:)) error. If a value within the property list fails to decode, this method throws the corresponding error.

## Parameters

- `type`: The type of the value to decode from the supplied property list.
- `data`: The property list to decode.

## See Also

- [init()](propertylistdecoder/init.md)
  Creates a new, reusable property list decoder.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/propertylistdecoder/decode(_:from:))*