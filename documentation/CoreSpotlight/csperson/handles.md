# handles

**Framework**: Core Spotlight  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (readonly) NSArray<NSString *> * handles;
```

## Discussion

Contact handles can include phone numbers, email addresses, and URLs. For additional contact handles, see Metadata Keys in [`CNContact`](../../Contacts/cncontact.md).

## See Also

### Accessing person properties
- [var contactIdentifier: String?](./contactidentifier.md)
  The identifier for the contact associated with the person.
- [var displayName: String?](./displayname.md)
  A display name for the person.
- [var handleIdentifier: String](./handleidentifier.md)
  A key that identifies the type of contact property represented by the person object’s handle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/csperson/handles)*