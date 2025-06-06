# biometryType

**Framework**: Local Authentication  
**Kind**: property

The type of biometric authentication supported by the device.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13.2+
- visionOS 1.0+
- watchOS 11.0+

## Declaration

```swift
var biometryType: LABiometryType { get }
```

#### Discussion

Use the value of this property to ensure that any authentication-related user prompts you create match the biometric capabilities of the device. For example, if the value of this property is [`LABiometryType.faceID`](labiometrytype/faceid.md), don’t refer to Touch ID in an authentication prompt.

This property is set only after you call the [`canEvaluatePolicy(_:error:)`](lacontext/canevaluatepolicy(_:error:).md) method, and is set no matter what the call returns. The default value is [`LABiometryType.none`](labiometrytype/none.md).

## See Also

- [func canEvaluatePolicy(LAPolicy, error: NSErrorPointer) -> Bool](lacontext/canevaluatepolicy(_:error:).md)
  Assesses whether authentication can proceed for a given policy.
- [enum LAPolicy](lapolicy.md)
  The set of available local authentication policies.
- [enum LABiometryType](labiometrytype.md)
  The set of available biometric authentication types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/localauthentication/lacontext/biometrytype)*