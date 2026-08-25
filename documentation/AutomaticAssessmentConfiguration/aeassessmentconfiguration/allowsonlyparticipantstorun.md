# allowsOnlyParticipantsToRun

**Framework**: Automatic Assessment Configuration  
**Kind**: property

A Boolean value that indicates whether only participant applications are allowed to run during an assessment.

**Availability**:
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)

## Declaration

```swift
var allowsOnlyParticipantsToRun: Bool { get set }
```

#### Discussion

Only validly signed participants can be permitted. The launch allowlist pins each entry to the code signing identifier and team identifier read from its signature, so an unsigned or invalidly signed participant has no identity to pin and is denied launch even though you configured it as a participant. This holds regardless of [`requiresSignatureValidation`](aeassessmentbinaryexecutable/requiressignaturevalidation.md).

> **Note**: [`AEAssessmentBinaryExecutable`](aeassessmentbinaryexecutable.md) for how an unenforceable executable participant affects the session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/automaticassessmentconfiguration/aeassessmentconfiguration/allowsonlyparticipantstorun)*