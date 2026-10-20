# biometry(fallback:)

**Framework**: Local Authentication  
**Kind**: method  
**Role**: Type Method

Creates a requirement that requires biometric authentication or a fallback requirement that you specify.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class func biometry(fallback: LABiometryFallbackRequirement) -> Self
```

```objc
+ (instancetype) biometryRequirementWithFallback:(LABiometryFallbackRequirement *) fallback;
```

#### Return Value

Returns a requirement that requires biometric authentication or a fallback requirement that you specify.

## Parameters

- `fallback`: A requirement to use a fallback if biometric authentication fails or is unavailable, or if the user prefers not to use biometric authentication.

## See Also

### Specifying authentication requirements
- [class var `default`: LAAuthenticationRequirement](./default.md)
  The requirement that requires user authentication.
- [class var biometry: LAAuthenticationRequirement](./biometry.md)
  The requirement that requires biometric authentication.
- [class var biometryCurrentSet: LAAuthenticationRequirement](./biometrycurrentset.md)
  The requirement that requires user authentication with the current set of biometrics.


---

*[View on Apple Developer](https://developer.apple.com/documentation/localauthentication/laauthenticationrequirement/biometry(fallback:))*