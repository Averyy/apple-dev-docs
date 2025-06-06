# default

**Framework**: Local Authentication  
**Kind**: property

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

## See Also

- [class var biometry: LAAuthenticationRequirement](laauthenticationrequirement/biometry.md)
  The requirement that requires biometric authentication.
- [class var biometryCurrentSet: LAAuthenticationRequirement](laauthenticationrequirement/biometrycurrentset.md)
  The requirement that requires user authentication with the current set of biometrics.
- [class func biometry(fallback: LABiometryFallbackRequirement) -> Self](laauthenticationrequirement/biometry(fallback:).md)
  Creates a requirement that requires biometric authentication or a fallback requirement that you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/localauthentication/laauthenticationrequirement/default)*