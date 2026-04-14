# init(keyType:cipherSuite:version:key:supportedTransports:identifier:)

**Framework**: Accessory Transport Extension  
**Kind**: init

Creates a security message.

**Availability**:
- iOS 26.5+ (Beta)
- iPadOS 26.5+ (Beta)

## Declaration

```swift
init(keyType: SecurityMessage.KeyType, cipherSuite: SecurityMessage.CipherSuite, version: SecurityMessage.CipherSuite.Version, key: Data, supportedTransports: [AccessoryTransport] = [.bluetooth], identifier: String? = nil)
```

## Parameters

- `keyType`: The type of key carried by this message.
- `cipherSuite`: The cipher suite used for key exchange.
- `version`: The cipher suite version.
- `key`: The key data.
- `supportedTransports`: The supported transports by accessory for sending sensitive information. Default is Bluetooth.
- `identifier`: An optional identifier for HPKE key derivation (Bluetooth identifier).


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorytransportextension/securitymessage/init(keytype:ciphersuite:version:key:supportedtransports:identifier:))*