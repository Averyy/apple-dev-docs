# ABCopyArrayOfPropertiesForRecordType(_:_:)

**Framework**: Address Book  
**Kind**: func

Returns an array containing the names of all the properties for the specified record type.

**Availability**:
- macOS ?+

## Declaration

```swift
func ABCopyArrayOfPropertiesForRecordType(_ addressBook: ABAddressBookRef!, _ recordType: CFString!) -> Unmanaged<CFArray>!
```

#### Return Value

An new array containing the names (CFString objects) of all the properties in `recordType`. You are responsible for releasing this object.

## Parameters

- `addressBook`: The address book for the logged-in user.
- `recordType`: Specifies the type of record: kABGroupRecordType or kABPersonRecordType.

## See Also

- [func ABAddPropertiesAndTypes(ABAddressBookRef!, CFString!, CFDictionary!) -> CFIndex](abaddpropertiesandtypes(_:_:_:).md)
  Adds the given properties to all the records of the specified type in the Address Book database, and returns the number of properties successfully added.
- [func ABCopyLocalizedPropertyOrLabel(CFString!) -> Unmanaged<CFString>!](abcopylocalizedpropertyorlabel(_:).md)
  Returns the localized version of a built in property,label, or key.
- [func ABLocalizedPropertyOrLabel(String!) -> String!](ablocalizedpropertyorlabel(_:).md)
  Returns the localized version of a built in property, label, or key.
- [func ABRemoveProperties(ABAddressBookRef!, CFString!, CFArray!) -> CFIndex](abremoveproperties(_:_:_:).md)
  Removes the given properties from all the records of this type in the Address Book database, and returns the number of properties successfully removed.
- [func ABTypeOfProperty(ABAddressBookRef!, CFString!, CFString!) -> ABPropertyType](abtypeofproperty(_:_:_:).md)
  Returns the type of a given property for a given record.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbook/abcopyarrayofpropertiesforrecordtype(_:_:))*