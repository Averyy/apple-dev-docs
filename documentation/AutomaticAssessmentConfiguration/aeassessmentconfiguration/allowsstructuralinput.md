# allowsStructuralInput

**Framework**: Automatic Assessment Configuration  
**Kind**: property

A Boolean value that indicates whether to allow Chinese and Japanese structural input during an assessment.

**Availability**:
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)

## Declaration

```swift
var allowsStructuralInput: Bool { get set }
```

#### Discussion

Chinese and Japanese structural input methods allow users to enter characters using component-based input. An assessment session disables structural input by default, but you can allow it by setting [`allowsStructuralInput`](aeassessmentconfiguration/allowsstructuralinput.md) to `true` in the [`AEAssessmentConfiguration`](aeassessmentconfiguration.md) instance that you use to initialize a session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/automaticassessmentconfiguration/aeassessmentconfiguration/allowsstructuralinput)*