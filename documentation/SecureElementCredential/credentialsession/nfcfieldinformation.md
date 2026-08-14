# CredentialSession.NFCFieldInformation

**Framework**: SecureElementCredential  
**Kind**: enum

The state of an NFC RF field.

**Availability**:
- iOS 18.1+
- iPadOS 18.1+

## Declaration

```swift
enum NFCFieldInformation
```

## Topics

### Field states
- [CredentialSession.NFCFieldInformation.fieldAbsent](credentialsession/nfcfieldinformation/fieldabsent.md)
  No NFC reader RF field is present.
- [CredentialSession.NFCFieldInformation.fieldPresent](credentialsession/nfcfieldinformation/fieldpresent.md)
  An NFC reader’s RF field is present.

## Relationships

### Conforms To
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [case fieldStateChanged(info: CredentialSession.NFCFieldInformation)](credentialsession/event/fieldstatechanged(info:).md)
  The state of the NFC RF field changed during card emulation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/secureelementcredential/credentialsession/nfcfieldinformation)*