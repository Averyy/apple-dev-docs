# Public-Private Key Authentication

**Framework**: Authentication Services

Register and authenticate users with passkeys and security keys, without using passwords.

#### Overview

Eliminating passwords simplifies account creation and authentication for apps and websites. Additionally, it reduces risks that arise from the reuse of one password across multiple services, brute force attacks, and social engineering that bad actors use to obtain credential information. By implementing public-private authentication according to the [`W3C Web Authentication`](https://developer.apple.comhttps://www.w3.org/TR/webauthn-2/) specification, your users no longer need to remember complicated passwords or rely on password managers.

Instead of using a password, your macOS, iOS, or iPadOS device, known as the , generates a public-private key pair at account creation time, and sends the public key to the server. The server, known as the , holds the public key for subsequent authentication, and uses  to challenge the authenticator to prove its identity is valid.

There are two forms of public-private key authentication:  and  With passkeys, the device stores its public-private key pair in the user’s iCloud Keychain and syncs the keys across the user’s devices. Security keys store the public-private key pair on a physical medium, such as a security card or a USB key.

## Topics

### Fundamentals
- [Connecting to a service with passkeys](connecting-to-a-service-with-passkeys.md)
  Allow users to sign in to a service without typing a password.
- [Supporting passkeys](supporting-passkeys.md)
  Eliminate passwords for your users when they sign in to apps and websites.
- [Supporting Security Key Authentication Using Physical Keys](supporting-security-key-authentication-using-physical-keys.md)
  Allow users to authenticate using NFC, USB, and Lightning security keys in your app or service.
### Account registration
- [protocol ASAuthorizationPublicKeyCredentialRegistration](asauthorizationpublickeycredentialregistration.md)
  An interface that credential registration requests adhere to.
- [class ASAuthorizationPlatformPublicKeyCredentialRegistration](asauthorizationplatformpublickeycredentialregistration.md)
  A newly created platform credential that results from a credential registration request.
- [class ASAuthorizationSecurityKeyPublicKeyCredentialRegistration](asauthorizationsecuritykeypublickeycredentialregistration.md)
  A newly created security key credential that results from a credential registration request.
- [protocol ASAuthorizationPublicKeyCredentialRegistrationRequest](asauthorizationpublickeycredentialregistrationrequest.md)
  An interface that defines properties for a credential registration request.
- [class ASAuthorizationPlatformPublicKeyCredentialRegistrationRequest](asauthorizationplatformpublickeycredentialregistrationrequest.md)
  The object for registering a new platform public key credential.
- [class ASAuthorizationSecurityKeyPublicKeyCredentialRegistrationRequest](asauthorizationsecuritykeypublickeycredentialregistrationrequest.md)
  The object for registering a new security key credential.
### Account authentication
- [protocol ASAuthorizationPublicKeyCredentialAssertion](asauthorizationpublickeycredentialassertion.md)
  An interface for establishing a public key-based assertion.
- [class ASAuthorizationPlatformPublicKeyCredentialAssertion](asauthorizationplatformpublickeycredentialassertion.md)
  A class that represents the platform credential assertion type.
- [class ASAuthorizationSecurityKeyPublicKeyCredentialAssertion](asauthorizationsecuritykeypublickeycredentialassertion.md)
  A class that represents the security key credential assertion type.
- [protocol ASAuthorizationPublicKeyCredentialAssertionRequest](asauthorizationpublickeycredentialassertionrequest.md)
  An interface for requesting a public key-based credential assertion.
- [class ASAuthorizationPlatformPublicKeyCredentialAssertionRequest](asauthorizationplatformpublickeycredentialassertionrequest.md)
  The concrete assertion request type for platform credentials.
- [class ASAuthorizationSecurityKeyPublicKeyCredentialAssertionRequest](asauthorizationsecuritykeypublickeycredentialassertionrequest.md)
  A class that defines the assertion request type for security key credentials.
### Credential providers
- [class ASAuthorizationPlatformPublicKeyCredentialProvider](asauthorizationplatformpublickeycredentialprovider.md)
  A mechanism for providing public key credential requests to an app or service with iCloud Keychain.
- [class ASAuthorizationSecurityKeyPublicKeyCredentialProvider](asauthorizationsecuritykeypublickeycredentialprovider.md)
  A mechanism for providing public key credential requests to an app or service with a physical security key.
### Request configuration
- [protocol ASPublicKeyCredential](aspublickeycredential.md)
  An interface that defines the properties of the public key.
- [class ASAuthorizationPublicKeyCredentialParameters](asauthorizationpublickeycredentialparameters.md)
  An object that provides required parameters for the credential during registration.
- [struct ASCOSEAlgorithmIdentifier](ascosealgorithmidentifier.md)
  An identifier for the algorithm that a credential’s key pair uses.
- [struct ASCOSEEllipticCurveIdentifier](ascoseellipticcurveidentifier.md)
  A structure that contains the elliptic curve identifier.
- [struct ASAuthorizationPublicKeyCredentialAttestationKind](asauthorizationpublickeycredentialattestationkind.md)
  A structure that defines the types of attestations a developer can request.
- [struct ASAuthorizationPublicKeyCredentialResidentKeyPreference](asauthorizationpublickeycredentialresidentkeypreference.md)
  A structure that specifies the relying party’s preference for resident key storage.
- [struct ASAuthorizationPublicKeyCredentialUserVerificationPreference](asauthorizationpublickeycredentialuserverificationpreference.md)
  A structure that defines the relying party’s user verification preference.
- [protocol ASAuthorizationPublicKeyCredentialDescriptor](asauthorizationpublickeycredentialdescriptor.md)
  An interface that defines the credential identifier.
- [class ASAuthorizationPlatformPublicKeyCredentialDescriptor](asauthorizationplatformpublickeycredentialdescriptor.md)
  An object that holds the credential.
- [class ASAuthorizationSecurityKeyPublicKeyCredentialDescriptor](asauthorizationsecuritykeypublickeycredentialdescriptor.md)
  An object that holds public key credential transport information.
- [ASAuthorizationSecurityKeyPublicKeyCredentialDescriptor.Transport](asauthorizationsecuritykeypublickeycredentialdescriptor/transport.md)
  A structure that defines the security key credential transport type.
- [static var allSupported: [ASAuthorizationSecurityKeyPublicKeyCredentialDescriptor.Transport]](asauthorizationsecuritykeypublickeycredentialdescriptor/transport/allsupported.md)
  An array of currently supported transport types.

## See Also

- [Passkey use in web browsers](passkey-use-in-web-browsers.md)
  Register and authenticate website users by using passkeys.
- [Connecting to a service with passkeys](connecting-to-a-service-with-passkeys.md)
  Allow users to sign in to a service without typing a password.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/public-private-key-authentication)*