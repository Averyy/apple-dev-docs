# init(contentsOfJSONFile:columns:types:options:)

**Framework**: TabularData  
**Kind**: init

Creates a data frame by reading a JSON file.

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
init(contentsOfJSONFile url: URL, columns: [String]? = nil, types: [String : JSONType] = [:], options: JSONReadingOptions = .init()) throws
```

#### Discussion

The JSON file should contain a sequence of objects where each object contains a value for every column name. Here’s an example with two columns “id” and “name”:

```None
[
  {"id": 1, "name": "foo"},
  {"id": 2, "name": "bar"},
]
```

> **Note**: A `JSONReadingError` instance.

A `JSONReadingError` instance.

## Parameters

- `url`: A URL to a JSON file.
- `columns`: An array of column names; Set to   to use every column in the JSON file.
- `types`: A dictionary of column names and their JSON types.   The data frame infers the types for column names that aren’t in the dictionary.
- `options`: The options that instruct how the data frame reads the JSON file.

## See Also

- [init(jsonData: Data, columns: [String]?, types: [String : JSONType], options: JSONReadingOptions) throws](dataframe/init(jsondata:columns:types:options:).md)
  Creates a data frame by converting JSON data.
- [enum JSONType](jsontype.md)
  Represents the value types in a JSON file.
- [struct JSONReadingOptions](jsonreadingoptions.md)
  A set of JSON file-reading options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/dataframe/init(contentsofjsonfile:columns:types:options:))*