# NEDNSOverTLSSettings

**Framework**: Network Extension  
**Kind**: class

The DNS resolver settings for a DNS-over-TLS server.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
class NEDNSOverTLSSettings
```

## Topics

### Configuring server properties
- [var serverName: String?](nednsovertlssettings/servername.md)
  The TLS name of a DNS-over-TLS server.
- [init(servers: [String])](nednssettings/init(servers:).md)
  Initialize the `NEDNSSetting` object.
- [var matchDomains: [String]?](nednssettings/matchdomains.md)
  A list of domain strings used to determine which DNS queries will use the DNS resolver settings contained in this object.
### Configuring client properties
- [var identityReference: Data?](nednsovertlssettings/identityreference.md)
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
- [class NEDNSOverHTTPSSettings](nednsoverhttpssettings.md)
  The DNS resolver settings for a DNS-over-HTTPS server.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nednsovertlssettings)*