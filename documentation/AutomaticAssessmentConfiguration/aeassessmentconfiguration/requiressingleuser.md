# requiresSingleUser

**Framework**: Automatic Assessment Configuration  
**Kind**: property

A Boolean value that indicates whether only a single user account must be logged in to start an assessment.

**Availability**:
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)

## Declaration

```swift
var requiresSingleUser: Bool { get set }
```

#### Discussion

When set to `true`, the assessment session will only start if there is exactly one user account logged in on the device. This requirement is disabled by default.


---

*[View on Apple Developer](https://developer.apple.com/documentation/automaticassessmentconfiguration/aeassessmentconfiguration/requiressingleuser)*