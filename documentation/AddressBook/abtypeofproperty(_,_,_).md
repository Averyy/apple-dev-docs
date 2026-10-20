# ABTypeOfProperty(_:_:_:)

**Framework**: Address Book  
**Kind**: func  
**Role**: Function

Returns the type of a given property for a given record.

**Availability**:
- macOS

## Declaration

```swift
func ABTypeOfProperty(_ addressBook: ABAddressBookRef!, _ recordType: CFString!, _ property: CFString!) -> ABPropertyType
```

```c
extern ABPropertyType ABTypeOfProperty(ABAddressBookRef addressBook, CFStringRef recordType, CFStringRef property);
```

#### Return Value

The type of `property` as defined in [`ABPropertyType`](./abpropertytype.md). If `property` does not exist in `recordType`, this function returns [`kABErrorInProperty`](./kaberrorinproperty.md).

## Parameters

- `addressBook`: The address book for the logged-in user.
- `recordType`: The record type that contains `property`: kABGroupRecordType or kABPersonRecordType.
- `property`: The property whose type you wish to obtain.

## See Also

### Properties
- [func ABAddPropertiesAndTypes(ABAddressBookRef!, CFString!, CFDictionary!) -> CFIndex](./abaddpropertiesandtypes%28_,_,_%29.md)
  Adds the given properties to all the records of the specified type in the Address Book database, and returns the number of properties successfully added.
- [func ABCopyArrayOfPropertiesForRecordType(ABAddressBookRef!, CFString!) -> Unmanaged<CFArray>!](./abcopyarrayofpropertiesforrecordtype%28_,_%29.md)
  Returns an array containing the names of all the properties for the specified record type.
- [func ABCopyLocalizedPropertyOrLabel(CFString!) -> Unmanaged<CFString>!](./abcopylocalizedpropertyorlabel%28_%29.md)
  Returns the localized version of a built in property,label, or key.
- [func ABLocalizedPropertyOrLabel(String!) -> String!](./ablocalizedpropertyorlabel%28_%29.md)
  Returns the localized version of a built in property, label, or key.
- [func ABRemoveProperties(ABAddressBookRef!, CFString!, CFArray!) -> CFIndex](./abremoveproperties%28_,_,_%29.md)
  Removes the given properties from all the records of this type in the Address Book database, and returns the number of properties successfully removed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbook/abtypeofproperty(_:_:_:))*