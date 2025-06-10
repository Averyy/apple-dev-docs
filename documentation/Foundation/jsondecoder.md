# JSONDecoder

**Framework**: Foundation  
**Kind**: class

An object that decodes instances of a data type from JSON objects.

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
class JSONDecoder
```

#### Overview

The example below shows how to decode an instance of a simple `GroceryProduct` type from a JSON object. The type adopts [`Codable`](https://developer.apple.com/documentation/Swift/Codable) so that it’s decodable using a [`JSONDecoder`](jsondecoder.md) instance.

```swift
struct GroceryProduct: Codable {
    var name: String
    var points: Int
    var description: String?
}

let json = """
{
    "name": "Durian",
    "points": 600,
    "description": "A fruit with a distinctive scent."
}
""".data(using: .utf8)!

let decoder = JSONDecoder()
let product = try decoder.decode(GroceryProduct.self, from: json)

print(product.name) // Prints "Durian"
```

## Topics

### Creating a Decoder
- [init()](jsondecoder/init.md)
  Creates a new, reusable JSON decoder with the default formatting settings and decoding strategies.
### Decoding
- [func decode<T>(T.Type, from: Data) throws -> T](jsondecoder/decode(_:from:).md)
  Returns a value of the type you specify, decoded from a JSON object.
### Customizing Decoding
- [var keyDecodingStrategy: JSONDecoder.KeyDecodingStrategy](jsondecoder/keydecodingstrategy-swift.property.md)
  A value that determines how to decode a type’s coding keys from JSON keys.
- [JSONDecoder.KeyDecodingStrategy](jsondecoder/keydecodingstrategy-swift.enum.md)
  The values that determine how to decode a type’s coding keys from JSON keys.
- [var userInfo: [CodingUserInfoKey : any Sendable]](jsondecoder/userinfo.md)
  A dictionary you use to customize the decoding process by providing contextual information.
- [var allowsJSON5: Bool](jsondecoder/allowsjson5.md)
  Specifies that decoding supports the JSON5 syntax.
- [var assumesTopLevelDictionary: Bool](jsondecoder/assumestopleveldictionary.md)
  Specifies that decoding assumes the top level of the JSON data is a dictionary, even if it doesn’t begin and end with braces.
### Decoding Dates
- [var dateDecodingStrategy: JSONDecoder.DateDecodingStrategy](jsondecoder/datedecodingstrategy-swift.property.md)
  The strategy used when decoding dates from part of a JSON object.
- [JSONDecoder.DateDecodingStrategy](jsondecoder/datedecodingstrategy-swift.enum.md)
  The strategies available for formatting dates when decoding them from JSON.
### Decoding Raw Data
- [var dataDecodingStrategy: JSONDecoder.DataDecodingStrategy](jsondecoder/datadecodingstrategy-swift.property.md)
  The strategy that a decoder uses to decode raw data.
- [JSONDecoder.DataDecodingStrategy](jsondecoder/datadecodingstrategy-swift.enum.md)
  The strategies for decoding raw data.
### Decoding Exceptional Numbers
- [var nonConformingFloatDecodingStrategy: JSONDecoder.NonConformingFloatDecodingStrategy](jsondecoder/nonconformingfloatdecodingstrategy-swift.property.md)
  The strategy used by a decoder when it encounters exceptional floating-point values.
- [JSONDecoder.NonConformingFloatDecodingStrategy](jsondecoder/nonconformingfloatdecodingstrategy-swift.enum.md)
  The strategies for encoding nonconforming floating-point numbers, also known as IEEE 754 exceptional values.
### Instance Methods
- [func decode<T, C>(T.Type, from: Data, configuration: C.Type) throws -> T](jsondecoder/decode(_:from:configuration:)-22lge.md)
- [func decode<T>(T.Type, from: Data, configuration: T.DecodingConfiguration) throws -> T](jsondecoder/decode(_:from:configuration:)-xsq1.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [NetworkDecoder](../Network/NetworkDecoder.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [TopLevelDecoder](../Combine/TopLevelDecoder.md)

## See Also

- [class JSONEncoder](jsonencoder.md)
  An object that encodes instances of a data type as JSON objects.
- [class JSONSerialization](jsonserialization.md)
  An object that converts between JSON and the equivalent Foundation objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/jsondecoder)*