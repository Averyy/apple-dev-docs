# AEAssessmentApplication

**Framework**: Automatic Assessment Configuration  
**Kind**: class

A representation of an app that users can access during an assessment.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+

## Declaration

```swift
class AEAssessmentApplication
```

#### Overview

Use an instance of this class when you want to make an app besides yours, like a calculator or a dictionary, available during an assessment. Create a representation of the app that you want to allow using the app’s bundle identifier and optionally the identifier of the team that distributes the app. You can get both identifiers for an app that you have installed using the `codesign` command line utility:

```shell
% codesign -v -d /Applications/MyApp.app
```

By default, the system requires that the app’s code signature is valid, and that either Apple distributes the app, or the developer notarizes the app or distributes it through the App Store. You can relax these requirements by setting the [`requiresSignatureValidation`](aeassessmentapplication/requiressignaturevalidation.md) property to `false`, but that creates a potential security risk. In that case, the only requirement is that the app has the specified bundle and team identifiers. Prefer to keep the signature requirement.

Add the app to a session configuration by calling the [`setConfiguration(_:for:)`](aeassessmentconfiguration/setconfiguration(_:for:).md) method, and then apply the configuration to either a new session that you create, or an existing session with the [`update(to:)`](aeassessmentsession/update(to:).md) method.

## Topics

### Creating an assessment application
- [init(bundleIdentifier: String, teamIdentifier: String?)](aeassessmentapplication/init(bundleidentifier:teamidentifier:).md)
  Creates a representation of an app using its bundle and team identifiers.
- [init(bundleIdentifier: String)](aeassessmentapplication/init(bundleidentifier:).md)
  Creates a representation of an app using its bundle identifier.
- [var bundleIdentifier: String](aeassessmentapplication/bundleidentifier.md)
  The bundle identifier of the app.
- [var teamIdentifier: String?](aeassessmentapplication/teamidentifier.md)
  The team identifier of the app.
### Requiring code-signed apps
- [var requiresSignatureValidation: Bool](aeassessmentapplication/requiressignaturevalidation.md)
  A Boolean that indicates whether the session requires the app to have a valid code signature to run.

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
- [class AEAssessmentParticipantConfiguration](aeassessmentparticipantconfiguration.md)
  Configuration information for an app that’s available during an assessment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/automaticassessmentconfiguration/aeassessmentapplication)*