# NEDNSOverHTTPSSettings

**Framework**: Network Extension  
**Kind**: class

The DNS resolver settings for a DNS-over-HTTPS server.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
class NEDNSOverHTTPSSettings
```

## Topics

### Configuring server properties
- [var serverURL: URL?](nednsoverhttpssettings/serverurl.md)
  The URL of a DNS-over-HTTPS server.
- [init(servers: [String])](nednssettings/init(servers:).md)
  Initialize the `NEDNSSetting` object.
- [var matchDomains: [String]?](nednssettings/matchdomains.md)
  A list of domain strings used to determine which DNS queries will use the DNS resolver settings contained in this object.
### Configuring client properties
- [var identityReference: Data?](nednsoverhttpssettings/identityreference.md)
  A persistent keychain reference to a keychain item containing the certificate and private key components of the DNS client credential.

## Relationships

### Inherits From
- [NEDNSSettings](nednssettings.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [class NEDNSSettingsManager](nednssettingsmanager.md)
  An object you use to create and manage a DNS settings configuration.
- [class NEDNSOverTLSSettings](nednsovertlssettings.md)
  The DNS resolver settings for a DNS-over-TLS server.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nednsoverhttpssettings)*