# CredentialSession.Event

**Framework**: SecureElementCredential  
**Kind**: enum

Events produced by a credential session, such as connectivity events and errors.

**Availability**:
- iOS 18.1+
- iPadOS 18.1+

## Declaration

```swift
enum Event
```

## Topics

### Credential events
- [case credentialFinishedInstalling(credential: CredentialSession.Credential)](credentialsession/event/credentialfinishedinstalling(credential:).md)
  The session finished installing a credential.
- [CredentialSession.Credential](credentialsession/credential.md)
  Information about a credential that a credential session retrieves from the Secure Element.
### Card emulation events
- [case connectivityEvent(CredentialSession.ConnectivityEvent)](credentialsession/event/connectivityevent(_:).md)
  A credential received a connectivity event during card emulation.
- [CredentialSession.ConnectivityEvent](credentialsession/connectivityevent.md)
  An event that a credential receives during card emulation.
### NFC field events
- [case fieldStateChanged(info: CredentialSession.NFCFieldInformation)](credentialsession/event/fieldstatechanged(info:).md)
  The state of the NFC RF field changed during card emulation.
- [CredentialSession.NFCFieldInformation](credentialsession/nfcfieldinformation.md)
  The state of an NFC RF field.
### Invalidation events
- [case sessionInvalidated(reason: CredentialSession.ErrorCode)](credentialsession/event/sessioninvalidated(reason:).md)
  The session became invalidated.
- [CredentialSession.ErrorCode](credentialsession/errorcode.md)
  An error encountered by a credential session.
### Timeout events
- [CredentialSession.Event.cardEmulationTimeout](credentialsession/event/cardemulationtimeout.md)
  The session’s card emulation timer expired.
- [CredentialSession.Event.presentmentIntentAssertionTimeout](credentialsession/event/presentmentintentassertiontimeout.md)
  The session’s presentment intent assertion timed out.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var eventStream: AsyncStream<CredentialSession.Event>](credentialsession/eventstream.md)
  An asynchronous stream of session events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/secureelementcredential/credentialsession/event)*