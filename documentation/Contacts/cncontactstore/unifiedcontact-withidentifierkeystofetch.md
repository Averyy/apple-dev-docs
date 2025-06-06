# unifiedContact(withIdentifier:keysToFetch:)

**Framework**: Contacts  
**Kind**: method

Fetches a unified contact for the specified contact identifier.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func unifiedContact(withIdentifier identifier: String, keysToFetch keys: [any CNKeyDescriptor]) throws -> CNContact
```

#### Return Value

A unified contact matching or linked to the identifier.

#### Discussion

Due to unification, the returned contact may have a different identifier than you specify. To fetch a batch of contacts by identifiers, use [`predicateForContacts(withIdentifiers:)`](cncontact/predicateforcontacts(withidentifiers:).md) with [`unifiedContacts(matching:keysToFetch:)`](cncontactstore/unifiedcontacts(matching:keystofetch:).md). Fetch only the properties that your app uses. You can combine contact keys and contact key descriptors together.

To include [`CNContactNoteKey`](cncontactnotekey.md) in the array of keys in iOS, add the [`com.apple.developer.contacts.notes`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.contacts.notes) entitlement to your app. The entitlement requires permission from Apple to use, and you can’t publicly distribute your app until you have permission to use it. For more information about adding the entitlement and getting permission, see [`com.apple.developer.contacts.notes`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.contacts.notes).

> **Note**: In Swift, this method returns a nonoptional result and is marked with the `throws` keyword to indicate that it throws an error in cases of failure. You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [`Error Handling`](https://developer.apple.comhttps://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [`The Swift Programming Language`](https://developer.apple.comhttps://docs.swift.org/swift-book/) and [`About Imported Cocoa Error Parameters`](https://developer.apple.com/documentation/Swift/about-imported-cocoa-error-parameters).

In Swift, this method returns a nonoptional result and is marked with the `throws` keyword to indicate that it throws an error in cases of failure. You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [`Error Handling`](https://developer.apple.comhttps://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [`The Swift Programming Language`](https://developer.apple.comhttps://docs.swift.org/swift-book/) and [`About Imported Cocoa Error Parameters`](https://developer.apple.com/documentation/Swift/about-imported-cocoa-error-parameters).

## Parameters

- `identifier`: The identifier of the contact to fetch.
- `keys`: The properties to fetch in the returned   object.

## See Also

- [func enumerateContacts(with: CNContactFetchRequest, usingBlock: (CNContact, UnsafeMutablePointer<ObjCBool>) -> Void) throws](cncontactstore/enumeratecontacts(with:usingblock:).md)
  Returns a Boolean value that indicates whether the enumeration of all contacts matching a contact fetch request executes successfully.
- [func unifiedMeContactWithKeys(toFetch: [any CNKeyDescriptor]) throws -> CNContact](cncontactstore/unifiedmecontactwithkeys(tofetch:).md)
  Fetches the unified contact that’s the  card.
- [func unifiedContacts(matching: NSPredicate, keysToFetch: [any CNKeyDescriptor]) throws -> [CNContact]](cncontactstore/unifiedcontacts(matching:keystofetch:).md)
  Fetches all unified contacts matching the specified predicate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contacts/cncontactstore/unifiedcontact(withidentifier:keystofetch:))*