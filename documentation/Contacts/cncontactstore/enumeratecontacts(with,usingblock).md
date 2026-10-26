# enumerateContacts(with:usingBlock:)

**Framework**: Contacts  
**Kind**: method  
**Role**: Instance Method

Returns a Boolean value that indicates whether the enumeration of all contacts matching a contact fetch request executes successfully.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func enumerateContacts(with fetchRequest: CNContactFetchRequest, usingBlock block: (CNContact, UnsafeMutablePointer<ObjCBool>) -> Void) throws
```

```objc
- (BOOL) enumerateContactsWithFetchRequest:(CNContactFetchRequest *) fetchRequest error:(NSError **) error usingBlock:(void (^)(CNContact *contact, BOOL *stop)) block;
```

#### Return Value

[`true`](../../Swift/true.md) if enumeration of all contacts matching a contact fetch request executes successfully; otherwise, [`false`](../../Swift/false.md).

#### Discussion

This method waits until the enumeration is finished. If there are no results, the block is not called and the method returns [`true`](../../Swift/true.md).

This method can fetch all contacts without keeping all of them at once in memory, which is expensive.

> **Handling Errors in Swift**: In Swift, this method returns `Void` and is marked with the `throws` keyword to indicate that it throws an error in cases of failure. You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [Error Handling](https://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [The Swift Programming Language](https://docs.swift.org/swift-book/) and [About Imported Cocoa Error Parameters](../../Swift/about-imported-cocoa-error-parameters.md).

## Parameters

- `fetchRequest`: The contact fetch request that specifies the search criteria.
- `block`: Called for each contact matching the fetch request.

## See Also

### Fetching contacts
- [func unifiedMeContactWithKeys(toFetch: [any CNKeyDescriptor]) throws -> CNContact](./unifiedmecontactwithkeys%28tofetch%29.md)
  Fetches the unified contact that’s the *me* card.
- [func unifiedContact(withIdentifier: String, keysToFetch: [any CNKeyDescriptor]) throws -> CNContact](./unifiedcontact%28withidentifier,keystofetch%29.md)
  Fetches a unified contact for the specified contact identifier.
- [func unifiedContacts(matching: NSPredicate, keysToFetch: [any CNKeyDescriptor]) throws -> [CNContact]](./unifiedcontacts%28matching,keystofetch%29.md)
  Fetches all unified contacts matching the specified predicate.
- [- enumeratorForContactFetchRequest:error:](./enumeratorforcontactfetchrequest_error_.md)
  Enumerates a contact fetch request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contacts/cncontactstore/enumeratecontacts(with:usingblock:))*