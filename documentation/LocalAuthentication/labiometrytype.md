# LABiometryType

**Framework**: Local Authentication  
**Kind**: enum

The set of available biometric authentication types.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13.2+
- visionOS 1.0+
- watchOS 11.0+

## Declaration

```swift
enum LABiometryType
```

## Topics

### Types
- [LABiometryType.none](labiometrytype/none.md)
  No biometry type is supported.
- [LABiometryType.faceID](labiometrytype/faceid.md)
  The device supports Face ID.
- [LABiometryType.touchID](labiometrytype/touchid.md)
  The device supports Touch ID.
- [LABiometryType.opticID](labiometrytype/opticid.md)
  The device supports Optic ID.
### Legacy Types
- [static var LABiometryNone: LABiometryType](labiometrytype/labiometrynone.md)
  No biometry type is supported.
### Initializers
- [init?(rawValue: Int)](labiometrytype/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [func canEvaluatePolicy(LAPolicy, error: NSErrorPointer) -> Bool](lacontext/canevaluatepolicy(_:error:).md)
  Assesses whether authentication can proceed for a given policy.
- [enum LAPolicy](lapolicy.md)
  The set of available local authentication policies.
- [var biometryType: LABiometryType](lacontext/biometrytype.md)
  The type of biometric authentication supported by the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/localauthentication/labiometrytype)*