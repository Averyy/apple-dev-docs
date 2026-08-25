# requiresSignatureValidation

**Framework**: Automatic Assessment Configuration  
**Kind**: property

Whether the running executable’s code signature is validated. Defaults to `YES`.

**Availability**:
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)

## Declaration

```swift
var requiresSignatureValidation: Bool { get set }
```

#### Discussion

Disabling this waives only the availability check, not the signing requirement of [`allowsOnlyParticipantsToRun`](aeassessmentconfiguration/allowsonlyparticipantstorun.md): an unsigned or invalidly signed executable still can’t be added to that session’s launch allowlist. Disabling it converts a required participant’s begin-time failure into a silent launch denial, and forgoes the swap/re-sign protection for a signed one.

> **Note**: [`isRequired`](aeassessmentbinaryexecutableconfiguration/isrequired.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/automaticassessmentconfiguration/aeassessmentbinaryexecutable/requiressignaturevalidation)*