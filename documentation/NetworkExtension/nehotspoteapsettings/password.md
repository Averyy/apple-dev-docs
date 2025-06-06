# password

**Framework**: Network Extension  
**Kind**: property

The password component of the IEEE 802.1X authentication credential.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var password: String { get set }
```

#### Discussion

This property must be configured for PEAP, EAP-TTLS, and EAP-FAST authentication. It is optional for EAP-TLS authentication. The length of the string must be 1 to 64 characters, inclusive.

## See Also

- [var isTLSClientCertificateRequired: Bool](nehotspoteapsettings/istlsclientcertificaterequired.md)
  A Boolean value indicating whether a network requires two-factor authentication or allows zero-factor authentication.
- [var trustedServerNames: [String]](nehotspoteapsettings/trustedservernames.md)
  An array of server certificate common name strings used to verify a server’s certificate.
- [var supportedEAPTypes: [NSNumber]](nehotspoteapsettings/supportedeaptypes.md)
  An array of supported EAP types.
- [NEHotspotEAPSettings.EAPType](nehotspoteapsettings/eaptype.md)
  The EAP types that may be specified in [`supportedEAPTypes`](nehotspoteapsettings/supportedeaptypes.md).
- [var username: String](nehotspoteapsettings/username.md)
  The user name string for EAP authentication, encoded as UTF-8.
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

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nehotspoteapsettings/password)*