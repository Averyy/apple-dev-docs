# removeProperties(_:)

**Framework**: Address Book  
**Kind**: method

Removes the given properties from all the records of this type in the Address Book database.

**Availability**:
- macOS ?+

## Declaration

```swift
class func removeProperties(_ properties: [Any]!) -> Int
```

#### Return Value

The number of properties successfully removed, or `-1` if an error occurs.

#### Discussion

Only custom properties can be removed. This method is not implemented.

## Parameters

- `properties`: An array of properties to remove.

## See Also

- [class func addPropertiesAndTypes([AnyHashable : Any]!) -> Int](abperson/addpropertiesandtypes(_:).md)
  Adds the given properties to all the records of this type in the Address Book database.
- [class func properties() -> [Any]!](abperson/properties.md)
  Returns an array of  the names of all the properties for the record in the Address Book database.
- [class func type(ofProperty: String!) -> ABPropertyType](abperson/type(ofproperty:).md)
  Returns the type of a given property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbook/abperson/removeproperties(_:))*