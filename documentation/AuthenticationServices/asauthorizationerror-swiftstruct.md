# ASAuthorizationError

**Framework**: Authentication Services  
**Kind**: struct

Errors that can occur during authorization.

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
struct ASAuthorizationError
```

## Topics

### Getting the Properties
- [static var notInteractive: ASAuthorizationError.Code](asauthorizationerror-swift.struct/notinteractive.md)
### Error Domain
- [let ASAuthorizationErrorDomain: String](asauthorizationerrordomain.md)
  The domain of authorization errors.
### Error Codes
- [static var canceled: ASAuthorizationError.Code](asauthorizationerror-swift.struct/canceled.md)
  The user canceled the authorization attempt.
- [static var failed: ASAuthorizationError.Code](asauthorizationerror-swift.struct/failed.md)
  The authorization attempt failed.
- [static var invalidResponse: ASAuthorizationError.Code](asauthorizationerror-swift.struct/invalidresponse.md)
  The authorization request received an invalid response.
- [static var notHandled: ASAuthorizationError.Code](asauthorizationerror-swift.struct/nothandled.md)
  The authorization request wasn’t handled.
- [static var unknown: ASAuthorizationError.Code](asauthorizationerror-swift.struct/unknown.md)
  The authorization attempt failed for an unknown reason.
- [static var credentialExport: ASAuthorizationError.Code](asauthorizationerror-swift.struct/credentialexport.md)
  The credential export request failed.
- [static var credentialImport: ASAuthorizationError.Code](asauthorizationerror-swift.struct/credentialimport.md)
  The credential import request failed.
- [ASAuthorizationError.Code](asauthorizationerror-swift.struct/code.md)
  Codes that authorization errors can have.
### Type Properties
- [static var deviceNotConfiguredForPasskeyCreation: ASAuthorizationError.Code](asauthorizationerror-swift.struct/devicenotconfiguredforpasskeycreation.md)
- [static var errorDomain: String](asauthorizationerror-swift.struct/errordomain.md)
- [static var matchedExcludedCredential: ASAuthorizationError.Code](asauthorizationerror-swift.struct/matchedexcludedcredential.md)
- [static var preferSignInWithApple: ASAuthorizationError.Code](asauthorizationerror-swift.struct/prefersigninwithapple.md)

## Relationships

### Conforms To
- [CustomNSError](../Foundation/CustomNSError.md)
- [Equatable](../Swift/Equatable.md)
- [Error](../Swift/Error.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func authorizationController(controller: ASAuthorizationController, didCompleteWithError: any Error)](asauthorizationcontrollerdelegate/authorizationcontroller(controller:didcompletewitherror:).md)
  Tells the delegate when authorization fails, and provides an error explaining why.
- [let ASAuthorizationErrorDomain: String](asauthorizationerrordomain.md)
  The domain of authorization errors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationerror-swift.struct)*