# requiresManagedDevice

**Framework**: Automatic Assessment Configuration  
**Kind**: property

A Boolean value that indicates whether the device must be managed to start an assessment.

**Availability**:
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)

## Declaration

```swift
var requiresManagedDevice: Bool { get set }
```

#### Discussion

When set to `true`, the assessment session will only start if the device is enrolled in a Mobile Device Management (MDM) solution. This requirement is disabled by default.


---

*[View on Apple Developer](https://developer.apple.com/documentation/automaticassessmentconfiguration/aeassessmentconfiguration/requiresmanageddevice)*