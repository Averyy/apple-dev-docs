# TKToken.Configuration

**Framework**: CryptoTokenKit  
**Kind**: class

A token’s configuration.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 10.15+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
class Configuration
```

#### Overview

When you introduce a new [`TKToken.Configuration`](tktoken/configuration-swift.class.md) into the system, it can inform the system about its identities, consisting of both private keys and certificates, which the [`keychainItems`](tktoken/configuration-swift.class/keychainitems.md) property provides. Use the [`configurationData`](tktoken/configuration-swift.class/configurationdata.md) property to set additional configuration data.

You configure always-available tokens on a per-user basis. Although the token driver and the app hosting the token extension are shared across the system, the configuration for a token is stored individually for each user.

## Topics

### Reporting Configuration Information
- [var instanceID: TKToken.InstanceID](tktoken/configuration-swift.class/instanceid.md)
  The unique, persistent identifier of this token that the token implementation creates.
- [var configurationData: Data?](tktoken/configuration-swift.class/configurationdata.md)
  Additional configuration information for the token instance.
### Retrieving Keys and Certificates
- [var keychainItems: [TKTokenKeychainItem]](tktoken/configuration-swift.class/keychainitems.md)
  The keychain items associated with this token.
- [func certificate(for: TKToken.ObjectID) throws -> TKTokenKeychainCertificate](tktoken/configuration-swift.class/certificate(for:).md)
  Returns a certificate from the keychain with the object identifier you specify.
- [func key(for: TKToken.ObjectID) throws -> TKTokenKeychainKey](tktoken/configuration-swift.class/key(for:).md)
  Returns a key from the keychain with the object identifier you specify.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [var configuration: TKToken.Configuration](tktoken/configuration-swift.property.md)
  The current configuration for a token.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptotokenkit/tktoken/configuration-swift.class)*