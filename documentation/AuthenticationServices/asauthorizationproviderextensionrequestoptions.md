# ASAuthorizationProviderExtensionRequestOptions

**Framework**: Authentication Services  
**Kind**: struct  
**Role**: Structure

The options for the extension to obtain the status of the registration.

**Availability**:
- macOS 13.0+

## Declaration

```swift
struct ASAuthorizationProviderExtensionRequestOptions
```

```c
enum ASAuthorizationProviderExtensionRequestOptions : NSUInteger;
```

## Topics

### Creating the options
- [init(rawValue: UInt)](./asauthorizationproviderextensionrequestoptions/init%28rawvalue%29.md)
  Creates the request options.
### Identifying the options
- [static var registrationRepair: ASAuthorizationProviderExtensionRequestOptions](./asauthorizationproviderextensionrequestoptions/registrationrepair.md)
  Indicates that the registration is undergoing repair.
- [static var userInteractionEnabled: ASAuthorizationProviderExtensionRequestOptions](./asauthorizationproviderextensionrequestoptions/userinteractionenabled.md)
  Indicates that the user interface is in an enabled state.
- [ASAuthorizationProviderExtensionRequestOptionsNone](./asauthorizationproviderextensionrequestoptions/asauthorizationproviderextensionrequestoptionsnone.md)
  Options aren’t available.
### Type Properties
- [static var registrationDeviceKeyMigration: ASAuthorizationProviderExtensionRequestOptions](./asauthorizationproviderextensionrequestoptions/registrationdevicekeymigration.md)
- [static var registrationSharedDeviceKeys: ASAuthorizationProviderExtensionRequestOptions](./asauthorizationproviderextensionrequestoptions/registrationshareddevicekeys.md)
- [static var userKeyInvalid: ASAuthorizationProviderExtensionRequestOptions](./asauthorizationproviderextensionrequestoptions/userkeyinvalid.md)
- [static var setupAssistant: ASAuthorizationProviderExtensionRequestOptions](./asauthorizationproviderextensionrequestoptions/setupassistant.md)
- [static var strongerKeyAvailable: ASAuthorizationProviderExtensionRequestOptions](./asauthorizationproviderextensionrequestoptions/strongerkeyavailable.md)
### Enumeration Cases
- [ASAuthorizationProviderExtensionRequestOptionsOpenIDFallback](./asauthorizationproviderextensionrequestoptions/asauthorizationproviderextensionrequestoptionsopenidfallback.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../Swift/optionset.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [SetAlgebra](../Swift/setalgebra.md)

## See Also

### Essentials
- [Creating extensions that support Platform SSO](./creating-extensions-that-support-platform-sso.md)
  Configure capabilities and authentication options for extensions.
- [Registering devices and users](./registering-devices-and-users.md)
  Implement device and user registration.
- [protocol ASAuthorizationProviderExtensionRegistrationHandler](./asauthorizationproviderextensionregistrationhandler.md)
  An interface through which a single sign-on (SSO) authentication provider extension registers users and devices for platform SSO.
- [enum ASAuthorizationProviderExtensionAuthenticationMethod](./asauthorizationproviderextensionauthenticationmethod.md)
  The platform single sign-on method for the user.
- [enum ASAuthorizationProviderExtensionRegistrationResult](./asauthorizationproviderextensionregistrationresult.md)
  The registration result.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationproviderextensionrequestoptions)*