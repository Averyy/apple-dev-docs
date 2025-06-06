# LAAuthenticationRequirement

**Framework**: Local Authentication  
**Kind**: class

A set of requirements that protect a right.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class LAAuthenticationRequirement
```

## Topics

### Specifying authentication requirements
- [class var `default`: LAAuthenticationRequirement](laauthenticationrequirement/default.md)
  The requirement that requires user authentication.
- [class var biometry: LAAuthenticationRequirement](laauthenticationrequirement/biometry.md)
  The requirement that requires biometric authentication.
- [class var biometryCurrentSet: LAAuthenticationRequirement](laauthenticationrequirement/biometrycurrentset.md)
  The requirement that requires user authentication with the current set of biometrics.
- [class func biometry(fallback: LABiometryFallbackRequirement) -> Self](laauthenticationrequirement/biometry(fallback:).md)
  Creates a requirement that requires biometric authentication or a fallback requirement that you specify.

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

- [class LABiometryFallbackRequirement](labiometryfallbackrequirement.md)
  A set of requirements to fall back on if biometrics aren’t present.


---

*[View on Apple Developer](https://developer.apple.com/documentation/localauthentication/laauthenticationrequirement)*