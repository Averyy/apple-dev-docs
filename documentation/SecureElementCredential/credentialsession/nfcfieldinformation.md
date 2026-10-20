# CredentialSession.NFCFieldInformation

**Framework**: SecureElementCredential  
**Kind**: enum  
**Role**: Enumeration

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
- [CredentialSession.NFCFieldInformation.fieldAbsent](./nfcfieldinformation/fieldabsent.md)
  No NFC reader RF field is present.
- [CredentialSession.NFCFieldInformation.fieldPresent](./nfcfieldinformation/fieldpresent.md)
  An NFC reader’s RF field is present.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### NFC field events
- [case fieldStateChanged(info: CredentialSession.NFCFieldInformation)](./event/fieldstatechanged%28info%29.md)
  The state of the NFC RF field changed during card emulation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/secureelementcredential/credentialsession/nfcfieldinformation)*