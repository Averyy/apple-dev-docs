# ABAddPropertiesAndTypes(_:_:_:)

**Framework**: Address Book  
**Kind**: func  
**Role**: Function

Adds the given properties to all the records of the specified type in the Address Book database, and returns the number of properties successfully added.

**Availability**:
- macOS

## Declaration

```swift
func ABAddPropertiesAndTypes(_ addressBook: ABAddressBookRef!, _ recordType: CFString!, _ propertiesAndTypes: CFDictionary!) -> CFIndex
```

```c
extern CFIndex ABAddPropertiesAndTypes(ABAddressBookRef addressBook, CFStringRef recordType, CFDictionaryRef propertiesAndTypes);
```

## Return Value

The number of properties successfully added.

## Parameters

- `addressBook`: The address book for the logged-in user.
- `recordType`: The record type you wish to add properties to: kABGroupRecordType or kABPersonRecordType.
- `propertiesAndTypes`: A CFDictionary object containing the properties to add. In each dictionary entry, the key is a string with the property’s name, and the value is a constant with the property’s type. The property’s name must be unique. You may want to use Java-style package names for your properties, for example, `"org.dogclub.dogname"` or `"com.mycompany.customerID"`. The property type must be one of the constants described in [`ABPropertyType`](./abpropertytype.md).

## See Also

### Properties
- [func ABCopyArrayOfPropertiesForRecordType(ABAddressBookRef!, CFString!) -> Unmanaged<CFArray>!](./abcopyarrayofpropertiesforrecordtype%28_,_%29.md)
  Returns an array containing the names of all the properties for the specified record type.
- [func ABCopyLocalizedPropertyOrLabel(CFString!) -> Unmanaged<CFString>!](./abcopylocalizedpropertyorlabel%28_%29.md)
  Returns the localized version of a built in property,label, or key.
- [func ABLocalizedPropertyOrLabel(String!) -> String!](./ablocalizedpropertyorlabel%28_%29.md)
  Returns the localized version of a built in property, label, or key.
- [func ABRemoveProperties(ABAddressBookRef!, CFString!, CFArray!) -> CFIndex](./abremoveproperties%28_,_,_%29.md)
  Removes the given properties from all the records of this type in the Address Book database, and returns the number of properties successfully removed.
- [func ABTypeOfProperty(ABAddressBookRef!, CFString!, CFString!) -> ABPropertyType](./abtypeofproperty%28_,_,_%29.md)
  Returns the type of a given property for a given record.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbook/abaddpropertiesandtypes(_:_:_:))*