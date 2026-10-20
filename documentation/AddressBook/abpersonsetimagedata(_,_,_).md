# ABPersonSetImageData(_:_:_:)

**Framework**: Address Book  
**Kind**: func  
**Role**: Function

Sets the image for this person to the given data.

**Availability**:
- iOS 2.0+ - Deprecated in 9.0
- iPadOS 2.0+ - Deprecated in 9.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS

> **Deprecated**: use CNMutableContact.imageData

## Declaration

*iOS, iPadOS, Mac Catalyst*

```swift
func ABPersonSetImageData(_ person: ABRecord!, _ imageData: CFData!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool
```

*macOS*

```swift
func ABPersonSetImageData(_ person: ABPersonRef!, _ imageData: CFData!) -> Bool
```

*iOS, iPadOS, Mac Catalyst*

```c
extern bool ABPersonSetImageData(ABRecordRef person, CFDataRef imageData, CFErrorRef*error);
```

*macOS*

```c
extern bool ABPersonSetImageData(ABPersonRef person, CFDataRef imageData);
```

#### Return Value

`true` if successful, `false` otherwise.

## Parameters

- `person`: The person whose image data you wish to set.
- `imageData`: The image data to use as the image for `person`.

## See Also

### People
- [func ABCopyArrayOfAllPeople(ABAddressBookRef!) -> Unmanaged<CFArray>!](./abcopyarrayofallpeople%28_%29.md)
  Returns an array of all the people in the Address Book database.
- [func ABGetMe(ABAddressBookRef!) -> Unmanaged<ABPersonRef>!](./abgetme%28_%29.md)
  Returns the ABPerson object for the logged-in user.
- [func ABPersonCopyImageData(ABRecord!) -> Unmanaged<CFData>!](./abpersoncopyimagedata%28_%29.md)
  Returns data that contains a picture of a person.
- [func ABPersonCopyParentGroups(ABPersonRef!) -> Unmanaged<CFArray>!](./abpersoncopyparentgroups%28_%29.md)
  Returns an array of groups that a person belongs to.
- [func ABPersonCopyVCardRepresentation(ABPersonRef!) -> Unmanaged<CFData>!](./abpersoncopyvcardrepresentation%28_%29.md)
  Returns the vCard representation of the person as a data object in vCard format.
- [func ABPersonCreate() -> Unmanaged<ABRecord>!](./abpersoncreate%28%29.md)
  Returns a newly created person object.
- [func ABPersonCreateSearchElement(CFString!, CFString!, CFString!, CFTypeRef!, ABSearchComparison) -> Unmanaged<ABSearchElementRef>!](./abpersoncreatesearchelement%28_,_,_,_,_%29.md)
  Returns a search element object that specifies a query for records of this type.
- [func ABPersonCreateWithVCardRepresentation(CFData!) -> Unmanaged<ABPersonRef>!](./abpersoncreatewithvcardrepresentation%28_%29.md)
  Returns a new ABPerson object initialized with the given data in vCard format.
- [func ABSetMe(ABAddressBookRef!, ABPersonRef!)](./absetme%28_,_%29.md)
  Sets the record that represents the logged-in user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbook/abpersonsetimagedata(_:_:_:))*