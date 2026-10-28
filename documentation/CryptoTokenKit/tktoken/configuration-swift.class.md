# TKToken.Configuration

**Framework**: CryptoTokenKit  
**Kind**: class  
**Role**: Class

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

```objc
@interface TKTokenConfiguration : NSObject
```

## Overview

When you introduce a new [`TKToken.Configuration`](./configuration-swift.class.md) into the system, it can inform the system about its identities, consisting of both private keys and certificates, which the [`keychainItems`](./configuration-swift.class/keychainitems.md) property provides. Use the [`configurationData`](./configuration-swift.class/configurationdata.md) property to set additional configuration data.

You configure always-available tokens on a per-user basis. Although the token driver and the app hosting the token extension are shared across the system, the configuration for a token is stored individually for each user.

## Topics

### Reporting Configuration Information
- [var instanceID: TKToken.InstanceID](./configuration-swift.class/instanceid.md)
  The unique, persistent identifier of this token that the token implementation creates.
- [var configurationData: Data?](./configuration-swift.class/configurationdata.md)
  Additional configuration information for the token instance.
### Retrieving Keys and Certificates
- [var keychainItems: [TKTokenKeychainItem]](./configuration-swift.class/keychainitems.md)
  The keychain items associated with this token.
- [func certificate(for: TKToken.ObjectID) throws -> TKTokenKeychainCertificate](./configuration-swift.class/certificate%28for%29.md)
  Returns a certificate from the keychain with the object identifier you specify.
- [func key(for: TKToken.ObjectID) throws -> TKTokenKeychainKey](./configuration-swift.class/key%28for%29.md)
  Returns a key from the keychain with the object identifier you specify.

## Relationships

### Inherits From
- [NSObject](../../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../../Swift/cvararg.md)
- [CustomDebugStringConvertible](../../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../../Swift/customstringconvertible.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [NSObjectProtocol](../../ObjectiveC/nsobjectprotocol.md)

## See Also

### Configuring the Token
- [var configuration: TKToken.Configuration](./configuration-swift.property.md)
  The current configuration for a token.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptotokenkit/tktoken/configuration-swift.class)*