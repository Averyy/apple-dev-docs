# ABPersonCreateSearchElement(_:_:_:_:_:)

**Framework**: Address Book  
**Kind**: func

Returns a search element object that specifies a query for records of this type.

**Availability**:
- macOS ?+

## Declaration

```swift
func ABPersonCreateSearchElement(_ property: CFString!, _ label: CFString!, _ key: CFString!, _ value: CFTypeRef!, _ comparison: ABSearchComparison) -> Unmanaged<ABSearchElementRef>!
```

#### Return Value

A search element object that specifies a query according to the above parameters. You are responsible for releasing this object.

#### Discussion

Use the ABAddressBook [`ABCopyArrayOfMatchingRecords(_:_:)`](abcopyarrayofmatchingrecords(_:_:).md) function to actually perform the query. Also, see `ABSearchElement C` for more functions that create compound queries.

## Parameters

- `property`: The name of the property to search on. It cannot be  . For a full list of the properties, see   and Common Properties in ABRecord.
- `label`: The label name for a multi-value list. If   does not have multiple values, pass  . If   does have multiple values, pass   to search all the values.
- `key`: The key name for a dictionary. If   is not a dictionary, pass  . If   is a dictionary, pass   to search all keys.
- `value`: The value you are searching for. It cannot be 
- `comparison`: Specifies the type of comparison to perform, such as   or  . For a full list, see  .

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
- [func ABPersonCreateWithVCardRepresentation(CFData!) -> Unmanaged<ABPersonRef>!](abpersoncreatewithvcardrepresentation(_:).md)
  Returns a new ABPerson object initialized with the given data in vCard format.
- [func ABPersonSetImageData(ABRecord!, CFData!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](abpersonsetimagedata(_:_:).md)
  Sets the image for this person to the given data.
- [func ABSetMe(ABAddressBookRef!, ABPersonRef!)](absetme(_:_:).md)
  Sets the record that represents the logged-in user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbook/abpersoncreatesearchelement(_:_:_:_:_:))*