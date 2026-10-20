# type(ofProperty:)

**Framework**: Address Book  
**Kind**: method  
**Role**: Type Method

Returns the type for a given property.

**Availability**:
- macOS

## Declaration

```swift
class func type(ofProperty property: String!) -> ABPropertyType
```

```objc
+ (ABPropertyType) typeOfProperty:(NSString *) property;
```

#### Return Value

The property type of `property`.

#### Discussion

If the property does not exist, this method returns `kABErrorInProperty`.

## Parameters

- `property`: The property whose type will be returned.

## See Also

### Managing properties
- [class func addPropertiesAndTypes([AnyHashable : Any]!) -> Int](./addpropertiesandtypes%28_%29.md)
  Adds the given properties to all records of this type in the Address Book database.
- [class func removeProperties([Any]!) -> Int](./removeproperties%28_%29.md)
  Removes the given properties from all the records of this type in the Address Book database.
- [class func properties() -> [Any]!](./properties%28%29.md)
  Returns an array of the names of all the properties for this record type in the Address Book database.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbook/abgroup/type(ofproperty:))*