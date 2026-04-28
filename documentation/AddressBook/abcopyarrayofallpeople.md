# ABCopyArrayOfAllPeople(_:)

**Framework**: Address Book  
**Kind**: func

Returns an array of all the people in the Address Book database.

**Availability**:
- macOS ?+

## Declaration

```swift
func ABCopyArrayOfAllPeople(_ addressBook: ABAddressBookRef!) -> Unmanaged<CFArray>!
```

#### Return Value

An array of ABPerson objects representing all the people in the Address Book database. If the database does not contain any people, the function returns an empty array. You are responsible for releasing this object.

## Parameters

- `addressBook`: The address book for the logged-in user.

## See Also

- [func ABGetMe(ABAddressBookRef!) -> Unmanaged<ABPersonRef>!](abgetme(_:).md)
  Returns the ABPerson object for the logged-in user.
- [func ABPersonCopyImageData(ABRecord!) -> Unmanaged<CFData>!](abpersoncopyimagedata(_:).md)
  Returns data that contains a picture of a person.
- [func ABPersonCopyParentGroups(ABPersonRef!) -> Unmanaged<CFArray>!](abpersoncopyparentgroups(_:).md)
  Returns an array of groups that a person belongs to.
- [func ABPersonCopyVCardRepresentation(ABPersonRef!) -> Unmanaged<CFData>!](abpersoncopyvcardrepresentation(_:).md)
  Returns the vCard representation of the person as a data object in vCard format.
- [func ABPersonCreate() -> Unmanaged<ABRecord>!](abpersoncreate().md)
  Returns a newly created person object.
- [func ABPersonCreateSearchElement(CFString!, CFString!, CFString!, CFTypeRef!, ABSearchComparison) -> Unmanaged<ABSearchElementRef>!](abpersoncreatesearchelement(_:_:_:_:_:).md)
  Returns a search element object that specifies a query for records of this type.
- [func ABPersonCreateWithVCardRepresentation(CFData!) -> Unmanaged<ABPersonRef>!](abpersoncreatewithvcardrepresentation(_:).md)
  Returns a new ABPerson object initialized with the given data in vCard format.
- [func ABPersonSetImageData(ABRecord!, CFData!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](abpersonsetimagedata(_:_:).md)
  Sets the image for this person to the given data.
- [func ABSetMe(ABAddressBookRef!, ABPersonRef!)](absetme(_:_:).md)
  Sets the record that represents the logged-in user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbook/abcopyarrayofallpeople(_:))*