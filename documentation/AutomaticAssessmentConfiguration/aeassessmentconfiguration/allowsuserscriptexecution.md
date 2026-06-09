# allowsUserScriptExecution

**Framework**: Automatic Assessment Configuration  
**Kind**: property

A Boolean value that indicates whether to allow user script execution during an assessment.

**Availability**:
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)

## Declaration

```swift
var allowsUserScriptExecution: Bool { get set }
```

#### Discussion

User scripts, such as AppleScripts or Automator workflows, can automate tasks on the system. An assessment session disables user script execution by default, but you can allow it by setting [`allowsUserScriptExecution`](aeassessmentconfiguration/allowsuserscriptexecution.md) to `true` in the [`AEAssessmentConfiguration`](aeassessmentconfiguration.md) instance that you use to initialize a session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/automaticassessmentconfiguration/aeassessmentconfiguration/allowsuserscriptexecution)*