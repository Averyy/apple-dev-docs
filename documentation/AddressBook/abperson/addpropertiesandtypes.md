# addPropertiesAndTypes(_:)

**Framework**: Address Book  
**Kind**: method

Adds the given properties to all the records of this type in the Address Book database.

**Availability**:
- macOS ?+

## Declaration

```swift
class func addPropertiesAndTypes(_ properties: [AnyHashable : Any]!) -> Int
```

#### Return Value

The number of properties successfully added, or `-1` if an error occurs.

#### Discussion

In each dictionary entry, the key is a string with the property’s name, and the value is a constant with the property’s type. The property’s name must be unique. You may want to use Java-style package names for your properties, for example, `org.dogclub.dogname` or `com.mycompany.customerID`. The property type must be one of the constants described in [`Property Types`](property_types.md).

## Parameters

- `properties`: A dictionary of properties to add, and their types.

## See Also

- [class func removeProperties([Any]!) -> Int](abperson/removeproperties(_:).md)
  Removes the given properties from all the records of this type in the Address Book database.
- [class func properties() -> [Any]!](abperson/properties.md)
  Returns an array of  the names of all the properties for the record in the Address Book database.
- [class func type(ofProperty: String!) -> ABPropertyType](abperson/type(ofproperty:).md)
  Returns the type of a given property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbook/abperson/addpropertiesandtypes(_:))*