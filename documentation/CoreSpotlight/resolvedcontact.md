# ResolvedContact

**Framework**: Core Spotlight  
**Kind**: struct

Contact information used to match person and organization references in search queries.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct ResolvedContact
```

## Mentions

- [Making your indexed content available to Foundation Models](making-your-indexed-content-available-to-foundation-models.md)

#### Overview

Provide as many identifiers as available — the search tool uses them to match references in queries against metadata fields like authors, recipients, and participants.

## Topics

### Creating the contact
- [init(displayName: String)](resolvedcontact/init(displayname:).md)
### Specifying the person’s name
- [var displayName: String](resolvedcontact/displayname.md)
  Display name (e.g., “John Appleseed” or “Acme Corp”).
- [var nameComponents: [PersonNameComponents]](resolvedcontact/namecomponents.md)
  Structured name components for locale-aware matching.
- [var names: [String]](resolvedcontact/names.md)
  Alternate name strings the contact may be known by.
### Specifying contact information
- [var emailAddresses: [String]](resolvedcontact/emailaddresses.md)
  Email addresses associated with this contact.
- [var phoneNumbers: [String]](resolvedcontact/phonenumbers.md)
  Phone numbers associated with this contact.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [protocol ContactResolver](contactresolver.md)
  Resolves the current user’s identity for search queries involving people.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/resolvedcontact)*