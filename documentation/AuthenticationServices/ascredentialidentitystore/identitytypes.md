# ASCredentialIdentityStore.IdentityTypes

**Framework**: Authentication Services  
**Kind**: struct

The defined identity types for use in retrieving credentials.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- macOS 14.4+
- visionOS 1.1+

## Declaration

```swift
struct IdentityTypes
```

## Topics

### Working with identity types
- [static var passkey: ASCredentialIdentityStore.IdentityTypes](ascredentialidentitystore/identitytypes/passkey.md)
  The passkey identity type.
- [static var password: ASCredentialIdentityStore.IdentityTypes](ascredentialidentitystore/identitytypes/password.md)
  The password identity type.
- [static var oneTimeCode: ASCredentialIdentityStore.IdentityTypes](ascredentialidentitystore/identitytypes/onetimecode.md)
  The one-time code identity type.
### Working with raw values
- [init(rawValue: UInt)](ascredentialidentitystore/identitytypes/init(rawvalue:).md)
  Creates an instance with the specified raw value.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [ASAuthorizationProviderExtensionLoginConfiguration.FederationType](asauthorizationproviderextensionloginconfiguration/federationtype-swift.enum.md)
- [ASAuthorizationProviderExtensionLoginConfiguration.UserSecureEnclaveKeyBiometricPolicy](asauthorizationproviderextensionloginconfiguration/usersecureenclavekeybiometricpolicy-swift.struct.md)
- [enum ASAuthorizationProviderExtensionPlatformSSOProtocolVersion](asauthorizationproviderextensionplatformssoprotocolversion.md)
- [struct ASAuthorizationProviderExtensionSupportedGrantTypes](asauthorizationproviderextensionsupportedgranttypes.md)
- [enum ASAuthorizationPublicKeyCredentialAttachment](asauthorizationpublickeycredentialattachment.md)
- [enum ASPublicKeyCredentialClientDataCrossOriginValue](aspublickeycredentialclientdatacrossoriginvalue.md)
- [enum ASUserAgeRange](asuseragerange.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/ascredentialidentitystore/identitytypes)*