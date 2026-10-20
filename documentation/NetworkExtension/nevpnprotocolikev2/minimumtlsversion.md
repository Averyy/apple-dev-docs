# minimumTLSVersion

**Framework**: Network Extension  
**Kind**: property  
**Role**: Instance Property

The minimum TLS version to allow for EAP-TLS authentication.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var minimumTLSVersion: NEVPNIKEv2TLSVersion { get set }
```

```objc
@property NEVPNIKEv2TLSVersion minimumTLSVersion;
```

#### Discussion

The default value of this property is [`NEVPNIKEv2TLSVersion.versionDefault`](../nevpnikev2tlsversion/versiondefault.md).

## See Also

### Accessing TLS version properties
- [var maximumTLSVersion: NEVPNIKEv2TLSVersion](./maximumtlsversion.md)
  The minimum TLS version to allow for EAP-TLS authentication.
- [enum NEVPNIKEv2TLSVersion](../nevpnikev2tlsversion.md)
  An enumeration of TLS Versions for use in EAP-TLS.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nevpnprotocolikev2/minimumtlsversion)*