# ResolvedContact

**Framework**: Core Spotlight  
**Kind**: struct

Contact information to help a search query match references to a person or organization.

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

Use this type to specify details about the person or business that uses your app. When a query matches references to a specific person or business, the information in this structure helps the search tool resolve references to that contact. For example, a query that looks for the author of an email uses this information to resolve a request such as “find the emails that I authored.” Fill in as many fields of this structure as possible with the information available to your app.

## Topics

### Creating the contact
- [init(displayName: String)](resolvedcontact/init(displayname:).md)
### Specifying the person’s name
- [var displayName: String](resolvedcontact/displayname.md)
  The name your app displays for the contact.
- [var nameComponents: [PersonNameComponents]](resolvedcontact/namecomponents.md)
  The contact’s names as a set of structured name components.
- [var names: [String]](resolvedcontact/names.md)
  Alternate names you use to refer to the contact.
### Specifying contact information
- [var emailAddresses: [String]](resolvedcontact/emailaddresses.md)
  The email addresses for this contact.
- [var phoneNumbers: [String]](resolvedcontact/phonenumbers.md)
  The phone numbers for this contact.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [protocol ContactResolver](contactresolver.md)
  An interface you use to help Foundation models resolve references to the person using the app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/resolvedcontact)*