# requiresSIP

**Framework**: Automatic Assessment Configuration  
**Kind**: property

A Boolean value that indicates whether System Integrity Protection (SIP) must be enabled to start an assessment.

**Availability**:
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)

## Declaration

```swift
var requiresSIP: Bool { get set }
```

#### Discussion

When set to `true`, the assessment session will only start if System Integrity Protection is enabled on the device. This requirement is disabled by default.


---

*[View on Apple Developer](https://developer.apple.com/documentation/automaticassessmentconfiguration/aeassessmentconfiguration/requiressip)*