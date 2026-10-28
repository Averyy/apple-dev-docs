# unifiedContact(withIdentifier:keysToFetch:)

**Framework**: Contacts  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (CNContact *) unifiedContactWithIdentifier:(NSString *) identifier keysToFetch:(NSArray<id<CNKeyDescriptor>> *) keys error:(NSError **) error;
```

## Return Value

A unified contact matching or linked to the identifier.

## Discussion

Due to unification, the returned contact may have a different identifier than you specify. To fetch a batch of contacts by identifiers, use [`predicateForContacts(withIdentifiers:)`](../cncontact/predicateforcontacts%28withidentifiers%29.md) with [`unifiedContacts(matching:keysToFetch:)`](./unifiedcontacts%28matching,keystofetch%29.md). Fetch only the properties that your app uses. You can combine contact keys and contact key descriptors together.

To include [`CNContactNoteKey`](../cncontactnotekey.md) in the array of keys in iOS, add the [`com.apple.developer.contacts.notes`](../../BundleResources/entitlements/com.apple.developer.contacts.notes.md) entitlement to your app. The entitlement requires permission from Apple to use, and you can’t publicly distribute your app until you have permission to use it. For more information about adding the entitlement and getting permission, see [`com.apple.developer.contacts.notes`](../../BundleResources/entitlements/com.apple.developer.contacts.notes.md).

> **Handling Errors in Swift**: In Swift, this method returns a nonoptional result and is marked with the `throws` keyword to indicate that it throws an error in cases of failure. You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [Error Handling](https://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [The Swift Programming Language](https://docs.swift.org/swift-book/) and [About Imported Cocoa Error Parameters](../../Swift/about-imported-cocoa-error-parameters.md).

## Parameters

- `identifier`: The identifier of the contact to fetch.
- `keys`: The properties to fetch in the returned [`CNContact`](../cncontact.md) object.

## See Also

### Fetching contacts
- [func enumerateContacts(with: CNContactFetchRequest, usingBlock: (CNContact, UnsafeMutablePointer<ObjCBool>) -> Void) throws](./enumeratecontacts%28with,usingblock%29.md)
  Returns a Boolean value that indicates whether the enumeration of all contacts matching a contact fetch request executes successfully.
- [func unifiedMeContactWithKeys(toFetch: [any CNKeyDescriptor]) throws -> CNContact](./unifiedmecontactwithkeys%28tofetch%29.md)
  Fetches the unified contact that’s the *me* card.
- [func unifiedContacts(matching: NSPredicate, keysToFetch: [any CNKeyDescriptor]) throws -> [CNContact]](./unifiedcontacts%28matching,keystofetch%29.md)
  Fetches all unified contacts matching the specified predicate.
- [- enumeratorForContactFetchRequest:error:](./enumeratorforcontactfetchrequest_error_.md)
  Enumerates a contact fetch request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contacts/cncontactstore/unifiedcontact(withidentifier:keystofetch:))*