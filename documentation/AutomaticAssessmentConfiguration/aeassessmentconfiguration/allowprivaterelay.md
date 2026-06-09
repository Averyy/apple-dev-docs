# allowPrivateRelay

**Framework**: Automatic Assessment Configuration  
**Kind**: property

A Boolean value that indicates whether the assessment allows iCloud Private Relay to be active.

**Availability**:
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)

## Declaration

```swift
var allowPrivateRelay: Bool { get set }
```

#### Discussion

When set to `false`, the assessment session will only start if iCloud Private Relay is not enabled. This requirement is not enforced by default.


---

*[View on Apple Developer](https://developer.apple.com/documentation/automaticassessmentconfiguration/aeassessmentconfiguration/allowprivaterelay)*