# ASAuthorizationRequest

**Framework**: Authentication Services  
**Kind**: class  
**Role**: Class

A base class for different kinds of authorization requests.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
class ASAuthorizationRequest
```

```objc
@interface ASAuthorizationRequest : NSObject
```

## Overview

Use one of the concrete requests, like [`ASAuthorizationAppleIDRequest`](./asauthorizationappleidrequest.md), [`ASAuthorizationPasswordRequest`](./asauthorizationpasswordrequest.md), or [`ASAuthorizationSingleSignOnRequest`](./asauthorizationsinglesignonrequest.md).

You typically generate one of these using the corresponding provider, which is an instance of [`ASAuthorizationAppleIDProvider`](./asauthorizationappleidprovider.md), [`ASAuthorizationPasswordProvider`](./asauthorizationpasswordprovider.md), or [`ASAuthorizationSingleSignOnProvider`](./asauthorizationsinglesignonprovider.md), respectively.

## Topics

### Inspecting the Provider
- [var provider: any ASAuthorizationProvider](./asauthorizationrequest/provider.md)
  The provider servicing the request.
- [protocol ASAuthorizationProvider](./asauthorizationprovider.md)
  An interface that authorization providers must implement.
### Initializers
- [init?(coder: NSCoder)](./asauthorizationrequest/init%28coder%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Inherited By
- [ASAuthorizationAccountCreationPlatformPublicKeyCredentialRequest](./asauthorizationaccountcreationplatformpublickeycredentialrequest.md)
- [ASAuthorizationOpenIDRequest](./asauthorizationopenidrequest.md)
- [ASAuthorizationPasswordRequest](./asauthorizationpasswordrequest.md)
- [ASAuthorizationPlatformPublicKeyCredentialAssertionRequest](./asauthorizationplatformpublickeycredentialassertionrequest.md)
- [ASAuthorizationPlatformPublicKeyCredentialRegistrationRequest](./asauthorizationplatformpublickeycredentialregistrationrequest.md)
- [ASAuthorizationSecurityKeyPublicKeyCredentialAssertionRequest](./asauthorizationsecuritykeypublickeycredentialassertionrequest.md)
- [ASAuthorizationSecurityKeyPublicKeyCredentialRegistrationRequest](./asauthorizationsecuritykeypublickeycredentialregistrationrequest.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Inspecting requests
- [var authorizationRequests: [ASAuthorizationRequest]](./asauthorizationcontroller/authorizationrequests.md)
  The authorization requests that the controller manages.
- [var customAuthorizationMethods: [ASAuthorizationCustomMethod]](./asauthorizationcontroller/customauthorizationmethods.md)
  An array of custom authorization methods for the user to choose.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationrequest)*