# ABLocalizedPropertyOrLabel(_:)

**Framework**: Address Book  
**Kind**: func  
**Role**: Function

Returns the localized version of a built in property, label, or key.

**Availability**:
- macOS

## Declaration

```swift
func ABLocalizedPropertyOrLabel(_ propertyOrLabel: String!) -> String!
```

```c
NSString *ABLocalizedPropertyOrLabel(NSString *propertyOrLabel);
```

## Discussion

The `propertyOrLabel` argument is the property, label, or key you wish to localize. Returns `propertyOrLabel` if a localized string can not be found

## See Also

### Properties
- [func ABAddPropertiesAndTypes(ABAddressBookRef!, CFString!, CFDictionary!) -> CFIndex](./abaddpropertiesandtypes%28_,_,_%29.md)
  Adds the given properties to all the records of the specified type in the Address Book database, and returns the number of properties successfully added.
- [func ABCopyArrayOfPropertiesForRecordType(ABAddressBookRef!, CFString!) -> Unmanaged<CFArray>!](./abcopyarrayofpropertiesforrecordtype%28_,_%29.md)
  Returns an array containing the names of all the properties for the specified record type.
- [func ABCopyLocalizedPropertyOrLabel(CFString!) -> Unmanaged<CFString>!](./abcopylocalizedpropertyorlabel%28_%29.md)
  Returns the localized version of a built in property,label, or key.
- [func ABRemoveProperties(ABAddressBookRef!, CFString!, CFArray!) -> CFIndex](./abremoveproperties%28_,_,_%29.md)
  Removes the given properties from all the records of this type in the Address Book database, and returns the number of properties successfully removed.
- [func ABTypeOfProperty(ABAddressBookRef!, CFString!, CFString!) -> ABPropertyType](./abtypeofproperty%28_,_,_%29.md)
  Returns the type of a given property for a given record.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbook/ablocalizedpropertyorlabel(_:))*