# unifiedMeContactWithKeys(toFetch:)

**Framework**: Contacts  
**Kind**: method

Fetches the unified contact that’s the  card.

**Availability**:
- macOS 10.11+

## Declaration

```swift
func unifiedMeContactWithKeys(toFetch keys: [any CNKeyDescriptor]) throws -> CNContact
```

#### Return Value

The unified contact that is the  card or `nil` if there isn’t one.

#### Discussion

In the user interface,   represents the  contact. Fetch only the properties your app uses. You can combine contact keys and contact key descriptors together.

To include [`CNContactNoteKey`](cncontactnotekey.md) in the array of keys in iOS 13 or later or macOS 13 or later, add the [`com.apple.developer.contacts.notes`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.contacts.notes) entitlement to your app. The entitlement requires permission from Apple to use, and you can’t publicly distribute your app until you have permission to use it. For more information about adding the entitlement and getting permission, see [`com.apple.developer.contacts.notes`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.contacts.notes).

## Parameters

- `keys`: The properties to fetch in the returned   object.

## See Also

- [func enumerateContacts(with: CNContactFetchRequest, usingBlock: (CNContact, UnsafeMutablePointer<ObjCBool>) -> Void) throws](cncontactstore/enumeratecontacts(with:usingblock:).md)
  Returns a Boolean value that indicates whether the enumeration of all contacts matching a contact fetch request executes successfully.
- [func unifiedContact(withIdentifier: String, keysToFetch: [any CNKeyDescriptor]) throws -> CNContact](cncontactstore/unifiedcontact(withidentifier:keystofetch:).md)
  Fetches a unified contact for the specified contact identifier.
- [func unifiedContacts(matching: NSPredicate, keysToFetch: [any CNKeyDescriptor]) throws -> [CNContact]](cncontactstore/unifiedcontacts(matching:keystofetch:).md)
  Fetches all unified contacts matching the specified predicate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contacts/cncontactstore/unifiedmecontactwithkeys(tofetch:))*