# enumeratorForContactFetchRequest:error:

**Framework**: Contacts  
**Kind**: method  
**Role**: Instance Method

Enumerates a contact fetch request.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```objc
- (CNFetchResult<NSEnumerator<CNContact *> *> *) enumeratorForContactFetchRequest:(CNContactFetchRequest *) request error:(NSError **) error;
```

#### Return Value

An enumerator of the records matching the result, or `nil` if there was an error.

#### Discussion

Executes the fetch request and returns an enumerator for the results. This can prevent all events from loading into memory at once. An error that occurs during enumeration may throw an exception.

## Parameters

- `request`: The contact fetch request.
- `error`: Error information, if an error occurred.

## See Also

### Fetching contacts
- [func enumerateContacts(with: CNContactFetchRequest, usingBlock: (CNContact, UnsafeMutablePointer<ObjCBool>) -> Void) throws](./enumeratecontacts%28with,usingblock%29.md)
  Returns a Boolean value that indicates whether the enumeration of all contacts matching a contact fetch request executes successfully.
- [func unifiedMeContactWithKeys(toFetch: [any CNKeyDescriptor]) throws -> CNContact](./unifiedmecontactwithkeys%28tofetch%29.md)
  Fetches the unified contact that’s the *me* card.
- [func unifiedContact(withIdentifier: String, keysToFetch: [any CNKeyDescriptor]) throws -> CNContact](./unifiedcontact%28withidentifier,keystofetch%29.md)
  Fetches a unified contact for the specified contact identifier.
- [func unifiedContacts(matching: NSPredicate, keysToFetch: [any CNKeyDescriptor]) throws -> [CNContact]](./unifiedcontacts%28matching,keystofetch%29.md)
  Fetches all unified contacts matching the specified predicate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contacts/cncontactstore/enumeratorforcontactfetchrequest:error:)*