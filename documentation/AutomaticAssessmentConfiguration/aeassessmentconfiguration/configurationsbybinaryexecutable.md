# configurationsByBinaryExecutable

**Framework**: Automatic Assessment Configuration  
**Kind**: property

The collection of executable participants available during an assessment, along with their associated configurations.

**Availability**:
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)

## Declaration

```swift
var configurationsByBinaryExecutable: [AEAssessmentBinaryExecutable : AEAssessmentBinaryExecutableConfiguration] { get }
```

#### Discussion

Add executables with [`setConfiguration(_:for:)`](aeassessmentconfiguration/setconfiguration(_:for:)-16sed.md) and remove them with `AEAssessmentConfiguration/removeBinaryExecutable(_:)`.

> **Note**: [`AEAssessmentBinaryExecutable`](aeassessmentbinaryexecutable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/automaticassessmentconfiguration/aeassessmentconfiguration/configurationsbybinaryexecutable)*