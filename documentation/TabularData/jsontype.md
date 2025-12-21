# JSONType

**Framework**: TabularData  
**Kind**: enum

Represents the value types in a JSON file.

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
enum JSONType
```

## Topics

### Enumeration Cases
- [JSONType.array](jsontype/array.md)
  An array type.
- [JSONType.boolean](jsontype/boolean.md)
  A Boolean type.
- [JSONType.date](jsontype/date.md)
  A date type.
- [JSONType.double](jsontype/double.md)
  A double-precision floating-point type.
- [JSONType.integer](jsontype/integer.md)
  An integer type.
- [JSONType.object](jsontype/object.md)
  An object type.
- [JSONType.string](jsontype/string.md)
  A string type.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [init(contentsOfJSONFile: URL, columns: [String]?, types: [String : JSONType], options: JSONReadingOptions) throws](dataframe/init(contentsofjsonfile:columns:types:options:).md)
  Creates a data frame by reading a JSON file.
- [init(jsonData: Data, columns: [String]?, types: [String : JSONType], options: JSONReadingOptions) throws](dataframe/init(jsondata:columns:types:options:).md)
  Creates a data frame by converting JSON data.
- [struct JSONReadingOptions](jsonreadingoptions.md)
  A set of JSON file-reading options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/jsontype)*