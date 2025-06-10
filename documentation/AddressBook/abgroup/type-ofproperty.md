# type(ofProperty:)

**Framework**: Address Book  
**Kind**: method

Returns the type for a given property.

**Availability**:
- macOS ?+

## Declaration

```swift
class func type(ofProperty property: String!) -> ABPropertyType
```

#### Return Value

The property type of `property`.

#### Discussion

If the property does not exist, this method returns `kABErrorInProperty`.

## Parameters

- `property`: The property whose type will be returned.

## See Also

- [class func addPropertiesAndTypes([AnyHashable : Any]!) -> Int](abgroup/addpropertiesandtypes(_:).md)
  Adds the given properties to all records of this type in the Address Book database.
- [class func removeProperties([Any]!) -> Int](abgroup/removeproperties(_:).md)
  Removes the given properties from all the records of this type in the Address Book database.
- [class func properties() -> [Any]!](abgroup/properties.md)
  Returns an array of the names of all the properties for this record type in the Address Book database.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbook/abgroup/type(ofproperty:))*