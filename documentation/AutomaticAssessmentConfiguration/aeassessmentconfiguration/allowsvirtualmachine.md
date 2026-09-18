# allowsVirtualMachine

**Framework**: Automatic Assessment Configuration  
**Kind**: property

A Boolean value that indicates whether the assessment allows running inside a virtual machine.

**Availability**:
- Mac Catalyst 27.0+
- macOS 27.0+

## Declaration

```swift
var allowsVirtualMachine: Bool { get set }
```

#### Discussion

When set to `false`, the assessment session will only start if the device is not a virtual machine, and won’t start if that status can’t be determined. Defaults to `true`, which doesn’t enforce the requirement.

> ❗ **Important**: Setting this to `false` may not block a session in every virtualized environment.

> **Note**: [`AEAssessmentConfiguration`](aeassessmentconfiguration.md) for the limits that apply to every enablement requirement.


---

*[View on Apple Developer](https://developer.apple.com/documentation/automaticassessmentconfiguration/aeassessmentconfiguration/allowsvirtualmachine)*