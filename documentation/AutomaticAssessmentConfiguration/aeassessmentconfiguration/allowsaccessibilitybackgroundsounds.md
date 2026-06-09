# allowsAccessibilityBackgroundSounds

**Framework**: Automatic Assessment Configuration  
**Kind**: property

A Boolean value that indicates whether to allow Background Sounds during an assessment.

**Availability**:
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)

## Declaration

```swift
var allowsAccessibilityBackgroundSounds: Bool { get set }
```

#### Discussion

Users can enable Background Sounds in the Settings app (Accessibility > Audio & Visual > Background Sounds) to play ambient sounds that can mask unwanted environmental noise. An assessment session disables Background Sounds by default, but you can allow it by setting [`allowsAccessibilityBackgroundSounds`](aeassessmentconfiguration/allowsaccessibilitybackgroundsounds.md) to `true` in the [`AEAssessmentConfiguration`](aeassessmentconfiguration.md) instance that you use to initialize a session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/automaticassessmentconfiguration/aeassessmentconfiguration/allowsaccessibilitybackgroundsounds)*