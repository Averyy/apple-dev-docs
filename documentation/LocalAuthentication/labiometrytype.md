# LABiometryType

**Framework**: Local Authentication  
**Kind**: enum  
**Role**: Enumeration

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

```c
enum LABiometryType : NSInteger;
```

## Topics

### Types
- [LABiometryType.none](./labiometrytype/none.md)
  No biometry type is supported.
- [LABiometryType.faceID](./labiometrytype/faceid.md)
  The device supports Face ID.
- [LABiometryType.touchID](./labiometrytype/touchid.md)
  The device supports Touch ID.
- [LABiometryType.opticID](./labiometrytype/opticid.md)
  The device supports Optic ID.
### Legacy Types
- [static var LABiometryNone: LABiometryType](./labiometrytype/labiometrynone.md)
  No biometry type is supported.
### Initializers
- [init?(rawValue: Int)](./labiometrytype/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Checking availability
- [func canEvaluatePolicy(LAPolicy, error: NSErrorPointer) -> Bool](./lacontext/canevaluatepolicy%28_,error%29.md)
  Assesses whether authentication can proceed for a given policy.
- [enum LAPolicy](./lapolicy.md)
  The set of available local authentication policies.
- [var biometryType: LABiometryType](./lacontext/biometrytype.md)
  The type of biometric authentication supported by the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/localauthentication/labiometrytype)*