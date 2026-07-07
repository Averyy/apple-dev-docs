# allowsActivityContinuation

**Framework**: Automatic Assessment Configuration  
**Kind**: property

A Boolean value that indicates whether to allow Handoff during an assessment.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+

## Declaration

```swift
var allowsActivityContinuation: Bool { get set }
```

#### Discussion

Handoff lets users start an activity on one device and seamlessly resume the activity on another. Users control whether a device participates in Handoff by turning the feature on or off in the Settings app (General > AirPlay & Handoff > Handoff). An assessment disables this feature by default, but you can allow users undergoing an assessment to continue to use Handoff by setting [`allowsActivityContinuation`](aeassessmentconfiguration/allowsactivitycontinuation.md) to `true`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/automaticassessmentconfiguration/aeassessmentconfiguration/allowsactivitycontinuation)*