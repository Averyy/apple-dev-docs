# ABCopyLocalizedPropertyOrLabel(_:)

**Framework**: Address Book  
**Kind**: func

Returns the localized version of a built in property,label, or key.

**Availability**:
- macOS ?+

## Declaration

```swift
func ABCopyLocalizedPropertyOrLabel(_ labelOrProperty: CFString!) -> Unmanaged<CFString>!
```

#### Return Value

The localized versionof `propertyOrLabel`, or `propertyOrLabel` ifa localized string can not be found. You are responsible for releasingthis object.

## Parameters

- `labelOrProperty`: The property, label, or key to be localized.

## See Also

- [func ABAddPropertiesAndTypes(ABAddressBookRef!, CFString!, CFDictionary!) -> CFIndex](abaddpropertiesandtypes(_:_:_:).md)
  Adds the given properties to all the records of the specified type in the Address Book database, and returns the number of properties successfully added.
- [func ABCopyArrayOfPropertiesForRecordType(ABAddressBookRef!, CFString!) -> Unmanaged<CFArray>!](abcopyarrayofpropertiesforrecordtype(_:_:).md)
  Returns an array containing the names of all the properties for the specified record type.
- [func ABLocalizedPropertyOrLabel(String!) -> String!](ablocalizedpropertyorlabel(_:).md)
  Returns the localized version of a built in property, label, or key.
- [func ABRemoveProperties(ABAddressBookRef!, CFString!, CFArray!) -> CFIndex](abremoveproperties(_:_:_:).md)
  Removes the given properties from all the records of this type in the Address Book database, and returns the number of properties successfully removed.
- [func ABTypeOfProperty(ABAddressBookRef!, CFString!, CFString!) -> ABPropertyType](abtypeofproperty(_:_:_:).md)
  Returns the type of a given property for a given record.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbook/abcopylocalizedpropertyorlabel(_:))*