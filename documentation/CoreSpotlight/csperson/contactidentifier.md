# contactIdentifier

**Framework**: Core Spotlight  
**Kind**: property

The identifier for the contact associated with the person.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+

## Declaration

```swift
var contactIdentifier: String? { get set }
```

#### Discussion

When you use the contact’s [`identifier`](https://developer.apple.com/documentation/Contacts/CNContact/identifier) value for the optional [`contactIdentifier`](csperson/contactidentifier.md) property, it enables a direct way to look up the associated contact.

## See Also

- [var displayName: String?](csperson/displayname.md)
  A display name for the person.
- [var handleIdentifier: String](csperson/handleidentifier.md)
  A key that identifies the type of contact property represented by the person object’s handle.
- [var handles: [String]](csperson/handles.md)
  An array of contact handles related to the person.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/csperson/contactidentifier)*