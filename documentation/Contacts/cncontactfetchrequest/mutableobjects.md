# mutableObjects

**Framework**: Contacts  
**Kind**: property

A Boolean value that indicates whether to return mutable contacts.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var mutableObjects: Bool { get set }
```

#### Discussion

When the value of this property is [`true`](https://developer.apple.com/documentation/Swift/true), the fetch returns [`CNMutableContact`](cnmutablecontact.md) objects; otherwise it returns [`CNContact`](cncontact.md) objects. The default value of this property is [`false`](https://developer.apple.com/documentation/Swift/false).

## See Also

- [var unifyResults: Bool](cncontactfetchrequest/unifyresults.md)
  A Boolean value that indicates whether to return linked contacts as unified contacts.
- [var sortOrder: CNContactSortOrder](cncontactfetchrequest/sortorder.md)
  The sort order for contacts.
- [enum CNContactSortOrder](cncontactsortorder.md)
  Indicates the sorting order for contacts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contacts/cncontactfetchrequest/mutableobjects)*