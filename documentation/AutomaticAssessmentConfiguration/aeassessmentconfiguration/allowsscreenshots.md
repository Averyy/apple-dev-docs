# allowsScreenshots

**Framework**: Automatic Assessment Configuration  
**Kind**: property

A Boolean value that indicates whether to allow screenshots copied to the clipboard during an assessment.

**Availability**:
- Mac Catalyst 26.1+
- macOS 26.1+

## Declaration

```swift
var allowsScreenshots: Bool { get set }
```

#### Discussion

An assessment session disables the ability to take screenshots by default to maintain assessment integrity. This property specifically applies to screenshots that are copied to the clipboard, typically those taken using the Command+Control+Shift+3 and Command+Control+Shift+4 keyboard shortcuts. You can allow clipboard screenshots by setting `allowsScreenshots` to `true`.

> **Note**: The clipboard is cleared before the assessment session ends to prevent exporting captured content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/automaticassessmentconfiguration/aeassessmentconfiguration/allowsscreenshots)*