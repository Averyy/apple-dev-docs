# CredentialSession.ConnectivityEvent

**Framework**: SecureElementCredential  
**Kind**: struct  
**Role**: Structure

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
- [let instanceApplicationIdentifier: Data](./connectivityevent/instanceapplicationidentifier.md)
  The instance application identifier associated with the credential that receives an event.
### Inspecting event data
- [let data: Data](./connectivityevent/data.md)
  The data a credential receives during card emulation.

## Relationships

### Conforms To
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Card emulation events
- [case connectivityEvent(CredentialSession.ConnectivityEvent)](./event/connectivityevent%28_%29.md)
  A credential received a connectivity event during card emulation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/secureelementcredential/credentialsession/connectivityevent)*