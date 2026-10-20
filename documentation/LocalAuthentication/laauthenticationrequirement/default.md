# default

**Framework**: Local Authentication  
**Kind**: property  
**Role**: Type Property

The requirement that requires user authentication.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class var `default`: LAAuthenticationRequirement { get }
```

```objc
@property (class, readonly) LAAuthenticationRequirement * defaultRequirement;
```

## See Also

### Specifying authentication requirements
- [class var biometry: LAAuthenticationRequirement](./biometry.md)
  The requirement that requires biometric authentication.
- [class var biometryCurrentSet: LAAuthenticationRequirement](./biometrycurrentset.md)
  The requirement that requires user authentication with the current set of biometrics.
- [class func biometry(fallback: LABiometryFallbackRequirement) -> Self](./biometry%28fallback%29.md)
  Creates a requirement that requires biometric authentication or a fallback requirement that you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/localauthentication/laauthenticationrequirement/default)*