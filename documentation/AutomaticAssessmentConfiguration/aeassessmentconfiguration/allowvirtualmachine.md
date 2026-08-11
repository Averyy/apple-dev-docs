# allowVirtualMachine

**Framework**: Automatic Assessment Configuration  
**Kind**: property

A Boolean value that indicates whether the assessment allows running inside a virtual machine.

**Availability**:
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)

## Declaration

```swift
var allowVirtualMachine: Bool { get set }
```

#### Discussion

When set to `false`, the assessment session will only start if the device is not a virtual machine. This requirement is not enforced by default; virtual machines are allowed unless you opt out.

> ❗ **Important**: This check is advisory, not a security guarantee. Setting `allowVirtualMachine` to `false` may not block an assessment session in every virtualized environment. Use this property to steer proctored exams toward physical hardware; it doesn’t provide a cryptographic attestation that the session is running on a physical machine.

For stronger assurances about the runtime environment, pair this property with [`App Attest`](https://developer.apple.comhttps://developer.apple.com/documentation/DeviceCheck) on macOS.


---

*[View on Apple Developer](https://developer.apple.com/documentation/automaticassessmentconfiguration/aeassessmentconfiguration/allowvirtualmachine)*