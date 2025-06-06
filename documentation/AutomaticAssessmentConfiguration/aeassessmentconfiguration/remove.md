# remove(_:)

**Framework**: Automatic Assessment Configuration  
**Kind**: method

Removes the availability of a previously allowed app.

**Availability**:
- iOS 17.5+
- iPadOS 17.5+
- Mac Catalyst 15.0+
- macOS 12.0+

## Declaration

```swift
func remove(_ application: AEAssessmentApplication)
```

#### Discussion

Use this method to remove apps that you previously added to the list of apps that are available during an assessment with the [`setConfiguration(_:for:)`](aeassessmentconfiguration/setconfiguration(_:for:).md) method. You can get the list of currently allowed apps by accessing the configuration’s [`configurationsByApplication`](aeassessmentconfiguration/configurationsbyapplication.md) property.

## Parameters

- `application`: The app that you want to remove from the list of allowed secondary apps.

## See Also

- [func setConfiguration(AEAssessmentParticipantConfiguration, for: AEAssessmentApplication)](aeassessmentconfiguration/setconfiguration(_:for:).md)
  Adds an app to the list of apps available during an assessment.
- [var configurationsByApplication: [AEAssessmentApplication : AEAssessmentParticipantConfiguration]](aeassessmentconfiguration/configurationsbyapplication.md)
  The collection of apps available during an assessment, along with their associated configurations.
- [var mainParticipantConfiguration: AEAssessmentParticipantConfiguration](aeassessmentconfiguration/mainparticipantconfiguration.md)
  The app-specific configuration for the app that invokes the assessment.
- [class AEAssessmentApplication](aeassessmentapplication.md)
  A representation of an app that users can access during an assessment.
- [class AEAssessmentParticipantConfiguration](aeassessmentparticipantconfiguration.md)
  Configuration information for an app that’s available during an assessment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/automaticassessmentconfiguration/aeassessmentconfiguration/remove(_:))*