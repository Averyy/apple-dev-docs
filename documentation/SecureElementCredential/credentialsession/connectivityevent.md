# CredentialSession.ConnectivityEvent

**Framework**: SecureElementCredential  
**Kind**: struct

An event that a credential receives during card emulation.

**Availability**:
- iOS 18.1+
- iPadOS 18.1+

## Declaration

```swift
struct ConnectivityEvent
```

## Topics

### Identifying the target instance
- [let instanceApplicationIdentifier: Data](credentialsession/connectivityevent/instanceapplicationidentifier.md)
  The instance application identifier associated with the credential that receives an event.
### Inspecting event data
- [let data: Data](credentialsession/connectivityevent/data.md)
  The data a credential receives during card emulation.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [case connectivityEvent(CredentialSession.ConnectivityEvent)](credentialsession/event/connectivityevent(_:).md)
  A credential received a connectivity event during card emulation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/secureelementcredential/credentialsession/connectivityevent)*