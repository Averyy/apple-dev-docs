# LAAuthenticationRequirement

**Framework**: Local Authentication  
**Kind**: class  
**Role**: Class

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

```objc
@interface LAAuthenticationRequirement : NSObject
```

## Topics

### Specifying authentication requirements
- [class var `default`: LAAuthenticationRequirement](./laauthenticationrequirement/default.md)
  The requirement that requires user authentication.
- [class var biometry: LAAuthenticationRequirement](./laauthenticationrequirement/biometry.md)
  The requirement that requires biometric authentication.
- [class var biometryCurrentSet: LAAuthenticationRequirement](./laauthenticationrequirement/biometrycurrentset.md)
  The requirement that requires user authentication with the current set of biometrics.
- [class func biometry(fallback: LABiometryFallbackRequirement) -> Self](./laauthenticationrequirement/biometry%28fallback%29.md)
  Creates a requirement that requires biometric authentication or a fallback requirement that you specify.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Requirements
- [class LABiometryFallbackRequirement](./labiometryfallbackrequirement.md)
  A set of requirements to fall back on if biometrics aren’t present.


---

*[View on Apple Developer](https://developer.apple.com/documentation/localauthentication/laauthenticationrequirement)*