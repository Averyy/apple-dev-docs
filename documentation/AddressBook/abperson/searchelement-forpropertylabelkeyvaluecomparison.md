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

- `property`: The name of the property to search on, such as `kABAddressProperty` or `kABLastNameProperty`. This name cannot be `nil`. For a full list of the properties, see [`Default Record Properties`](default-record-properties.md) and [`Default Person Properties`](default-person-properties.md).
- `label`: The label name for a multivalue list, such as `kABAddressHomeLabel`, `kABPhoneWorkLabel`, or a user-specified label, such as `Summer Home`. If the specified property does not have multiple values, pass `nil`. If the specified property does have multiple values, pass `nil` to search all the values. For a full list of label names, see [`Default Multivalue List Labels`](default-multivalue-list-labels.md) and [`Generic Multivalue List Labels`](generic-multivalue-list-labels.md).
- `key`: The key name for a dictionary, such as `kABAddressCityKey` or `kABAddressStreetKey`. If the specified property is not a dictionary, pass `nil`. If the specified property is a dictionary, pass `nil` to search all keys. For a full list of key names, see [`Address Keys`](address-keys.md).
- `value`: What you’re searching for. If `nil`, then the only supported value for `comparison` is `kABEqual` or `kABNotEqual`.
- `comparison`: The type of comparison to perform, such as `kABEqual` or `kABPrefixMatchCaseInsensitive`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbook/abperson/searchelement(forproperty:label:key:value:comparison:))*