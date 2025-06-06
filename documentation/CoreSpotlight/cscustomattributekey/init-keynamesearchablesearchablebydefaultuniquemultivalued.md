# init(keyName:searchable:searchableByDefault:unique:multiValued:)

**Framework**: Core Spotlight  
**Kind**: init

Returns a new custom attribute key with the specified name and properties.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+

## Declaration

```swift
init?(keyName: String, searchable: Bool, searchableByDefault: Bool, unique: Bool, multiValued: Bool)
```

#### Return Value

A new custom attribute key with the specified name and properties.

#### Discussion

To create custom attribute key names, it’s recommended that you use a reverse DNS format that includes your company name and does not include the period character (”.”). For example, a key name of the form `com_mycompany_myapp_mykeyname` works well.

## Parameters

- `keyName`: The name of the custom attribute for use as a key in a  . The key name must be a string that contains only ASCII characters and no punctuation other than the underscore (that is, “_”). The prefix   is reserved.
- `searchable`: A Boolean value that indicates if the attribute can be specified as a search term.
- `searchableByDefault`: A Boolean value that indicates if the attribute should be searchable by default.
- `unique`: A Boolean value that indicates if duplicate values should be treated as the same value to save storage space.
- `multiValued`: A Boolean value that indicates if the attribute is likely to have multiple values, such as arrays, associated with it.

## See Also

- [convenience init?(keyName: String)](cscustomattributekey/init(keyname:).md)
  Returns a new custom attribute key with the specified name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/cscustomattributekey/init(keyname:searchable:searchablebydefault:unique:multivalued:))*