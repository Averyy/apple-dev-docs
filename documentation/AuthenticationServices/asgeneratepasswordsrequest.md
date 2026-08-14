# ASGeneratePasswordsRequest

**Framework**: Authentication Services  
**Kind**: class

**Availability**:
- iOS 26.2+
- iPadOS 26.2+
- Mac Catalyst 26.2+
- visionOS 26.2+

## Declaration

```swift
class ASGeneratePasswordsRequest
```

## Topics

### Initializers
- [init?(coder: NSCoder)](asgeneratepasswordsrequest/init(coder:).md)
- [init(serviceIdentifier: ASCredentialServiceIdentifier, passwordFieldPasswordRules: String?, confirmPasswordFieldPasswordRules: String?, passwordRulesFromQuirks: String?)](asgeneratepasswordsrequest/init(serviceidentifier:passwordfieldpasswordrules:confirmpasswordfieldpasswordrules:passwordrulesfromquirks:).md)
### Instance Properties
- [var confirmPasswordFieldPasswordRules: String?](asgeneratepasswordsrequest/confirmpasswordfieldpasswordrules.md)
  Developer provided password rules for a “confirm password” field.
- [var passwordFieldPasswordRules: String?](asgeneratepasswordsrequest/passwordfieldpasswordrules.md)
  Developer provided password rules.
- [var passwordRulesFromQuirks: String?](asgeneratepasswordsrequest/passwordrulesfromquirks.md)
  Password rules from https://github.com/apple/password-manager-resources
- [var serviceIdentifier: ASCredentialServiceIdentifier](asgeneratepasswordsrequest/serviceidentifier.md)
  The identifier of the service for which the the credential would be associated.

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCoding](../foundation/nscoding.md)
- [NSCopying](../foundation/nscopying.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [NSSecureCoding](../foundation/nssecurecoding.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asgeneratepasswordsrequest)*