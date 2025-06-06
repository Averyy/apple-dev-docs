# unifiedContacts(matching:keysToFetch:)

**Framework**: Contacts  
**Kind**: method

Fetches all unified contacts matching the specified predicate.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func unifiedContacts(matching predicate: NSPredicate, keysToFetch keys: [any CNKeyDescriptor]) throws -> [CNContact]
```

#### Return Value

An array of [`CNContact`](cncontact.md) objects matching the predicate.

#### Discussion

If the system doesn’t find any matches, this method returns an empty array (or `nil` in case of error). Use only the predicates from the [`CNContact`](cncontact.md) class predicates. This method doesn’t support compound predicates. Due to unification, the returned contacts may have different identifiers than you specify. To fetch all contacts, use [`enumerateContacts(with:usingBlock:)`](cncontactstore/enumeratecontacts(with:usingblock:).md).

To include [`CNContactNoteKey`](cncontactnotekey.md) in the array of keys in iOS, add the [`com.apple.developer.contacts.notes`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.contacts.notes) entitlement to your app. The entitlement requires permission from Apple to use, and you can’t publicly distribute your app until you have permission to use it. For more information about adding the entitlement and getting permission, see [`com.apple.developer.contacts.notes`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.contacts.notes).

> **Note**: In Swift, this method returns a nonoptional result and is marked with the `throws` keyword to indicate that it throws an error in cases of failure. You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [`Error Handling`](https://developer.apple.comhttps://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [`The Swift Programming Language`](https://developer.apple.comhttps://docs.swift.org/swift-book/) and [`About Imported Cocoa Error Parameters`](https://developer.apple.com/documentation/Swift/about-imported-cocoa-error-parameters).

In Swift, this method returns a nonoptional result and is marked with the `throws` keyword to indicate that it throws an error in cases of failure. You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [`Error Handling`](https://developer.apple.comhttps://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [`The Swift Programming Language`](https://developer.apple.comhttps://docs.swift.org/swift-book/) and [`About Imported Cocoa Error Parameters`](https://developer.apple.com/documentation/Swift/about-imported-cocoa-error-parameters).

## Parameters

- `predicate`: The predicate to match against.
- `keys`: The properties to fetch in the returned   objects. Fetch only the properties that your app uses. You can combine contact keys and contact key descriptors.

## See Also

- [func enumerateContacts(with: CNContactFetchRequest, usingBlock: (CNContact, UnsafeMutablePointer<ObjCBool>) -> Void) throws](cncontactstore/enumeratecontacts(with:usingblock:).md)
  Returns a Boolean value that indicates whether the enumeration of all contacts matching a contact fetch request executes successfully.
- [func unifiedMeContactWithKeys(toFetch: [any CNKeyDescriptor]) throws -> CNContact](cncontactstore/unifiedmecontactwithkeys(tofetch:).md)
  Fetches the unified contact that’s the  card.
- [func unifiedContact(withIdentifier: String, keysToFetch: [any CNKeyDescriptor]) throws -> CNContact](cncontactstore/unifiedcontact(withidentifier:keystofetch:).md)
  Fetches a unified contact for the specified contact identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contacts/cncontactstore/unifiedcontacts(matching:keystofetch:))*