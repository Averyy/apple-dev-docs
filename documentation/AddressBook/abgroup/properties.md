# properties()

**Framework**: Address Book  
**Kind**: method

Returns an array of the names of all the properties for this record type in the Address Book database.

**Availability**:
- macOS ?+

## Declaration

```swift
class func properties() -> [Any]!
```

## See Also

- [class func addPropertiesAndTypes([AnyHashable : Any]!) -> Int](abgroup/addpropertiesandtypes(_:).md)
  Adds the given properties to all records of this type in the Address Book database.
- [class func removeProperties([Any]!) -> Int](abgroup/removeproperties(_:).md)
  Removes the given properties from all the records of this type in the Address Book database.
- [class func type(ofProperty: String!) -> ABPropertyType](abgroup/type(ofproperty:).md)
  Returns the type for a given property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbook/abgroup/properties())*