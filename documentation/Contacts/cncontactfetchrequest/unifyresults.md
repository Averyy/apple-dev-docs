# unifyResults

**Framework**: Contacts  
**Kind**: property

A Boolean value that indicates whether to return linked contacts as unified contacts.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var unifyResults: Bool { get set }
```

#### Discussion

A unified contact is an aggregation of properties from a set of linked individual contacts. When the value of this property is [`true`](https://developer.apple.com/documentation/Swift/true), the fetch returns unified contacts; otherwise, it returns individual contacts. The default value of this property is [`true`](https://developer.apple.com/documentation/Swift/true).

## See Also

- [var mutableObjects: Bool](cncontactfetchrequest/mutableobjects.md)
  A Boolean value that indicates whether to return mutable contacts.
- [var sortOrder: CNContactSortOrder](cncontactfetchrequest/sortorder.md)
  The sort order for contacts.
- [enum CNContactSortOrder](cncontactsortorder.md)
  Indicates the sorting order for contacts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contacts/cncontactfetchrequest/unifyresults)*