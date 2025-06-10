# ABRecord

**Framework**: Address Book  
**Kind**: typealias

A reference to an ABRecord object or any of its derivedopaque types.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS ?+

## Declaration

```swift
typealias ABRecord = CFTypeRef
```

## See Also

- [func ABGroupAddMember(ABRecord!, ABRecord!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](abgroupaddmember(_:_:).md)
  Adds a person to a group.
- [func ABGroupRemoveMember(ABRecord!, ABRecord!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](abgroupremovemember(_:_:).md)
  Removes a person from a group.
- [func ABMultiValueCreateMutable(ABPropertyType) -> Unmanaged<ABMutableMultiValue>!](abmultivaluecreatemutable().md)
  Returns a newly created mutable multi-value list object.
- [func ABPersonSetImageData(ABRecord!, CFData!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](abpersonsetimagedata(_:_:).md)
  Sets the image for this person to the given data.
- [func ABRecordRemoveValue(ABRecord!, ABPropertyID, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](abrecordremovevalue(_:_:).md)
  Removes the value of the given property.
- [func ABRecordSetValue(ABRecord!, ABPropertyID, CFTypeRef!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](abrecordsetvalue(_:_:_:).md)
  Sets the value of a given property for a record.
- [typealias ABAddressBook](abaddressbookref.md)
  A reference to an ABAddressBook object.
- [typealias ABMultiValue](abmultivalueref.md)
  A reference to an `ABMultiValue` or `ABMutableMultiValueobject`.
- [typealias ABMutableMultiValue](abmutablemultivalueref.md)
  A reference to an ABMutableMultiValue object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbook/abrecordref)*