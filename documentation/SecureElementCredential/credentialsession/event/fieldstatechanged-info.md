# CredentialSession.Event.fieldStateChanged(info:)

**Framework**: SecureElementCredential  
**Kind**: case

The state of the NFC RF field changed during card emulation.

**Availability**:
- iOS 18.1+
- iPadOS 18.1+

## Declaration

```swift
case fieldStateChanged(info: CredentialSession.NFCFieldInformation)
```

#### Discussion

The credential session sends an initial event with the current field state when entering the card emulation state. The session then sends further events if the field state changes. The session only publishes this event when it’s in the card emulation state.

You can only receive this event if you have acquired the [`CredentialSession.PresentmentIntentAssertion`](credentialsession/presentmentintentassertion.md).

## See Also

- [CredentialSession.NFCFieldInformation](credentialsession/nfcfieldinformation.md)
  The state of an NFC RF field.


---

*[View on Apple Developer](https://developer.apple.com/documentation/secureelementcredential/credentialsession/event/fieldstatechanged(info:))*