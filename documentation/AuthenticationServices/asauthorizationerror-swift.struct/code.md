# ASAuthorizationError.Code

**Framework**: Authentication Services  
**Kind**: enum

Codes that authorization errors can have.

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
enum Code
```

## Topics

### Codes
- [ASAuthorizationError.Code.canceled](asauthorizationerror-swift.struct/code/canceled.md)
  The user canceled the authorization attempt.
- [ASAuthorizationError.Code.failed](asauthorizationerror-swift.struct/code/failed.md)
  The authorization attempt failed.
- [ASAuthorizationError.Code.invalidResponse](asauthorizationerror-swift.struct/code/invalidresponse.md)
  The authorization request received an invalid response.
- [ASAuthorizationError.Code.notHandled](asauthorizationerror-swift.struct/code/nothandled.md)
  The authorization request wasn’t handled.
- [ASAuthorizationError.Code.unknown](asauthorizationerror-swift.struct/code/unknown.md)
  The authorization attempt failed for an unknown reason.
- [ASAuthorizationError.Code.notInteractive](asauthorizationerror-swift.struct/code/notinteractive.md)
  The authorization request isn’t interactive.
- [ASAuthorizationError.Code.credentialExport](asauthorizationerror-swift.struct/code/credentialexport.md)
  The credential export request failed.
- [ASAuthorizationError.Code.credentialImport](asauthorizationerror-swift.struct/code/credentialimport.md)
  The credential import request failed.
### Enumeration Cases
- [ASAuthorizationError.Code.matchedExcludedCredential](asauthorizationerror-swift.struct/code/matchedexcludedcredential.md)
  This error should only be returned when specifying @c excludedCredentials on a public key credential registration request.
### Initializers
- [init?(rawValue: Int)](asauthorizationerror-swift.struct/code/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationerror-swift.struct/code)*