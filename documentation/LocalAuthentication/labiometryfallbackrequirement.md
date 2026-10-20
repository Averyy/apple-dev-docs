# LABiometryFallbackRequirement

**Framework**: Local Authentication  
**Kind**: class  
**Role**: Class

A set of requirements to fall back on if biometrics aren’t present.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class LABiometryFallbackRequirement
```

```objc
@interface LABiometryFallbackRequirement : NSObject
```

## Topics

### Specifying biometric fallback requirements
- [class var `default`: LABiometryFallbackRequirement](./labiometryfallbackrequirement/default.md)
  The default biometric fallback requirement.
- [class var devicePasscode: LABiometryFallbackRequirement](./labiometryfallbackrequirement/devicepasscode.md)
  The fallback requirement that requires entering the device passcode.

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
- [class LAAuthenticationRequirement](./laauthenticationrequirement.md)
  A set of requirements that protect a right.


---

*[View on Apple Developer](https://developer.apple.com/documentation/localauthentication/labiometryfallbackrequirement)*