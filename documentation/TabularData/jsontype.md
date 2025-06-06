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

### Operators
- [static func == (JSONType, JSONType) -> Bool](jsontype/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
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
### Instance Properties
- [var hashValue: Int](jsontype/hashvalue.md)
  The hash value.
### Instance Methods
- [func hash(into: inout Hasher)](jsontype/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [Equatable Implementations](jsontype/equatable-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [init(contentsOfJSONFile: URL, columns: [String]?, types: [String : JSONType], options: JSONReadingOptions) throws](dataframe/init(contentsofjsonfile:columns:types:options:).md)
  Creates a data frame by reading a JSON file.
- [init(jsonData: Data, columns: [String]?, types: [String : JSONType], options: JSONReadingOptions) throws](dataframe/init(jsondata:columns:types:options:).md)
  Creates a data frame by converting JSON data.
- [struct JSONReadingOptions](jsonreadingoptions.md)
  A set of JSON file-reading options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/jsontype)*