# allowsAccessibilityReader

**Framework**: Automatic Assessment Configuration  
**Kind**: property

A Boolean value that indicates whether to allow the Accessibility Reader during an assessment.

**Availability**:
- iOS 26.1+
- iPadOS 26.1+
- Mac Catalyst 26.1+
- macOS 26.1+

## Declaration

```swift
var allowsAccessibilityReader: Bool { get set }
```

#### Discussion

Users can enable the Accessibility Reader in the Settings app (Accessibility > Read & Speak > Accessibility Reader) to have text content formatted or read aloud. An assessment session disables the Accessibility Reader by default, but you can allow it by setting [`allowsAccessibilityReader`](aeassessmentconfiguration/allowsaccessibilityreader.md) to `true` in the [`AEAssessmentConfiguration`](aeassessmentconfiguration.md) instance that you use to initialize a session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/automaticassessmentconfiguration/aeassessmentconfiguration/allowsaccessibilityreader)*