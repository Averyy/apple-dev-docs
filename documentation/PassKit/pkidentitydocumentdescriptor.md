# PKIdentityDocumentDescriptor

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: protocol

A type that describes the structure and behavior of an identity document.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
protocol PKIdentityDocumentDescriptor : NSObjectProtocol
```

#### Overview

A descriptor object describes the type of document that your app can request or check whether a document is available to request. For example, you use a [`PKIdentityDriversLicenseDescriptor`](pkidentitydriverslicensedescriptor.md) to request information from a user’s driver’s license (or equivalent document).

> **Note**:  Different document types behave differently, requiring different properties or response formats. Don’t define your own implementation of this protocol or subclass an existing implementation.

 Different document types behave differently, requiring different properties or response formats. Don’t define your own implementation of this protocol or subclass an existing implementation.

## Topics

### Inspecting elements
- [var elements: [PKIdentityElement]](pkidentitydocumentdescriptor/elements.md)
  A list of identity elements to request.
- [class PKIdentityElement](pkidentityelement.md)
  An object that represents the elements an app requests from identity documents.
### Adding an identity element
- [func addElements([PKIdentityElement], intentToStore: PKIdentityIntentToStore)](pkidentitydocumentdescriptor/addelements(_:intenttostore:).md)
  Adds a list of identity element and defines the way an app, or it’s server, stores the elements.
- [class PKIdentityIntentToStore](pkidentityintenttostore.md)
  An object that represents your intention to store an identity element or values derived from an identity element.
### Getting an elements intent
- [func intentToStore(element: PKIdentityElement) -> PKIdentityIntentToStore?](pkidentitydocumentdescriptor/intenttostore(element:).md)
  Gets the intent to store for an identity element you specify.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
### Conforming Types
- [PKIdentityDriversLicenseDescriptor](pkidentitydriverslicensedescriptor.md)
- [PKIdentityNationalIDCardDescriptor](pkidentitynationalidcarddescriptor.md)

## See Also

- [class PKIdentityDriversLicenseDescriptor](pkidentitydriverslicensedescriptor.md)
  An object for requesting information from a user’s driver’s license or equivalent document.
- [class PKIdentityIntentToStore](pkidentityintenttostore.md)
  An object that represents your intention to store an identity element or values derived from an identity element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkidentitydocumentdescriptor)*