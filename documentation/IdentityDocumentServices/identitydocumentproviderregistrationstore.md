# IdentityDocumentProviderRegistrationStore

**Framework**: IdentityDocumentServices  
**Kind**: class

A store that notifies the system which documents an app has available for presentment.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+

## Declaration

```swift
actor IdentityDocumentProviderRegistrationStore
```

## Mentions

- [Implementing as an identity document provider](implenting-as-an-identity-document-provider.md)

#### Discussion

The system uses the information you register with this store to appropriately surface your app as an option during a presentment. When a person registers a document, the authorization UI you provide through the app’s `IdentityDocumentProvider` extension needs to handle incoming requests for that specific document. The app needs to only register documents that are active and that it can successfully present. If a document becomes inactive, you need to unregister it from the store.

> **Note**:  This API requires the [`Digital Credentials API - Mobile Document Provider`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.identity-document-services.document-provider.mobile-document-types) entitlement for online web presentment.

## Topics

### Registering and removing mobile documents
- [init()](identitydocumentproviderregistrationstore/init.md)
  Initializes an identity document provider registration store.
- [func addRegistration(some IdentityDocumentRegistration) async throws](identitydocumentproviderregistrationstore/addregistration(_:).md)
  Register a document with the system.
- [var registrations: [any IdentityDocumentRegistration]](identitydocumentproviderregistrationstore/registrations.md)
  A list of all documents registered with the system.
- [func removeRegistration(forDocumentIdentifier: String) async throws](identitydocumentproviderregistrationstore/removeregistration(fordocumentidentifier:).md)
  Unregister a specific document with the system.
### Defining and getting the status of the mobile document
- [var status: IdentityDocumentProviderRegistrationStore.Status](identitydocumentproviderregistrationstore/status-swift.property.md)
  The status of the registration store.
- [IdentityDocumentProviderRegistrationStore.Status](identitydocumentproviderregistrationstore/status-swift.enum.md)
  Defines a status for the registration store.
### Errors
- [IdentityDocumentProviderRegistrationStore.RegistrationError](identitydocumentproviderregistrationstore/registrationerror.md)
  An error type that the identity document registration store and associated types throw.

## Relationships

### Conforms To
- [Actor](../Swift/Actor.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [protocol IdentityDocumentRegistration](identitydocumentregistration.md)
  A protocol that defines an identity document registration.
- [struct MobileDocumentRegistration](mobiledocumentregistration.md)
  A type you use to register mobile documents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/identitydocumentservices/identitydocumentproviderregistrationstore)*