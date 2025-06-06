# type(ofProperty:)

**Framework**: Address Book  
**Kind**: method

Returns the type of a given property.

**Availability**:
- macOS ?+

## Declaration

```swift
class func type(ofProperty property: String!) -> ABPropertyType
```

#### Discussion

If the property does not exist, this method returns `kABErrorInProperty`.

## Parameters

- `property`: The property whose type will be returned.

## See Also

- [class func addPropertiesAndTypes([AnyHashable : Any]!) -> Int](abperson/addpropertiesandtypes(_:).md)
  Adds the given properties to all the records of this type in the Address Book database.
- [class func removeProperties([Any]!) -> Int](abperson/removeproperties(_:).md)
  Removes the given properties from all the records of this type in the Address Book database.
- [class func properties() -> [Any]!](abperson/properties.md)
  Returns an array of  the names of all the properties for the record in the Address Book database.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbook/abperson/type(ofproperty:))*