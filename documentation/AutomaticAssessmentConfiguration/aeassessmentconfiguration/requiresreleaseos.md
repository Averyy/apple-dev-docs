# requiresReleaseOS

**Framework**: Automatic Assessment Configuration  
**Kind**: property

A Boolean value that indicates whether the device must be running a final customer release of the operating system to start an assessment.

**Availability**:
- Mac Catalyst 27.0+
- macOS 27.0+

## Declaration

```swift
var requiresReleaseOS: Bool { get set }
```

#### Discussion

When set to `true`, the assessment session will only start if the device is running a released build of the operating system, rather than a beta, seed, or other prerelease build. Defaults to `false`.

> **Note**: [`AEAssessmentConfiguration`](aeassessmentconfiguration.md) for the limits that apply to every enablement requirement.


---

*[View on Apple Developer](https://developer.apple.com/documentation/automaticassessmentconfiguration/aeassessmentconfiguration/requiresreleaseos)*