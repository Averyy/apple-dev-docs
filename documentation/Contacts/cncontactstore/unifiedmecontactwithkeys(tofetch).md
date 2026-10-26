# unifiedMeContactWithKeys(toFetch:)

**Framework**: Contacts  
**Kind**: method  
**Role**: Instance Method

Fetches the unified contact that’s the *me* card.

**Availability**:
- macOS 10.11+

## Declaration

```swift
func unifiedMeContactWithKeys(toFetch keys: [any CNKeyDescriptor]) throws -> CNContact
```

```objc
- (CNContact *) unifiedMeContactWithKeysToFetch:(NSArray<id<CNKeyDescriptor>> *) keys error:(NSError **) error;
```

#### Return Value

The unified contact that is the *me* card or `nil` if there isn’t one.

#### Discussion

In the user interface, *My Card*  represents the *me* contact. Fetch only the properties your app uses. You can combine contact keys and contact key descriptors together.

To include [`CNContactNoteKey`](../cncontactnotekey.md) in the array of keys in iOS 13 or later or macOS 13 or later, add the [`com.apple.developer.contacts.notes`](../../BundleResources/entitlements/com.apple.developer.contacts.notes.md) entitlement to your app. The entitlement requires permission from Apple to use, and you can’t publicly distribute your app until you have permission to use it. For more information about adding the entitlement and getting permission, see [`com.apple.developer.contacts.notes`](../../BundleResources/entitlements/com.apple.developer.contacts.notes.md).

## Parameters

- `keys`: The properties to fetch in the returned [`CNContact`](../cncontact.md) object.

## See Also

### Fetching contacts
- [func enumerateContacts(with: CNContactFetchRequest, usingBlock: (CNContact, UnsafeMutablePointer<ObjCBool>) -> Void) throws](./enumeratecontacts%28with,usingblock%29.md)
  Returns a Boolean value that indicates whether the enumeration of all contacts matching a contact fetch request executes successfully.
- [func unifiedContact(withIdentifier: String, keysToFetch: [any CNKeyDescriptor]) throws -> CNContact](./unifiedcontact%28withidentifier,keystofetch%29.md)
  Fetches a unified contact for the specified contact identifier.
- [func unifiedContacts(matching: NSPredicate, keysToFetch: [any CNKeyDescriptor]) throws -> [CNContact]](./unifiedcontacts%28matching,keystofetch%29.md)
  Fetches all unified contacts matching the specified predicate.
- [- enumeratorForContactFetchRequest:error:](./enumeratorforcontactfetchrequest_error_.md)
  Enumerates a contact fetch request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contacts/cncontactstore/unifiedmecontactwithkeys(tofetch:))*