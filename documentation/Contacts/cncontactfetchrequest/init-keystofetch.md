# init(keysToFetch:)

**Framework**: Contacts  
**Kind**: init

Creates a fetch request for the specified keys.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
init(keysToFetch: [any CNKeyDescriptor])
```

#### Return Value

The initialized [`CNContactFetchRequest`](cncontactfetchrequest.md) instance.

#### Discussion

This is the designated initializer for this class. Using `init` raises an exception.

## Parameters

- `keysToFetch`: An array of contact property keys and/or key descriptors from contacts objects to be fetched in the returned contacts. For a list of possible keys, see  .

## See Also

- [protocol CNKeyDescriptor](cnkeydescriptor.md)
  This protocol is reserved for Contacts framework usage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contacts/cncontactfetchrequest/init(keystofetch:))*