# NEHotspotEAPSettings.EAPType

**Framework**: Network Extension  
**Kind**: enum

The EAP types that may be specified in [`supportedEAPTypes`](nehotspoteapsettings/supportedeaptypes.md).

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
enum EAPType
```

## Topics

### Enumeration Cases
- [NEHotspotEAPSettings.EAPType.EAPTLS](nehotspoteapsettings/eaptype/eaptls.md)
  Network EAP type is `EAPTLS`.
- [NEHotspotEAPSettings.EAPType.EAPTTLS](nehotspoteapsettings/eaptype/eapttls.md)
  Network EAP type is `EAPTTLS`.
- [NEHotspotEAPSettings.EAPType.EAPPEAP](nehotspoteapsettings/eaptype/eappeap.md)
  Network EAP type is `EAPPEAP`.
- [NEHotspotEAPSettings.EAPType.EAPFAST](nehotspoteapsettings/eaptype/eapfast.md)
  Network EAP type is `EAPFAST`.
### Initializers
- [init?(rawValue: Int)](nehotspoteapsettings/eaptype/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var isTLSClientCertificateRequired: Bool](nehotspoteapsettings/istlsclientcertificaterequired.md)
  A Boolean value indicating whether a network requires two-factor authentication or allows zero-factor authentication.
- [var trustedServerNames: [String]](nehotspoteapsettings/trustedservernames.md)
  An array of server certificate common name strings used to verify a server’s certificate.
- [var supportedEAPTypes: [NSNumber]](nehotspoteapsettings/supportedeaptypes.md)
  An array of supported EAP types.
- [var username: String](nehotspoteapsettings/username.md)
  The user name string for EAP authentication, encoded as UTF-8.
- [var password: String](nehotspoteapsettings/password.md)
  The password component of the IEEE 802.1X authentication credential.
- [var preferredTLSVersion: NEHotspotEAPSettings.TLSVersion](nehotspoteapsettings/preferredtlsversion.md)
  The Transport Layer Security (TLS) version to use during a TLS authentication handshake.
- [NEHotspotEAPSettings.TLSVersion](nehotspoteapsettings/tlsversion.md)
  The EAPTLS Version identifiers that may be specified by [`preferredTLSVersion`](nehotspoteapsettings/preferredtlsversion.md).
- [var outerIdentity: String](nehotspoteapsettings/outeridentity.md)
  The identity string to be used in the EAP-Identity/Response packet during outer EAP authentication.
- [var ttlsInnerAuthenticationType: NEHotspotEAPSettings.TTLSInnerAuthenticationType](nehotspoteapsettings/ttlsinnerauthenticationtype-swift.property.md)
  The inner-layer authentication protocol used by a TTLS module.
- [NEHotspotEAPSettings.TTLSInnerAuthenticationType](nehotspoteapsettings/ttlsinnerauthenticationtype-swift.enum.md)
  The TTLS Inner Authentication Types that may be specified by [`NEHotspotEAPSettings.TTLSInnerAuthenticationType`](nehotspoteapsettings/ttlsinnerauthenticationtype-swift.enum.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nehotspoteapsettings/eaptype)*