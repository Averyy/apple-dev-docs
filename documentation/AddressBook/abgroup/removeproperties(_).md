# removeProperties(_:)

**Framework**: Address Book  
**Kind**: method  
**Role**: Type Method

Removes the given properties from all the records of this type in the Address Book database.

**Availability**:
- macOS

## Declaration

```swift
class func removeProperties(_ properties: [Any]!) -> Int
```

```objc
+ (NSInteger) removeProperties:(NSArray *) properties;
```

## Return Value

The number of properties successfully removed.

## Discussion

Only custom properties can be removed. This method is not implemented.

## Parameters

- `properties`: An array of the properties to be removed.

## See Also

### Managing properties
- [class func addPropertiesAndTypes([AnyHashable : Any]!) -> Int](./addpropertiesandtypes%28_%29.md)
  Adds the given properties to all records of this type in the Address Book database.
- [class func properties() -> [Any]!](./properties%28%29.md)
  Returns an array of the names of all the properties for this record type in the Address Book database.
- [class func type(ofProperty: String!) -> ABPropertyType](./type%28ofproperty%29.md)
  Returns the type for a given property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbook/abgroup/removeproperties(_:))*