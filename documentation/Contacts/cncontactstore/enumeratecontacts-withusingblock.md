# enumerateContacts(with:usingBlock:)

**Framework**: Contacts  
**Kind**: method

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

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if enumeration of all contacts matching a contact fetch request executes successfully; otherwise, [`false`](https://developer.apple.com/documentation/swift/false).

#### Discussion

This method waits until the enumeration is finished. If there are no results, the block is not called and the method returns [`true`](https://developer.apple.com/documentation/swift/true).

This method can fetch all contacts without keeping all of them at once in memory, which is expensive.

> **Note**: In Swift, this method returns `Void` and is marked with the `throws` keyword to indicate that it throws an error in cases of failure. You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [`Error Handling`](https://developer.apple.comhttps://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [`The Swift Programming Language`](https://developer.apple.comhttps://docs.swift.org/swift-book/) and [`About Imported Cocoa Error Parameters`](https://developer.apple.com/documentation/Swift/about-imported-cocoa-error-parameters).

In Swift, this method returns `Void` and is marked with the `throws` keyword to indicate that it throws an error in cases of failure. You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [`Error Handling`](https://developer.apple.comhttps://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [`The Swift Programming Language`](https://developer.apple.comhttps://docs.swift.org/swift-book/) and [`About Imported Cocoa Error Parameters`](https://developer.apple.com/documentation/Swift/about-imported-cocoa-error-parameters).

## Parameters

- `fetchRequest`: The contact fetch request that specifies the search criteria.
- `block`: Called for each contact matching the fetch request.

## See Also

- [func unifiedMeContactWithKeys(toFetch: [any CNKeyDescriptor]) throws -> CNContact](cncontactstore/unifiedmecontactwithkeys(tofetch:).md)
  Fetches the unified contact that’s the  card.
- [func unifiedContact(withIdentifier: String, keysToFetch: [any CNKeyDescriptor]) throws -> CNContact](cncontactstore/unifiedcontact(withidentifier:keystofetch:).md)
  Fetches a unified contact for the specified contact identifier.
- [func unifiedContacts(matching: NSPredicate, keysToFetch: [any CNKeyDescriptor]) throws -> [CNContact]](cncontactstore/unifiedcontacts(matching:keystofetch:).md)
  Fetches all unified contacts matching the specified predicate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contacts/cncontactstore/enumeratecontacts(with:usingblock:))*