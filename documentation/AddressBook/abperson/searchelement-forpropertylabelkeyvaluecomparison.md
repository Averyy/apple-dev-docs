# searchElement(forProperty:label:key:value:comparison:)

**Framework**: Address Book  
**Kind**: method

Returns a search element object that specifies a query for records of this type.

**Availability**:
- macOS ?+

## Declaration

```swift
class func searchElement(forProperty property: String!, label: String!, key: String!, value: Any!, comparison: ABSearchComparison) -> ABSearchElement!
```

## Parameters

- `property`: The name of the property to search on, such as   or  . This name cannot be  . For a full list of the properties, see   and  .
- `label`: The label name for a multivalue list, such as  ,  , or a user-specified label, such as  . If the specified property does not have multiple values, pass  . If the specified property does have multiple values, pass   to search all the values. For a full list of label names, see   and  .
- `key`: The key name for a dictionary, such as   or  . If the specified property is not a dictionary, pass  . If the specified property is a dictionary, pass   to search all keys. For a full list of key names, see  .
- `value`: What you’re searching for. If  , then the only supported value for   is   or  .
- `comparison`: The type of comparison to perform, such as   or  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbook/abperson/searchelement(forproperty:label:key:value:comparison:))*