# Security

**Framework**: Security  
**Kind**: module

Secure the data your app manages, and control access to your app.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

#### Overview

Use the Security framework to protect information, establish trust, and control access to software. Broadly, security services support these goals:

- Establish a user’s identity (authentication) and then selectively grant access to resources (authorization).
- Secure data, both on disk and in motion across a network connection.
- Ensure the validity of code to be executed for a particular purpose.

As shown in the image below, you can also use lower level cryptographic resources to create new secure services. Cryptography is difficult and the cost of bugs typically so high that it’s rarely a good idea to implement your own cryptography solution. Rely on the Security framework when you need cryptography in your app.

![Diagram showing your app sitting above the Security framework, which provides tools to enable secure interaction with users, data, and code.](https://docs-assets.developer.apple.com/published/c89145031becb4c02e98769e238d4f25/media-2891898%402x.png)

> **Note**:  Always use the highest level API that meets your needs. The Security framework is not always your best option. For example, to conduct secure network communications, start by considering the [`Foundation`](https://developer.apple.com/documentation/Foundation) framework’s [`URL Loading System`](https://developer.apple.com/documentation/Foundation/url-loading-system), which builds on the Security framework. Only if your app requires lower level access to security protocol functions would you use the secure transport API directly.

 Always use the highest level API that meets your needs. The Security framework is not always your best option. For example, to conduct secure network communications, start by considering the [`Foundation`](https://developer.apple.com/documentation/Foundation) framework’s [`URL Loading System`](https://developer.apple.com/documentation/Foundation/url-loading-system), which builds on the Security framework. Only if your app requires lower level access to security protocol functions would you use the secure transport API directly.

## Topics

### Essentials
- [Security updates](../Updates/Security.md)
  Learn about important changes to Security.
### Authorization and authentication
- [Password AutoFill](password-autofill.md)
  Streamline your app’s login and onboarding procedures.
- [Shared Web Credentials](shared-web-credentials.md)
  Share credentials between iOS apps and their website counterparts.
- [Authorization Services](authorization-services.md)
  Access restricted areas of the operating system, and control access to particular features of your macOS app.
- [Authorization Plug-ins](authorization-plug-ins.md)
  Extend the authorization services API by creating plug-ins that can participate in authorization decisions.
- [Sessions](sessions.md)
  Manage login, authorization, and security sessions in macOS.
- [One-time codes](one-time-codes.md)
  Streamline entry of authentication and recovery codes.
### Secure data
- [Keychain services](keychain-services.md)
  Securely store small chunks of data on behalf of the user.
- [Preventing Insecure Network Connections](preventing-insecure-network-connections.md)
  Enforce secure network links in your app by relying on App Transport Security.
### Secure code
- [Code Signing Services](code-signing-services.md)
  Examine and validate signed code running on the system.
- [Notarizing macOS software before distribution](notarizing-macos-software-before-distribution.md)
  Give users even more confidence in your macOS software by submitting it to Apple for notarization.
- [Preparing your app to work with pointer authentication](preparing-your-app-to-work-with-pointer-authentication.md)
  Test your app against the arm64e architecture to ensure that it works seamlessly with enhanced security features.
- [App Sandbox](app-sandbox.md)
  Restrict access to system resources and user data in macOS apps to contain damage if an app becomes compromised.
- [Hardened Runtime](hardened-runtime.md)
  Manage security protections and resource access for your macOS apps.
- [Disabling and Enabling System Integrity Protection](disabling-and-enabling-system-integrity-protection.md)
  Disable system protections only temporarily during development to test drivers, kernel extensions, and other low-level code.
- [Using the latest code signature format](../Xcode/using-the-latest-code-signature-format.md)
  Update legacy app code signatures so your app runs on current OS releases.
- [Updating Mac Software](updating-mac-software.md)
  Implement Mac software updates without causing code-signing crashes.
- [TN3125: Inside Code Signing: Provisioning Profiles](../Technotes/tn3125-inside-code-signing-provisioning-profiles.md)
  Learn how provisioning profiles enable third-party code to run on Apple platforms.
### Launch environment constraints
- [Applying launch environment and library constraints](applying-launch-environment-and-library-constraints.md)
  Limit the libraries your process loads, and the situations where it runs.
- [Defining launch environment and library constraints](defining-launch-environment-and-library-constraints.md)
  Restrict your app’s components to their expected contexts.
- [Constraining a tool’s launch environment](constraining-a-tool's-launch-environment.md)
  Improve the security of your macOS app by limiting the ways its components can run.
### Cryptography
- [Complying with Encryption Export Regulations](complying-with-encryption-export-regulations.md)
  Declare the use of encryption in your app to streamline the app submission process.
- [Certificate, Key, and Trust Services](certificate-key-and-trust-services.md)
  Establish trust using certificates and cryptographic keys.
- [Cryptographic Message Syntax Services](cryptographic-message-syntax-services.md)
  Cryptographically sign and encrypt S/MIME messages.
- [Randomization Services](randomization-services.md)
  Generate cryptographically secure random numbers.
- [Security Transforms](security-transforms.md)
  Perform cryptographic functions like encoding, encryption, signing, and signature verification.
- [ASN.1](asn-1.md)
  Encode and decode Distinguished Encoding Rules (DER) and Basic Encoding Rules (BER) data streams.
### Result codes
- [Security Framework Result Codes](security-framework-result-codes.md)
  Evaluate result codes common to many Security framework functions.
### Legacy interfaces
- [Common Security Services Manager](common-security-services-manager.md)
  A set of open source modules underpinning the legacy implementation of the Security framework.
- [Secure Transport](secure-transport.md)
  Secure network communication using standardized transport layer security mechanisms.
- [Secure Download](secure-download.md)
  Implement Apple’s Secure Download System in macOS.
- [Security legacy reference](security-legacy-reference.md)
  Learn about legacy APIs.
### Reference
- [Security Structures](security-structures.md)
- [Security Constants](security-constants.md)
- [Security Functions](security-functions.md)
- [Security Data Types](security-data-types.md)
### Variables
- [var TLS_ECDHE_PSK_WITH_CHACHA20_POLY1305_SHA256: SSLCipherSuite](tls_ecdhe_psk_with_chacha20_poly1305_sha256.md)
- [var errSecMissingQualifiedCertStatement: OSStatus](errsecmissingqualifiedcertstatement.md)
- [let kSecPolicyAppleEAPClient: CFString](ksecpolicyappleeapclient.md)
- [let kSecPolicyAppleEAPServer: CFString](ksecpolicyappleeapserver.md)
- [let kSecPolicyAppleIPSecClient: CFString](ksecpolicyappleipsecclient.md)
- [let kSecPolicyAppleIPSecServer: CFString](ksecpolicyappleipsecserver.md)
- [let kSecPolicyAppleSSLClient: CFString](ksecpolicyapplesslclient.md)
- [let kSecPolicyAppleSSLServer: CFString](ksecpolicyapplesslserver.md)
- [let kSecTrustQCStatements: CFString](ksectrustqcstatements.md)
- [let kSecTrustQWACValidation: CFString](ksectrustqwacvalidation.md)
### Functions
- [func sec_protocol_metadata_copy_negotiated_protocol(sec_protocol_metadata_t) -> UnsafePointer<CChar>?](sec_protocol_metadata_copy_negotiated_protocol(_:).md)
- [func sec_protocol_metadata_copy_server_name(sec_protocol_metadata_t) -> UnsafePointer<CChar>?](sec_protocol_metadata_copy_server_name(_:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/Security)*