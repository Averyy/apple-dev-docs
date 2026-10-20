# devicePasscode

**Framework**: Local Authentication  
**Kind**: property  
**Role**: Type Property

The fallback requirement that requires entering the device passcode.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class var devicePasscode: LABiometryFallbackRequirement { get }
```

```objc
@property (class, readonly) LABiometryFallbackRequirement * devicePasscodeRequirement;
```

## See Also

### Specifying biometric fallback requirements
- [class var `default`: LABiometryFallbackRequirement](./default.md)
  The default biometric fallback requirement.


---

*[View on Apple Developer](https://developer.apple.com/documentation/localauthentication/labiometryfallbackrequirement/devicepasscode)*