# configurationsByApplication

**Framework**: Automatic Assessment Configuration  
**Kind**: property

The collection of apps available during an assessment, along with their associated configurations.

**Availability**:
- iOS 17.5+
- iPadOS 17.5+
- Mac Catalyst 15.0+
- macOS 12.0+

## Declaration

```swift
var configurationsByApplication: [AEAssessmentApplication : AEAssessmentParticipantConfiguration] { get }
```

#### Discussion

Access this property to get a list of the currently allowed secondary apps and their individual configurations. Add apps to the list by calling the [`setConfiguration(_:for:)`](aeassessmentconfiguration/setconfiguration(_:for:).md) method. Remove them from the list by calling the [`remove(_:)`](aeassessmentconfiguration/remove(_:).md) method.

## See Also

- [func setConfiguration(AEAssessmentParticipantConfiguration, for: AEAssessmentApplication)](aeassessmentconfiguration/setconfiguration(_:for:).md)
  Adds an app to the list of apps available during an assessment.
- [func remove(AEAssessmentApplication)](aeassessmentconfiguration/remove(_:).md)
  Removes the availability of a previously allowed app.
- [var mainParticipantConfiguration: AEAssessmentParticipantConfiguration](aeassessmentconfiguration/mainparticipantconfiguration.md)
  The app-specific configuration for the app that invokes the assessment.
- [class AEAssessmentApplication](aeassessmentapplication.md)
  A representation of an app that users can access during an assessment.
- [class AEAssessmentParticipantConfiguration](aeassessmentparticipantconfiguration.md)
  Configuration information for an app that’s available during an assessment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/automaticassessmentconfiguration/aeassessmentconfiguration/configurationsbyapplication)*