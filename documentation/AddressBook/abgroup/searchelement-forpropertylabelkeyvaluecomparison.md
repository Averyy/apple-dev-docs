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

- `property`: The name of the property to search on. It cannot be  . For a full list of the properties, see    and  .
- `label`: The label name for a multivalue list. If   does not have multiple values, pass  . If   does have multiple values, pass   to search all the values. By default,   records don’t contain any multivalue list properties.
- `key`: The key name for a dictionary. Pass   if   is not a dictionary. If   is a dictionary, pass   to search all keys. By default,   records don’t contain any properties that are dictionaries.
- `value`: What you’re searching for. If  , the only supported value for   is   or  .
- `comparison`: The type of comparison to perform and is an  , such as   or  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbook/abgroup/searchelement(forproperty:label:key:value:comparison:))*