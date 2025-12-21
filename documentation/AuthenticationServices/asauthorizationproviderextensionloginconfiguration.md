# ASAuthorizationProviderExtensionLoginConfiguration

**Framework**: Authentication Services  
**Kind**: class

An interface for configuring platform single sign-on.

**Availability**:
- macOS 13.0+

## Declaration

```swift
class ASAuthorizationProviderExtensionLoginConfiguration
```

## Mentions

- [Creating extensions that support Platform SSO](creating-extensions-that-support-platform-sso.md)

#### Overview

This class provides login configuration information for platform single sign-on.

## Topics

### Creating the configuration
- [init(clientID: String, issuer: String, tokenEndpointURL: URL, jwksEndpointURL: URL, audience: String?)](asauthorizationproviderextensionloginconfiguration/init(clientid:issuer:tokenendpointurl:jwksendpointurl:audience:).md)
  Creates a configuration with the required values.
- [class func configuration(openIDConfigurationURL: URL, clientID: String, issuer: String?, completion: (ASAuthorizationProviderExtensionLoginConfiguration?, (any Error)?) -> Void)](asauthorizationproviderextensionloginconfiguration/configuration(openidconfigurationurl:clientid:issuer:completion:).md)
  Creates a login configuration using the OpenID configuration.
### Obtaining the required configuration
- [var audience: String](asauthorizationproviderextensionloginconfiguration/audience.md)
  The audience for validation and requests.
- [var clientID: String](asauthorizationproviderextensionloginconfiguration/clientid.md)
  The identifier for the client at the identity provider.
- [var jwksEndpointURL: URL](asauthorizationproviderextensionloginconfiguration/jwksendpointurl.md)
  The JSON Web Key Set endpoint URL for keys.
- [var tokenEndpointURL: URL](asauthorizationproviderextensionloginconfiguration/tokenendpointurl.md)
  The token endpoint URL for login requests.
- [var issuer: String](asauthorizationproviderextensionloginconfiguration/issuer.md)
  The issuer of the identity token that the identity provider returns.
### Obtaining the recommended configuration
- [var accountDisplayName: String?](asauthorizationproviderextensionloginconfiguration/accountdisplayname.md)
  The display name for the account.
- [var invalidCredentialPredicate: String?](asauthorizationproviderextensionloginconfiguration/invalidcredentialpredicate.md)
  The predicate string that identifies invalid credential errors.
### Configuring the server nonce
- [var customNonceRequestValues: [URLQueryItem]](asauthorizationproviderextensionloginconfiguration/customnoncerequestvalues.md)
  Custom values to add to the server nonce POST request body.
- [var nonceEndpointURL: URL](asauthorizationproviderextensionloginconfiguration/nonceendpointurl.md)
  The URL to retrieve a one-time use value from the server.
- [var nonceResponseKeypath: String](asauthorizationproviderextensionloginconfiguration/nonceresponsekeypath.md)
  The keypath in the response that contains the one-time use value.
- [var serverNonceClaimName: String](asauthorizationproviderextensionloginconfiguration/servernonceclaimname.md)
  The name of the claim to include in authentication requests.
### Configuring the previous refresh token
- [var includePreviousRefreshTokenInLoginRequest: Bool](asauthorizationproviderextensionloginconfiguration/includepreviousrefreshtokeninloginrequest.md)
  A Boolean value that indicates whether to include the previous refresh token in the authentation request.
- [var previousRefreshTokenClaimName: String](asauthorizationproviderextensionloginconfiguration/previousrefreshtokenclaimname.md)
  The claim name for the previous single sign-on token value in the authentication request.
### Customizing the authentication request
- [func setCustomAssertionRequestBodyClaims([String : Any]) throws](asauthorizationproviderextensionloginconfiguration/setcustomassertionrequestbodyclaims(_:).md)
  Adds the custom claims to the embedded assertion request body.
- [func setCustomAssertionRequestHeaderClaims([String : Any]) throws](asauthorizationproviderextensionloginconfiguration/setcustomassertionrequestheaderclaims(_:).md)
  Adds the custom claims to the embedded assertion request header.
- [func setCustomLoginRequestBodyClaims([String : Any]) throws](asauthorizationproviderextensionloginconfiguration/setcustomloginrequestbodyclaims(_:).md)
  Adds the custom claims to the login request body.
- [func setCustomLoginRequestHeaderClaims([String : Any]) throws](asauthorizationproviderextensionloginconfiguration/setcustomloginrequestheaderclaims(_:).md)
  Adds the custom claims to the login request header.
- [var additionalScopes: String](asauthorizationproviderextensionloginconfiguration/additionalscopes.md)
  A set of extra scopes to add to the base for the authentication request.
- [var customLoginRequestValues: [URLQueryItem]](asauthorizationproviderextensionloginconfiguration/customloginrequestvalues.md)
  Provider-supplied values to add to the login POST request body.
- [var kerberosTicketMappings: [ASAuthorizationProviderExtensionKerberosMapping]](asauthorizationproviderextensionloginconfiguration/kerberosticketmappings.md)
  The set of ticket mappings the system uses to import Kerberos tickets from the single sign-on token.
