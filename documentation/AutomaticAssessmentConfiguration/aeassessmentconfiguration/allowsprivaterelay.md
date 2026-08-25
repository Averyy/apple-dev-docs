# allowsPrivateRelay

**Framework**: Automatic Assessment Configuration  
**Kind**: property

A Boolean value that indicates whether the assessment allows iCloud Private Relay to be active.

**Availability**:
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)

## Declaration

```swift
var allowsPrivateRelay: Bool { get set }
```

#### Discussion

When set to `false`, the assessment session will only start if iCloud Private Relay is not enabled, and won’t start if that status can’t be determined. Defaults to `true`, which doesn’t enforce the requirement.


---

*[View on Apple Developer](https://developer.apple.com/documentation/automaticassessmentconfiguration/aeassessmentconfiguration/allowsprivaterelay)*