# mainParticipantConfiguration

**Framework**: Automatic Assessment Configuration  
**Kind**: property

The app-specific configuration for the app that invokes the assessment.

**Availability**:
- iOS 17.5+
- iPadOS 17.5+
- Mac Catalyst 15.0+
- macOS 12.0+

## Declaration

```swift
var mainParticipantConfiguration: AEAssessmentParticipantConfiguration { get }
```

#### Discussion

Use this property to get and customize the app-specific configuration that’s applied to your own app. For example, you can set the [`allowsNetworkAccess`](aeassessmentparticipantconfiguration/allowsnetworkaccess.md) property for your own app:

## See Also

- [func setConfiguration(AEAssessmentParticipantConfiguration, for: AEAssessmentApplication)](aeassessmentconfiguration/setconfiguration(_:for:).md)
  Adds an app to the list of apps available during an assessment.
- [var configurationsByApplication: [AEAssessmentApplication : AEAssessmentParticipantConfiguration]](aeassessmentconfiguration/configurationsbyapplication.md)
  The collection of apps available during an assessment, along with their associated configurations.
- [func remove(AEAssessmentApplication)](aeassessmentconfiguration/remove(_:).md)
  Removes the availability of a previously allowed app.
- [class AEAssessmentApplication](aeassessmentapplication.md)
  A representation of an app that users can access during an assessment.
- [class AEAssessmentParticipantConfiguration](aeassessmentparticipantconfiguration.md)
  Configuration information for an app that’s available during an assessment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/automaticassessmentconfiguration/aeassessmentconfiguration/mainparticipantconfiguration)*