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
### Operators
- [static func == (CredentialSession.NFCFieldInformation, CredentialSession.NFCFieldInformation) -> Bool](credentialsession/nfcfieldinformation/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Instance Properties
- [var hashValue: Int](credentialsession/nfcfieldinformation/hashvalue.md)
  The hash value.
### Instance Methods
- [func hash(into: inout Hasher)](credentialsession/nfcfieldinformation/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [Equatable Implementations](credentialsession/nfcfieldinformation/equatable-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [case fieldStateChanged(info: CredentialSession.NFCFieldInformation)](credentialsession/event/fieldstatechanged(info:).md)
  The state of the NFC RF field changed during card emulation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/secureelementcredential/credentialsession/nfcfieldinformation)*