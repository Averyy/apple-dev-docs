# isRequired

**Framework**: Automatic Assessment Configuration  
**Kind**: property

Whether the assessment requires this executable. Defaults to `NO`.

**Availability**:
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)

## Declaration

```swift
var isRequired: Bool { get set }
```

#### Discussion

Governs what happens when the executable cannot be enforced — for example, when signature validation fails under [`allowsOnlyParticipantsToRun`](aeassessmentconfiguration/allowsonlyparticipantstorun.md). A non-required participant is silently dropped; a required one prevents the session from beginning.

> **Note**: [`requiresSignatureValidation`](aeassessmentbinaryexecutable/requiressignaturevalidation.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/automaticassessmentconfiguration/aeassessmentbinaryexecutableconfiguration/isrequired)*