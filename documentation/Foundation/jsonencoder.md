# JSONEncoder

**Framework**: Foundation  
**Kind**: class

An object that encodes instances of a data type as JSON objects.

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
class JSONEncoder
```

## Mentions

- [Uploading data to a website](uploading-data-to-a-website.md)
- [Encoding and Decoding Custom Types](encoding-and-decoding-custom-types.md)

#### Overview

The example below shows how to encode an instance of a simple `GroceryProduct` type from a JSON object. The type adopts [`Codable`](https://developer.apple.com/documentation/Swift/Codable) so that it’s encodable as JSON using a [`JSONEncoder`](jsonencoder.md) instance.

```swift
struct GroceryProduct: Codable {
    var name: String
    var points: Int
    var description: String?
}

let pear = GroceryProduct(name: "Pear", points: 250, description: "A ripe pear.")

let encoder = JSONEncoder()
encoder.outputFormatting = .prettyPrinted

let data = try encoder.encode(pear)
print(String(data: data, encoding: .utf8)!)

/* Prints:
 {
   "name" : "Pear",
   "points" : 250,
   "description" : "A ripe pear."
 }
*/
```

## Topics

### First Steps
- [init()](jsonencoder/init.md)
  Creates a new, reusable JSON encoder with the default formatting settings and encoding strategies.
- [func encode<T>(T) throws -> Data](jsonencoder/encode(_:).md)
  Returns a JSON-encoded representation of the value you supply.
### Customizing Encoding
- [var outputFormatting: JSONEncoder.OutputFormatting](jsonencoder/outputformatting-swift.property.md)
  A value that determines the readability, size, and element order of the encoded JSON object.
- [JSONEncoder.OutputFormatting](jsonencoder/outputformatting-swift.struct.md)
  The output formatting options that determine the readability, size, and element order of an encoded JSON object.
- [var keyEncodingStrategy: JSONEncoder.KeyEncodingStrategy](jsonencoder/keyencodingstrategy-swift.property.md)
  A value that determines how to encode a  type’s coding keys as JSON keys.
- [JSONEncoder.KeyEncodingStrategy](jsonencoder/keyencodingstrategy-swift.enum.md)
  The values that determine how to encode a type’s coding keys as JSON keys.
- [var userInfo: [CodingUserInfoKey : any Sendable]](jsonencoder/userinfo.md)
  A dictionary you use to customize the encoding process by providing contextual information.
### Encoding Dates
- [var dateEncodingStrategy: JSONEncoder.DateEncodingStrategy](jsonencoder/dateencodingstrategy-swift.property.md)
  The strategy used when encoding dates as part of a JSON object.
- [JSONEncoder.DateEncodingStrategy](jsonencoder/dateencodingstrategy-swift.enum.md)
  The formatting strategies available for formatting dates when encoding a date as JSON.
### Encoding Raw Data
- [var dataEncodingStrategy: JSONEncoder.DataEncodingStrategy](jsonencoder/dataencodingstrategy-swift.property.md)
  The strategy that an encoder uses to encode raw data.
- [JSONEncoder.DataEncodingStrategy](jsonencoder/dataencodingstrategy-swift.enum.md)
  The strategies for encoding raw data.
### Encoding Exceptional Numbers
- [var nonConformingFloatEncodingStrategy: JSONEncoder.NonConformingFloatEncodingStrategy](jsonencoder/nonconformingfloatencodingstrategy-swift.property.md)
  The strategy used by an encoder when it encounters exceptional floating-point values.
- [JSONEncoder.NonConformingFloatEncodingStrategy](jsonencoder/nonconformingfloatencodingstrategy-swift.enum.md)
  The strategies for encoding nonconforming floating-point numbers, also known as IEEE 754 exceptional values.
### Instance Methods
- [func encode<T, C>(T, configuration: C.Type) throws -> Data](jsonencoder/encode(_:configuration:)-721tx.md)
- [func encode<T>(T, configuration: T.EncodingConfiguration) throws -> Data](jsonencoder/encode(_:configuration:)-8l39i.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Sendable](../Swift/Sendable.md)
- [TopLevelEncoder](../Combine/TopLevelEncoder.md)

## See Also

- [class JSONDecoder](jsondecoder.md)
  An object that decodes instances of a data type from JSON objects.
- [class JSONSerialization](jsonserialization.md)
  An object that converts between JSON and the equivalent Foundation objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/jsonencoder)*