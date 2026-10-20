# ABPersonCopyImageData(_:)

**Framework**: Address Book  
**Kind**: func  
**Role**: Function

Returns data that contains a picture of a person.

**Availability**:
- iOS 2.0+ - Deprecated in 9.0
- iPadOS 2.0+ - Deprecated in 9.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS

> **Deprecated**: use CNContact.imageData

## Declaration

*iOS, iPadOS, Mac Catalyst*

```swift
func ABPersonCopyImageData(_ person: ABRecord!) -> Unmanaged<CFData>!
```

*macOS*

```swift
func ABPersonCopyImageData(_ person: ABPersonRef!) -> Unmanaged<CFData>!
```

*iOS, iPadOS, Mac Catalyst*

```c
extern CFDataRefABPersonCopyImageData(ABRecordRef person);
```

*macOS*

```c
extern CFDataRefABPersonCopyImageData(ABPersonRef person);
```

#### Return Value

The data representing an image of `person`. You are responsible for releasing this object.

#### Discussion

The returned data is in a QuickTime-compatible format. To create an image from it, use the NSImage method [`init(data:)`](../AppKit/nsimage/init%28data%29.md).

## Parameters

- `person`: The person whose image you wish to obtain.

## See Also

### People
- [func ABCopyArrayOfAllPeople(ABAddressBookRef!) -> Unmanaged<CFArray>!](./abcopyarrayofallpeople%28_%29.md)
  Returns an array of all the people in the Address Book database.
- [func ABGetMe(ABAddressBookRef!) -> Unmanaged<ABPersonRef>!](./abgetme%28_%29.md)
  Returns the ABPerson object for the logged-in user.
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

*[View on Apple Developer](https://developer.apple.com/documentation/addressbook/abpersoncopyimagedata(_:))*