# CNContactFetchRequest

**Framework**: Contacts  
**Kind**: class

An object that defines the options to use when fetching contacts.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class CNContactFetchRequest
```

#### Overview

You need at least one contact property key to fetch a contact’s properties. Use this class with the [`enumerateContacts(with:usingBlock:)`](cncontactstore/enumeratecontacts(with:usingblock:).md) method to execute the contact fetch request.

## Topics

### Creating a Fetch Request
- [init(keysToFetch: [any CNKeyDescriptor])](cncontactfetchrequest/init(keystofetch:).md)
  Creates a fetch request for the specified keys.
- [protocol CNKeyDescriptor](cnkeydescriptor.md)
  This protocol is reserved for Contacts framework usage.
### Specifying the Search Predicate
- [var predicate: NSPredicate?](cncontactfetchrequest/predicate.md)
  The predicate to match contacts against.
### Configuring the Fetch Options
- [var mutableObjects: Bool](cncontactfetchrequest/mutableobjects.md)
  A Boolean value that indicates whether to return mutable contacts.
- [var unifyResults: Bool](cncontactfetchrequest/unifyresults.md)
  A Boolean value that indicates whether to return linked contacts as unified contacts.
- [var sortOrder: CNContactSortOrder](cncontactfetchrequest/sortorder.md)
  The sort order for contacts.
- [enum CNContactSortOrder](cncontactsortorder.md)
  Indicates the sorting order for contacts.
### Specifying the Keys to Fetch
- [var keysToFetch: [any CNKeyDescriptor]](cncontactfetchrequest/keystofetch.md)
  The properties to fetch in the returned contacts.

## Relationships

### Inherits From
- [CNFetchRequest](cnfetchrequest.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [class CNFetchRequest](cnfetchrequest.md)
  The base class for contact fetch requests.
- [class CNFetchResult](cnfetchresult.md)
  An object that represents the result of a change-history fetch request.
- [class CNSaveRequest](cnsaverequest.md)
  An object that collects the changes you want to save to the user’s contacts database.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contacts/cncontactfetchrequest)*