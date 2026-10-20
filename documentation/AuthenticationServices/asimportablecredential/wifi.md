# ASImportableCredential.WiFi

**Framework**: Authentication Services  
**Kind**: struct  
**Role**: Structure

A representation of Wi-Fi Passphrase as defined in the [Credential Exchange Format (CXF) specs](https://fidoalliance.org/specs/cx/cxf-v1.0-rd-20250313.html) This represents a credential for a WiFi network..

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
struct WiFi
```

## Topics

### Initializers
- [init(ssid: ASImportableEditableField?, networkSecurityType: ASImportableEditableField?, passphrase: ASImportableEditableField?, hidden: ASImportableEditableField?)](./wifi/init%28ssid,networksecuritytype,passphrase,hidden%29.md)
### Instance Properties
- [var hidden: ASImportableEditableField?](./wifi/hidden.md)
- [var networkSecurityType: ASImportableEditableField?](./wifi/networksecuritytype.md)
- [var passphrase: ASImportableEditableField?](./wifi/passphrase.md)
- [var ssid: ASImportableEditableField?](./wifi/ssid.md)

## Relationships

### Conforms To
- [Decodable](../../Swift/decodable.md)
- [Encodable](../../Swift/encodable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asimportablecredential/wifi)*