# allowsLockdownMode

**Framework**: Automatic Assessment Configuration  
**Kind**: property

A Boolean value that indicates whether the assessment allows Lockdown Mode to be active.

**Availability**:
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)

## Declaration

```swift
var allowsLockdownMode: Bool { get set }
```

#### Discussion

When set to `false`, the assessment session will only start if Lockdown Mode is not enabled on the device. Defaults to `true`, which doesn’t enforce the requirement.


---

*[View on Apple Developer](https://developer.apple.com/documentation/automaticassessmentconfiguration/aeassessmentconfiguration/allowslockdownmode)*