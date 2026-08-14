# CSPerson

**Framework**: Core Spotlight  
**Kind**: class

An object that represents a person in the context of search results.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+

## Declaration

```swift
class CSPerson
```

#### Overview

A `CSPerson` object represents a person in the context of search results. You can create a `CSPerson` object when you have a display name and a contact handle of some kind, such as an email address or phone number.

If you create a `CSPerson` object to represent a specific contact, you can use the value of the contact’s identifier property for the person object’s [`contactIdentifier`](csperson/contactidentifier.md) property. Using the same value lets you avoid using names or phone numbers to look up the contact that’s associated with a person.

## Topics

### Initializing a person object
- [init(displayName: String?, handles: [String], handleIdentifier: String)](csperson/init(displayname:handles:handleidentifier:).md)
  Returns a new `CSPerson` object initialized with the specified display name and contact attributes.
- [init?(coder: NSCoder)](csperson/init(coder:).md)
### Accessing person properties
- [var contactIdentifier: String?](csperson/contactidentifier.md)
  The identifier for the contact associated with the person.
- [var displayName: String?](csperson/displayname.md)
  A display name for the person.
- [var handleIdentifier: String](csperson/handleidentifier.md)
  A key that identifies the type of contact property represented by the person object’s handle.
- [var handles: [String]](csperson/handles.md)
  An array of contact handles related to the person.

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCoding](../foundation/nscoding.md)
- [NSCopying](../foundation/nscopying.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [NSSecureCoding](../foundation/nssecurecoding.md)

## See Also

- [class CSSearchableItem](cssearchableitem.md)
  The details of your app-specific content that someone might search for on their devices.
- [class CSSearchableItemAttributeSet](cssearchableitemattributeset.md)
  The detailed metadata for a searchable item.
- [class CSCustomAttributeKey](cscustomattributekey.md)
  A key associated with a custom attribute for a searchable item.
- [class CSLocalizedString](cslocalizedstring.md)
  An object that displays localized text in search results related to your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/csperson)*