# ASAuthorizationProviderExtensionLoginConfiguration.UserSecureEnclaveKeyBiometricPolicy

**Framework**: Authentication Services  
**Kind**: struct  
**Role**: Structure

**Availability**:
- macOS 10.15+

## Declaration

```swift
struct UserSecureEnclaveKeyBiometricPolicy
```

```c
enum ASAuthorizationProviderExtensionUserSecureEnclaveKeyBiometricPolicy : NSUInteger;
```

## Topics

### Initializers
- [init(rawValue: UInt)](./usersecureenclavekeybiometricpolicy-swift.struct/init%28rawvalue%29.md)
### Type Properties
- [static var passwordFallback: ASAuthorizationProviderExtensionLoginConfiguration.UserSecureEnclaveKeyBiometricPolicy](./usersecureenclavekeybiometricpolicy-swift.struct/passwordfallback.md)
- [static var reuseDuringUnlock: ASAuthorizationProviderExtensionLoginConfiguration.UserSecureEnclaveKeyBiometricPolicy](./usersecureenclavekeybiometricpolicy-swift.struct/reuseduringunlock.md)
- [static var touchIDOrWatchAny: ASAuthorizationProviderExtensionLoginConfiguration.UserSecureEnclaveKeyBiometricPolicy](./usersecureenclavekeybiometricpolicy-swift.struct/touchidorwatchany.md)
- [static var touchIDOrWatchCurrentSet: ASAuthorizationProviderExtensionLoginConfiguration.UserSecureEnclaveKeyBiometricPolicy](./usersecureenclavekeybiometricpolicy-swift.struct/touchidorwatchcurrentset.md)
### Constants
- [ASAuthorizationProviderExtensionUserSecureEnclaveKeyBiometricPolicyNone](../asauthorizationproviderextensionusersecureenclavekeybiometricpolicy/asauthorizationproviderextensionusersecureenclavekeybiometricpolicynone.md)

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
- [ASAuthorizationProviderExtensionLoginConfiguration.FederationType](./federationtype-swift.enum.md)
- [enum ASAuthorizationProviderExtensionPlatformSSOProtocolVersion](../asauthorizationproviderextensionplatformssoprotocolversion.md)
- [struct ASAuthorizationProviderExtensionSupportedGrantTypes](../asauthorizationproviderextensionsupportedgranttypes.md)
- [enum ASAuthorizationPublicKeyCredentialAttachment](../asauthorizationpublickeycredentialattachment.md)
- [ASCredentialIdentityStore.IdentityTypes](../ascredentialidentitystore/identitytypes.md)
  The defined identity types for use in retrieving credentials.
- [enum ASPublicKeyCredentialClientDataCrossOriginValue](../aspublickeycredentialclientdatacrossoriginvalue.md)
- [enum ASUserAgeRange](../asuseragerange.md)
- [ASAuthorizationPublicKeyCredentialLargeBlobAssertionOperation](../asauthorizationpublickeycredentiallargeblobassertionoperation.md)
  A type that represents the operation of the large blob assertion.
- [ASAuthorizationPublicKeyCredentialLargeBlobSupportRequirement](../asauthorizationpublickeycredentiallargeblobsupportrequirement.md)
  An enumeration of large binary object support requirement values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationproviderextensionloginconfiguration/usersecureenclavekeybiometricpolicy-swift.struct)*