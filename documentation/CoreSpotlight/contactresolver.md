# ContactResolver

**Framework**: Core Spotlight  
**Kind**: protocol

Resolves the current user’s identity for search queries involving people.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
protocol ContactResolver : Sendable
```

## Mentions

- [Making your indexed content available to Foundation Models](making-your-indexed-content-available-to-foundation-models.md)

#### Overview

When a search involves people (e.g., “emails from me”, “notes I created yesterday”), the search tool needs to know who “me” is. Implement this protocol to provide the current user’s contact information from your app’s identity source — such as an account profile, Contacts framework, or other source.

**Example:**

```swift
struct MyContactResolver: ContactResolver {
    func userIdentity() -> ResolvedContact {
        var contact = ResolvedContact(displayName: "John Appleseed")
        contact.emailAddresses = ["john@example.com"]
        return contact
    }
}

var configuration = SpotlightSearchTool.Configuration()
configuration.contactResolver = MyContactResolver()
```

## Topics

### Returning the identity data
- [func userIdentity() -> ResolvedContact](contactresolver/useridentity.md)
  Returns the current user’s contact information.

## Relationships

### Inherits From
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct ResolvedContact](resolvedcontact.md)
  Contact information used to match person and organization references in search queries.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/contactresolver)*