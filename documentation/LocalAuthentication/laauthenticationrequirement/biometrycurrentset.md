# biometryCurrentSet

**Framework**: Local Authentication  
**Kind**: property  
**Role**: Type Property

The requirement that requires user authentication with the current set of biometrics.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class var biometryCurrentSet: LAAuthenticationRequirement { get }
```

```objc
@property (class, readonly) LAAuthenticationRequirement * biometryCurrentSetRequirement;
```

#### Discussion

Authorizations with this requirement fail when:

- Biometrics aren’t available on the current device.
- There aren’t any enrolled biometrics on the current device.
- There’s a change in enrolled biometrics on the current device. For example, adding a new finger to Touch ID changes the set of enrolled biometrics.

## See Also

### Specifying authentication requirements
- [class var `default`: LAAuthenticationRequirement](./default.md)
  The requirement that requires user authentication.
- [class var biometry: LAAuthenticationRequirement](./biometry.md)
  The requirement that requires biometric authentication.
- [class func biometry(fallback: LABiometryFallbackRequirement) -> Self](./biometry%28fallback%29.md)
  Creates a requirement that requires biometric authentication or a fallback requirement that you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/localauthentication/laauthenticationrequirement/biometrycurrentset)*