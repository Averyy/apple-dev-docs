# ABAddPropertiesAndTypes(_:_:_:)

**Framework**: Address Book  
**Kind**: func

Adds the given properties to all the records of the specified type in the Address Book database, and returns the number of properties successfully added.

**Availability**:
- macOS ?+

## Declaration

```swift
func ABAddPropertiesAndTypes(_ addressBook: ABAddressBookRef!, _ recordType: CFString!, _ propertiesAndTypes: CFDictionary!) -> CFIndex
```

#### Return Value

The number of properties successfully added.

## Parameters

- `addressBook`: The address book for the logged-in user.
- `recordType`: The record type you wish to add properties to: kABGroupRecordType or kABPersonRecordType.
- `propertiesAndTypes`: A CFDictionary object containing the properties to add. In each dictionary entry, the key is a string with the property’s name, and the value is a constant with the property’s type. The property’s name must be unique. You may want to use Java-style package names for your properties, for example,   or  . The property type must be one of the constants described in  .

## See Also

- [func ABCopyArrayOfPropertiesForRecordType(ABAddressBookRef!, CFString!) -> Unmanaged<CFArray>!](abcopyarrayofpropertiesforrecordtype(_:_:).md)
  Returns an array containing the names of all the properties for the specified record type.
- [func ABCopyLocalizedPropertyOrLabel(CFString!) -> Unmanaged<CFString>!](abcopylocalizedpropertyorlabel(_:).md)
  Returns the localized version of a built in property,label, or key.
- [func ABLocalizedPropertyOrLabel(String!) -> String!](ablocalizedpropertyorlabel(_:).md)
  Returns the localized version of a built in property, label, or key.
- [func ABRemoveProperties(ABAddressBookRef!, CFString!, CFArray!) -> CFIndex](abremoveproperties(_:_:_:).md)
  Removes the given properties from all the records of this type in the Address Book database, and returns the number of properties successfully removed.
- [func ABTypeOfProperty(ABAddressBookRef!, CFString!, CFString!) -> ABPropertyType](abtypeofproperty(_:_:_:).md)
  Returns the type of a given property for a given record.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbook/abaddpropertiesandtypes(_:_:_:))*