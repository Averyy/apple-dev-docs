# ABPersonSetImageData(_:_:_:)

**Framework**: Address Book  
**Kind**: func

Sets the image for this person to the given data.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS ?+

## Declaration

```swift
func ABPersonSetImageData(_ person: ABRecord!, _ imageData: CFData!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool
```

#### Return Value

`true` if successful, `false` otherwise.

## Parameters

- `person`: The person whose image data you wish to set.
- `imageData`: The image data to use as the image for  .

## See Also

- [func ABCopyArrayOfAllPeople(ABAddressBookRef!) -> Unmanaged<CFArray>!](abcopyarrayofallpeople(_:).md)
  Returns an array of all the people in the Address Book database.
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
- [func ABSetMe(ABAddressBookRef!, ABPersonRef!)](absetme(_:_:).md)
  Sets the record that represents the logged-in user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbook/abpersonsetimagedata(_:_:))*