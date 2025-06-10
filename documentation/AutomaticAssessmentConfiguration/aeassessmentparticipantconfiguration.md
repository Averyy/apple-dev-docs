# AEAssessmentParticipantConfiguration

**Framework**: Automatic Assessment Configuration  
**Kind**: class

Configuration information for an app that’s available during an assessment.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+

## Declaration

```swift
class AEAssessmentParticipantConfiguration
```

#### Overview

Use an instance of this class to configure the properties of an app that you allow to run during an assessment. Associate the participant configuration with an app (an [`AEAssessmentApplication`](aeassessmentapplication.md) instance) when you call the [`setConfiguration(_:for:)`](aeassessmentconfiguration/setconfiguration(_:for:).md) method of a session configuration.

## Topics

### Creating participant configuration instances
- [init()](aeassessmentparticipantconfiguration/init.md)
  Initializes an assessment participant configuration instance.
- [class func new() -> Self](aeassessmentparticipantconfiguration/new.md)
  Creates a new assessment participant configuration instance.
### Allowing network access
- [var allowsNetworkAccess: Bool](aeassessmentparticipantconfiguration/allowsnetworkaccess.md)
  A Boolean that indicates whether an app can access network resources during an assessment.
### Instance Properties
- [var configurationInfo: [String : Any]](aeassessmentparticipantconfiguration/configurationinfo.md)
- [var isRequired: Bool](aeassessmentparticipantconfiguration/isrequired.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [func setConfiguration(AEAssessmentParticipantConfiguration, for: AEAssessmentApplication)](aeassessmentconfiguration/setconfiguration(_:for:).md)
  Adds an app to the list of apps available during an assessment.
- [var configurationsByApplication: [AEAssessmentApplication : AEAssessmentParticipantConfiguration]](aeassessmentconfiguration/configurationsbyapplication.md)
  The collection of apps available during an assessment, along with their associated configurations.
- [func remove(AEAssessmentApplication)](aeassessmentconfiguration/remove(_:).md)
  Removes the availability of a previously allowed app.
- [var mainParticipantConfiguration: AEAssessmentParticipantConfiguration](aeassessmentconfiguration/mainparticipantconfiguration.md)
  The app-specific configuration for the app that invokes the assessment.
- [class AEAssessmentApplication](aeassessmentapplication.md)
  A representation of an app that users can access during an assessment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/automaticassessmentconfiguration/aeassessmentparticipantconfiguration)*