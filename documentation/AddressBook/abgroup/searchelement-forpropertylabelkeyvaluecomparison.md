# searchElement(forProperty:label:key:value:comparison:)

**Framework**: Address Book  
**Kind**: method

Returns a search element object that searches for records of this type.

**Availability**:
- macOS ?+

## Declaration

```swift
class func searchElement(forProperty property: String!, label: String!, key: String!, value: Any!, comparison: ABSearchComparison) -> ABSearchElement!
```

## Parameters

- `property`: The name of the property to search on. It cannot be `nil`. For a full list of the properties, see  [`Default Record Properties`](default-record-properties.md) and [`Default Group Properties`](default-group-properties.md).
- `label`: The label name for a multivalue list. If `property` does not have multiple values, pass `nil`. If `property` does have multiple values, pass `nil` to search all the values. By default, `ABGroup` records don’t contain any multivalue list properties.
- `key`: The key name for a dictionary. Pass `nil` if `property` is not a dictionary. If `property` is a dictionary, pass `nil` to search all keys. By default, `ABGroup` records don’t contain any properties that are dictionaries.
- `value`: What you’re searching for. If `nil`, the only supported value for `comparison` is `kABEqual` or `kABNotEqual`.
- `comparison`: The type of comparison to perform and is an [`ABSearchComparison`](absearchcomparison.md), such as `kABEqual` or `kABPrefixMatchCaseInsensitive`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbook/abgroup/searchelement(forproperty:label:key:value:comparison:))*