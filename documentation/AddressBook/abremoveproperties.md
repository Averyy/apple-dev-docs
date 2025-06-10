# ABRemoveProperties(_:_:_:)

**Framework**: Address Book  
**Kind**: func

Removes the given properties from all the records of this type in the Address Book database, and returns the number of properties successfully removed.

**Availability**:
- macOS ?+

## Declaration

```swift
func ABRemoveProperties(_ addressBook: ABAddressBookRef!, _ recordType: CFString!, _ properties: CFArray!) -> CFIndex
```

#### Return Value

The number of properties successfully removed.

#### Discussion

Only custom properties can be removed. This function is not implemented.

## Parameters

- `addressBook`: The address book for the logged-in user.
- `recordType`: The name of record to remove the properties from: kABGroupRecordType or kABPersonRecordType.
- `properties`: An array of properties (CFString objects) to remove.

## See Also

- [func ABAddPropertiesAndTypes(ABAddressBookRef!, CFString!, CFDictionary!) -> CFIndex](abaddpropertiesandtypes(_:_:_:).md)
  Adds the given properties to all the records of the specified type in the Address Book database, and returns the number of properties successfully added.
- [func ABCopyArrayOfPropertiesForRecordType(ABAddressBookRef!, CFString!) -> Unmanaged<CFArray>!](abcopyarrayofpropertiesforrecordtype(_:_:).md)
  Returns an array containing the names of all the properties for the specified record type.
- [func ABCopyLocalizedPropertyOrLabel(CFString!) -> Unmanaged<CFString>!](abcopylocalizedpropertyorlabel(_:).md)
  Returns the localized version of a built in property,label, or key.
- [func ABLocalizedPropertyOrLabel(String!) -> String!](ablocalizedpropertyorlabel(_:).md)
  Returns the localized version of a built in property, label, or key.
- [func ABTypeOfProperty(ABAddressBookRef!, CFString!, CFString!) -> ABPropertyType](abtypeofproperty(_:_:_:).md)
  Returns the type of a given property for a given record.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbook/abremoveproperties(_:_:_:))*