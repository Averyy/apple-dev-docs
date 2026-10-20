# NEHotspotEAPSettings.TTLSInnerAuthenticationType

**Framework**: Network Extension  
**Kind**: enum  
**Role**: Enumeration

The TTLS Inner Authentication Types that may be specified by [`NEHotspotEAPSettings.TTLSInnerAuthenticationType`](./ttlsinnerauthenticationtype-swift.enum.md).

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
enum TTLSInnerAuthenticationType
```

```c
enum NEHotspotConfigurationTTLSInnerAuthenticationType : NSInteger;
```

## Topics

### Enumeration Cases
- [NEHotspotEAPSettings.TTLSInnerAuthenticationType.eapttlsInnerAuthenticationPAP](./ttlsinnerauthenticationtype-swift.enum/eapttlsinnerauthenticationpap.md)
  Network EAPTTLS inner authentication type is PAP.
- [NEHotspotEAPSettings.TTLSInnerAuthenticationType.eapttlsInnerAuthenticationCHAP](./ttlsinnerauthenticationtype-swift.enum/eapttlsinnerauthenticationchap.md)
  Network EAPTTLS inner authentication type is CHAP.
- [NEHotspotEAPSettings.TTLSInnerAuthenticationType.eapttlsInnerAuthenticationMSCHAP](./ttlsinnerauthenticationtype-swift.enum/eapttlsinnerauthenticationmschap.md)
  Network EAPTTLS inner authentication type is MSCHAP.
- [NEHotspotEAPSettings.TTLSInnerAuthenticationType.eapttlsInnerAuthenticationMSCHAPv2](./ttlsinnerauthenticationtype-swift.enum/eapttlsinnerauthenticationmschapv2.md)
  Network EAPTTLS inner authentication type is MSCHAP, version 2.
- [NEHotspotEAPSettings.TTLSInnerAuthenticationType.eapttlsInnerAuthenticationEAP](./ttlsinnerauthenticationtype-swift.enum/eapttlsinnerauthenticationeap.md)
  Network EAPTTLS inner authentication type is EAP.
### Initializers
- [init?(rawValue: Int)](./ttlsinnerauthenticationtype-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Accessing EAP properties
- [var isTLSClientCertificateRequired: Bool](./istlsclientcertificaterequired.md)
  A Boolean value indicating whether a network requires two-factor authentication or allows zero-factor authentication.
- [var trustedServerNames: [String]](./trustedservernames.md)
  An array of server certificate common name strings used to verify a server’s certificate.
- [var supportedEAPTypes: [NSNumber]](./supportedeaptypes.md)
  An array of supported EAP types.
- [NEHotspotEAPSettings.EAPType](./eaptype.md)
  The EAP types that may be specified in [`supportedEAPTypes`](./supportedeaptypes.md).
- [var username: String](./username.md)
  The user name string for EAP authentication, encoded as UTF-8.
- [var password: String](./password.md)
  The password component of the IEEE 802.1X authentication credential.
- [var preferredTLSVersion: NEHotspotEAPSettings.TLSVersion](./preferredtlsversion.md)
  The Transport Layer Security (TLS) version to use during a TLS authentication handshake.
- [NEHotspotEAPSettings.TLSVersion](./tlsversion.md)
  The EAPTLS Version identifiers that may be specified by [`preferredTLSVersion`](./preferredtlsversion.md).
- [var outerIdentity: String](./outeridentity.md)
  The identity string to be used in the EAP-Identity/Response packet during outer EAP authentication.
- [var ttlsInnerAuthenticationType: NEHotspotEAPSettings.TTLSInnerAuthenticationType](./ttlsinnerauthenticationtype-swift.property.md)
  The inner-layer authentication protocol used by a TTLS module.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nehotspoteapsettings/ttlsinnerauthenticationtype-swift.enum)*