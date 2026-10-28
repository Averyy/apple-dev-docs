# biometry

**Framework**: Local Authentication  
**Kind**: property  
**Role**: Type Property

The requirement that requires biometric authentication.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class var biometry: LAAuthenticationRequirement { get }
```

```objc
@property (class, readonly) LAAuthenticationRequirement * biometryRequirement;
```

## Discussion

Authorizations with this requirement fail when biometrics aren’t available on the current device or there aren’t any enrolled biometrics on the current device.

## See Also

### Specifying authentication requirements
- [class var `default`: LAAuthenticationRequirement](./default.md)
  The requirement that requires user authentication.
- [class var biometryCurrentSet: LAAuthenticationRequirement](./biometrycurrentset.md)
  The requirement that requires user authentication with the current set of biometrics.
- [class func biometry(fallback: LABiometryFallbackRequirement) -> Self](./biometry%28fallback%29.md)
  Creates a requirement that requires biometric authentication or a fallback requirement that you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/localauthentication/laauthenticationrequirement/biometry)*