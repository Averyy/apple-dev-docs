# properties()

**Framework**: Address Book  
**Kind**: method  
**Role**: Type Method

Returns an array of the names of all the properties for this record type in the Address Book database.

**Availability**:
- macOS

## Declaration

```swift
class func properties() -> [Any]!
```

```objc
+ (NSArray *) properties;
```

## See Also

### Managing properties
- [class func addPropertiesAndTypes([AnyHashable : Any]!) -> Int](./addpropertiesandtypes%28_%29.md)
  Adds the given properties to all records of this type in the Address Book database.
- [class func removeProperties([Any]!) -> Int](./removeproperties%28_%29.md)
  Removes the given properties from all the records of this type in the Address Book database.
- [class func type(ofProperty: String!) -> ABPropertyType](./type%28ofproperty%29.md)
  Returns the type for a given property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbook/abgroup/properties())*