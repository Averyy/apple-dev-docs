# ASGeneratePasswordsRequest

**Framework**: Authentication Services  
**Kind**: class  
**Role**: Class

**Availability**:
- iOS 26.2+
- iPadOS 26.2+
- Mac Catalyst 26.2+
- visionOS 26.2+

## Declaration

```swift
class ASGeneratePasswordsRequest
```

```objc
@interface ASGeneratePasswordsRequest : NSObject
```

## Topics

### Initializers
- [init?(coder: NSCoder)](./asgeneratepasswordsrequest/init%28coder%29.md)
- [init(serviceIdentifier: ASCredentialServiceIdentifier, passwordFieldPasswordRules: String?, confirmPasswordFieldPasswordRules: String?, passwordRulesFromQuirks: String?)](./asgeneratepasswordsrequest/init%28serviceidentifier,passwordfieldpasswordrules,confirmpasswordfieldpasswordrules,passwordrulesfromquirks%29.md)
### Instance Properties
- [var confirmPasswordFieldPasswordRules: String?](./asgeneratepasswordsrequest/confirmpasswordfieldpasswordrules.md)
  Developer provided password rules for a “confirm password” field.
- [var passwordFieldPasswordRules: String?](./asgeneratepasswordsrequest/passwordfieldpasswordrules.md)
  Developer provided password rules.
- [var passwordRulesFromQuirks: String?](./asgeneratepasswordsrequest/passwordrulesfromquirks.md)
  Password rules from https://github.com/apple/password-manager-resources
- [var serviceIdentifier: ASCredentialServiceIdentifier](./asgeneratepasswordsrequest/serviceidentifier.md)
  The identifier of the service for which the the credential would be associated.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asgeneratepasswordsrequest)*