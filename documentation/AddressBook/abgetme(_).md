# ABGetMe(_:)

**Framework**: Address Book  
**Kind**: func  
**Role**: Function

Returns the ABPerson object for the logged-in user.

**Availability**:
- macOS

## Declaration

```swift
func ABGetMe(_ addressBook: ABAddressBookRef!) -> Unmanaged<ABPersonRef>!
```

```c
extern ABPersonRefABGetMe(ABAddressBookRef addressBook);
```

#### Return Value

The ABPerson record that represents the logged-in user, or `NULL` if the user never specified such a record. You are responsible for retaining and releasing this object as needed.

## Parameters

- `addressBook`: The address book for the logged-in user.

## See Also

### People
- [func ABCopyArrayOfAllPeople(ABAddressBookRef!) -> Unmanaged<CFArray>!](./abcopyarrayofallpeople%28_%29.md)
  Returns an array of all the people in the Address Book database.
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
- [func ABPersonSetImageData(ABRecord!, CFData!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](./abpersonsetimagedata%28_,_,_%29.md)
  Sets the image for this person to the given data.
- [func ABSetMe(ABAddressBookRef!, ABPersonRef!)](./absetme%28_,_%29.md)
  Sets the record that represents the logged-in user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbook/abgetme(_:))*