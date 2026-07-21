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

> ❗ **Important**: This check is advisory, not a security guarantee. The framework can’t reliably detect whether SIP is enabled on systems where the user has administrator privileges, so setting `requiresSIP` to `true` may not block an assessment session when SIP is in fact disabled. Use this property to prompt users to re-enable SIP if they turned it off for unrelated reasons; it doesn’t indicate whether the system was modified while SIP was previously disabled.

For stronger assurances that SIP is enabled, pair this property with [`App Attest`](https://developer.apple.comhttps://developer.apple.com/documentation/DeviceCheck) on macOS.


---

*[View on Apple Developer](https://developer.apple.com/documentation/automaticassessmentconfiguration/aeassessmentconfiguration/requiressip)*