### Instance Properties
- [var additionalAuthorizationScopes: String?](asauthorizationproviderextensionloginconfiguration/additionalauthorizationscopes.md)
- [var customFederationUserPreauthenticationRequestValues: [URLQueryItem]](asauthorizationproviderextensionloginconfiguration/customfederationuserpreauthenticationrequestvalues.md)
- [var customKeyExchangeRequestValues: [URLQueryItem]](asauthorizationproviderextensionloginconfiguration/customkeyexchangerequestvalues.md)
- [var customKeyRequestValues: [URLQueryItem]](asauthorizationproviderextensionloginconfiguration/customkeyrequestvalues.md)
- [var customRefreshRequestValues: [URLQueryItem]](asauthorizationproviderextensionloginconfiguration/customrefreshrequestvalues.md)
- [var customRequestJWTParameterName: String?](asauthorizationproviderextensionloginconfiguration/customrequestjwtparametername.md)
- [var deviceContext: Data?](asauthorizationproviderextensionloginconfiguration/devicecontext.md)
- [var federationMEXURL: URL?](asauthorizationproviderextensionloginconfiguration/federationmexurl.md)
- [var federationMEXURLKeypath: String?](asauthorizationproviderextensionloginconfiguration/federationmexurlkeypath.md)
- [var federationPredicate: String?](asauthorizationproviderextensionloginconfiguration/federationpredicate.md)
- [var federationRequestURN: String?](asauthorizationproviderextensionloginconfiguration/federationrequesturn.md)
- [var federationType: ASAuthorizationProviderExtensionLoginConfiguration.FederationType](asauthorizationproviderextensionloginconfiguration/federationtype-swift.property.md)
- [var federationUserPreauthenticationURL: URL?](asauthorizationproviderextensionloginconfiguration/federationuserpreauthenticationurl.md)
- [var groupRequestClaimName: String?](asauthorizationproviderextensionloginconfiguration/grouprequestclaimname.md)
- [var groupResponseClaimName: String?](asauthorizationproviderextensionloginconfiguration/groupresponseclaimname.md)
- [var jwksTrustedRootCertificates: [SecCertificate]](asauthorizationproviderextensionloginconfiguration/jwkstrustedrootcertificates-5y2pc.md)
- [var keyEndpointURL: URL?](asauthorizationproviderextensionloginconfiguration/keyendpointurl.md)
- [var loginRequestEncryptionAPVPrefix: Data?](asauthorizationproviderextensionloginconfiguration/loginrequestencryptionapvprefix.md)
- [var loginRequestEncryptionPublicKey: SecKey?](asauthorizationproviderextensionloginconfiguration/loginrequestencryptionpublickey.md)
- [var refreshEndpointURL: URL?](asauthorizationproviderextensionloginconfiguration/refreshendpointurl.md)
- [var uniqueIdentifierClaimName: String?](asauthorizationproviderextensionloginconfiguration/uniqueidentifierclaimname.md)
- [var userSecureEnclaveKeyBiometricPolicy: ASAuthorizationProviderExtensionLoginConfiguration.UserSecureEnclaveKeyBiometricPolicy](asauthorizationproviderextensionloginconfiguration/usersecureenclavekeybiometricpolicy-swift.property.md)
- [var hpkeAuthPublicKey: SecKey?](asauthorizationproviderextensionloginconfiguration/hpkeauthpublickey.md)
- [var hpkePreSharedKey: Data?](asauthorizationproviderextensionloginconfiguration/hpkepresharedkey.md)
- [var hpkePreSharedKeyID: Data?](asauthorizationproviderextensionloginconfiguration/hpkepresharedkeyid.md)
- [var loginRequestEncryptionAlgorithm: ASAuthorizationProviderExtensionEncryptionAlgorithm](asauthorizationproviderextensionloginconfiguration/loginrequestencryptionalgorithm.md)
- [var loginRequestHPKEPreSharedKey: Data?](asauthorizationproviderextensionloginconfiguration/loginrequesthpkepresharedkey.md)
- [var loginRequestHPKEPreSharedKeyID: Data?](asauthorizationproviderextensionloginconfiguration/loginrequesthpkepresharedkeyid.md)
### Instance Methods
- [func setCustomKeyExchangeRequestBodyClaims([String : Any]) throws](asauthorizationproviderextensionloginconfiguration/setcustomkeyexchangerequestbodyclaims(_:).md)
- [func setCustomKeyExchangeRequestHeaderClaims([String : Any]) throws](asauthorizationproviderextensionloginconfiguration/setcustomkeyexchangerequestheaderclaims(_:).md)
- [func setCustomKeyRequestBodyClaims([String : Any]) throws](asauthorizationproviderextensionloginconfiguration/setcustomkeyrequestbodyclaims(_:).md)
- [func setCustomKeyRequestHeaderClaims([String : Any]) throws](asauthorizationproviderextensionloginconfiguration/setcustomkeyrequestheaderclaims(_:).md)
- [func setCustomRefreshRequestBodyClaims([String : Any]) throws](asauthorizationproviderextensionloginconfiguration/setcustomrefreshrequestbodyclaims(_:).md)
- [func setCustomRefreshRequestHeaderClaims([String : Any]) throws](asauthorizationproviderextensionloginconfiguration/setcustomrefreshrequestheaderclaims(_:).md)
### Structures
- [ASAuthorizationProviderExtensionLoginConfiguration.UserSecureEnclaveKeyBiometricPolicy](asauthorizationproviderextensionloginconfiguration/usersecureenclavekeybiometricpolicy-swift.struct.md)
### Enumerations
- [ASAuthorizationProviderExtensionLoginConfiguration.FederationType](asauthorizationproviderextensionloginconfiguration/federationtype-swift.enum.md)

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

- [Configuring Device Management](configuring-device-management.md)
  Configure Device Management to support device and user registration for Platform SSO.
- [Configuring authentication with the identity provider (IdP)](configuring-authentication-with-the-identity-provider-idp.md)
  Specify how Platform SSO authenticates with the identity provider.
- [class ASAuthorizationProviderExtensionLoginManager](asauthorizationproviderextensionloginmanager.md)
  An interface to maintain platform single sign-on (SSO) during authentication and registration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationproviderextensionloginconfiguration)*