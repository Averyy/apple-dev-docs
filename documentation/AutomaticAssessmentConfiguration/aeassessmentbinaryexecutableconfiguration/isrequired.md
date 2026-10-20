# isRequired

**Framework**: Automatic Assessment Configuration  
**Kind**: property  
**Role**: Instance Property

Whether the assessment requires this executable. Defaults to `NO`.

**Availability**:
- Mac Catalyst 27.0+
- macOS 27.0+

## Declaration

```swift
var isRequired: Bool { get set }
```

```objc
@property (nonatomic, assign, getter=isRequired) BOOL required;
```

#### Discussion

Governs what happens when the executable cannot be enforced — for example, when signature validation fails under [`allowsOnlyParticipantsToRun`](../aeassessmentconfiguration/allowsonlyparticipantstorun.md). A non-required participant is silently dropped; a required one prevents the session from beginning.

> **See Also**: [`requiresSignatureValidation`](../aeassessmentbinaryexecutable/requiressignaturevalidation.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/automaticassessmentconfiguration/aeassessmentbinaryexecutableconfiguration/isrequired)*