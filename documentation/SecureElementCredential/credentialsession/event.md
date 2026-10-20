# CredentialSession.Event

**Framework**: SecureElementCredential  
**Kind**: enum  
**Role**: Enumeration

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
- [case credentialFinishedInstalling(credential: CredentialSession.Credential)](./event/credentialfinishedinstalling%28credential%29.md)
  The session finished installing a credential.
- [CredentialSession.Credential](./credential.md)
  Information about a credential that a credential session retrieves from the Secure Element.
### Card emulation events
- [case connectivityEvent(CredentialSession.ConnectivityEvent)](./event/connectivityevent%28_%29.md)
  A credential received a connectivity event during card emulation.
- [CredentialSession.ConnectivityEvent](./connectivityevent.md)
  An event that a credential receives during card emulation.
### NFC field events
- [case fieldStateChanged(info: CredentialSession.NFCFieldInformation)](./event/fieldstatechanged%28info%29.md)
  The state of the NFC RF field changed during card emulation.
- [CredentialSession.NFCFieldInformation](./nfcfieldinformation.md)
  The state of an NFC RF field.
### Invalidation events
- [case sessionInvalidated(reason: CredentialSession.ErrorCode)](./event/sessioninvalidated%28reason%29.md)
  The session became invalidated.
- [CredentialSession.ErrorCode](./errorcode.md)
  An error encountered by a credential session.
### Timeout events
- [CredentialSession.Event.cardEmulationTimeout](./event/cardemulationtimeout.md)
  The session’s card emulation timer expired.
- [CredentialSession.Event.presentmentIntentAssertionTimeout](./event/presentmentintentassertiontimeout.md)
  The session’s presentment intent assertion timed out.

## Relationships

### Conforms To
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Handling session events
- [var eventStream: AsyncStream<CredentialSession.Event>](./eventstream.md)
  An asynchronous stream of session events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/secureelementcredential/credentialsession/event)*