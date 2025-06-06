# handles

**Framework**: Core Spotlight  
**Kind**: property

An array of contact handles related to the person.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+

## Declaration

```swift
var handles: [String] { get }
```

#### Discussion

Contact handles can include phone numbers, email addresses, and URLs. For additional contact handles, see Metadata Keys in [`CNContact`](https://developer.apple.com/documentation/Contacts/CNContact).

## See Also

- [var contactIdentifier: String?](csperson/contactidentifier.md)
  The identifier for the contact associated with the person.
- [var displayName: String?](csperson/displayname.md)
  A display name for the person.
- [var handleIdentifier: String](csperson/handleidentifier.md)
  A key that identifies the type of contact property represented by the person object’s handle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/csperson/handles)*