# allowsDock

**Framework**: Automatic Assessment Configuration  
**Kind**: property

A Boolean value that indicates whether to allow the Dock during an assessment.

**Availability**:
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)

## Declaration

```swift
var allowsDock: Bool { get set }
```

#### Discussion

An assessment session hides the Dock by default, but you can allow it by setting [`allowsDock`](aeassessmentconfiguration/allowsdock.md) to `true` in the [`AEAssessmentConfiguration`](aeassessmentconfiguration.md) instance that you use to initialize a session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/automaticassessmentconfiguration/aeassessmentconfiguration/allowsdock)*