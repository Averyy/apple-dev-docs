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
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asgeneratepasswordsrequest)*