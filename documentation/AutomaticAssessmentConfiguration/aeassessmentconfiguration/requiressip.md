# requiresSIP

**Framework**: Automatic Assessment Configuration  
**Kind**: property

A Boolean value that indicates whether System Integrity Protection (SIP) must be enabled to start an assessment.

**Availability**:
- Mac Catalyst 27.0+
- macOS 27.0+

## Declaration

```swift
var requiresSIP: Bool { get set }
```

#### Discussion

When set to `true`, the assessment session will only start if System Integrity Protection is enabled on the device. Defaults to `false`.

> ❗ **Important**: The framework can’t reliably detect whether SIP is enabled on systems where the user has administrator privileges, so setting `requiresSIP` to `true` may not block a session when SIP is in fact disabled. It also doesn’t indicate whether the system was modified while SIP was previously disabled.

> **Note**: [`AEAssessmentConfiguration`](aeassessmentconfiguration.md) for the limits that apply to every enablement requirement.


---

*[View on Apple Developer](https://developer.apple.com/documentation/automaticassessmentconfiguration/aeassessmentconfiguration/requiressip)*