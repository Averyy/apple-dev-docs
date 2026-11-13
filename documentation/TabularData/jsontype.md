# JSONType

**Framework**: TabularData  
**Kind**: enum  
**Role**: Enumeration

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

### Numeric types
- [JSONType.integer](./jsontype/integer.md)
  An integer type.
- [JSONType.double](./jsontype/double.md)
  A double-precision floating-point type.
### Other value types
- [JSONType.boolean](./jsontype/boolean.md)
  A Boolean type.
- [JSONType.date](./jsontype/date.md)
  A date type.
- [JSONType.string](./jsontype/string.md)
  A string type.
### Container types
- [JSONType.array](./jsontype/array.md)
  An array type.
- [JSONType.object](./jsontype/object.md)
  An object type.

## Relationships

### Conforms To
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Creating a data frame from a JSON file
- [init(contentsOfJSONFile: URL, columns: [String]?, types: [String : JSONType], options: JSONReadingOptions) throws](./dataframe/init%28contentsofjsonfile,columns,types,options%29.md)
  Creates a data frame by reading a JSON file.
- [init(jsonData: Data, columns: [String]?, types: [String : JSONType], options: JSONReadingOptions) throws](./dataframe/init%28jsondata,columns,types,options%29.md)
  Creates a data frame by converting JSON data.
- [struct JSONReadingOptions](./jsonreadingoptions.md)
  A set of JSON file-reading options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/jsontype)*