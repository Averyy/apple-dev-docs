# ASCredentialIdentityStore.IdentityTypes

**Framework**: Authentication Services  
**Kind**: struct  
**Role**: Structure

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

```c
enum ASCredentialIdentityTypes : NSUInteger;
```

## Topics

### Working with identity types
- [static var passkey: ASCredentialIdentityStore.IdentityTypes](./identitytypes/passkey.md)
  The passkey identity type.
- [static var password: ASCredentialIdentityStore.IdentityTypes](./identitytypes/password.md)
  The password identity type.
- [static var oneTimeCode: ASCredentialIdentityStore.IdentityTypes](./identitytypes/onetimecode.md)
  The one-time code identity type.
### Working with raw values
- [init(rawValue: UInt)](./identitytypes/init%28rawvalue%29.md)
  Creates an instance with the specified raw value.
### Matching any type
- [ASCredentialIdentityTypesAll](../ascredentialidentitytypes/ascredentialidentitytypesall.md)
  A value that matches all identity types.

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../../Swift/optionset.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)
- [SetAlgebra](../../Swift/setalgebra.md)

## See Also

### Enumerations
- [ASAuthorizationProviderExtensionLoginConfiguration.FederationType](../asauthorizationproviderextensionloginconfiguration/federationtype-swift.enum.md)
- [ASAuthorizationProviderExtensionLoginConfiguration.UserSecureEnclaveKeyBiometricPolicy](../asauthorizationproviderextensionloginconfiguration/usersecureenclavekeybiometricpolicy-swift.struct.md)
- [enum ASAuthorizationProviderExtensionPlatformSSOProtocolVersion](../asauthorizationproviderextensionplatformssoprotocolversion.md)
- [struct ASAuthorizationProviderExtensionSupportedGrantTypes](../asauthorizationproviderextensionsupportedgranttypes.md)
- [enum ASAuthorizationPublicKeyCredentialAttachment](../asauthorizationpublickeycredentialattachment.md)
- [enum ASPublicKeyCredentialClientDataCrossOriginValue](../aspublickeycredentialclientdatacrossoriginvalue.md)
- [enum ASUserAgeRange](../asuseragerange.md)
- [ASAuthorizationPublicKeyCredentialLargeBlobAssertionOperation](../asauthorizationpublickeycredentiallargeblobassertionoperation.md)
  A type that represents the operation of the large blob assertion.
- [ASAuthorizationPublicKeyCredentialLargeBlobSupportRequirement](../asauthorizationpublickeycredentiallargeblobsupportrequirement.md)
  An enumeration of large binary object support requirement values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/ascredentialidentitystore/identitytypes)*