# AccessorySecurity.Crypto.KeyMaterial

**Framework**: Accessory Transport Extension  
**Kind**: struct

A structure that contains cryptographic key material for HPKE encryption.

**Availability**:
- iOS 26.4+ (Beta)
- iPadOS 26.4+ (Beta)
- Mac Catalyst 26.4+ (Beta)

## Declaration

```swift
struct KeyMaterial
```

#### Overview

The [`AccessorySecurity.Event.keyExchange(keyMaterial:)`](accessorysecurity/event/keyexchange(keymaterial:).md) case includes an instance of this type.

#### Derive the Shared Secret

When your accessory receives encrypted notification data, it decrypts the data using an [`HPKE`](https://developer.apple.comhttps://datatracker.ietf.org/doc/rfc9180/) receiver, which requires the accessory and extension to have a shared secret. The format of the secret is:

```xml
<ciphersuite>-<ciphersuite-version>-<device-uuid>-<direction>-<feature-id>
```

The following example uses the `HostToAccessory` direction:

```swift
P256-v1-f47ac10b-58cc-4372-a567-0e02b2c3d479-HostToAccessory-abcdef12-3456-7890-abcd-ef0123456789
```

In code, reference event’s feature ID, in combination with the [`ciphersuite`](accessorysecurity/crypto/keymaterial/ciphersuite.md) protocol information:

```swift
let protocolInfo: Data = Data("\(ciphersuite)-\(version)-\(identifier)".utf8)
let context: Data = Data("\(protocolInfo)-HostToAccessory-\(event.feature.id)".utf8)
```

## Topics

### Accessing key material
- [let identifier: String](accessorysecurity/crypto/keymaterial/identifier.md)
  An identifier that the system uses to derive HPKE keys.
- [let publicKey: Data](accessorysecurity/crypto/keymaterial/publickey.md)
  A data object that contains your public key.
- [var encapsulatedKey: Data](accessorysecurity/crypto/keymaterial/encapsulatedkey.md)
  A data object that contains an encapsulated key.
### Determining the encryption method
- [let ciphersuite: AccessorySecurity.Crypto.Ciphersuite](accessorysecurity/crypto/keymaterial/ciphersuite.md)
  An HPKE ciphersuite that the system uses for key exchange.
- [let version: AccessorySecurity.Crypto.Ciphersuite.Version](accessorysecurity/crypto/keymaterial/version.md)
  The ciphersuite protocol version.

## Relationships

### Conforms To
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorytransportextension/accessorysecurity/crypto/keymaterial)*