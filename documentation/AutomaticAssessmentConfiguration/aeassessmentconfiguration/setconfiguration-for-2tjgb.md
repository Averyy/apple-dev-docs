# setConfiguration(_:for:)

**Framework**: Automatic Assessment Configuration  
**Kind**: method

Adds an app to the list of apps available during an assessment.

**Availability**:
- iOS 17.5+
- iPadOS 17.5+
- Mac Catalyst 15.0+
- macOS 12.0+

## Declaration

```swift
func setConfiguration(_ configuration: AEAssessmentParticipantConfiguration, for application: AEAssessmentApplication)
```

#### Discussion

Use this method to make an app besides your own available during an assessment. Create a representation of the app that you want to allow as an [`AEAssessmentApplication`](aeassessmentapplication.md) instance, and the configuration for that app using an [`AEAssessmentParticipantConfiguration`](aeassessmentparticipantconfiguration.md) instance:

```swift
let calculator = AEAssessmentApplication(bundleIdentifier: "com.apple.calculator")
let calculatorConfig = AEAssessmentParticipantConfiguration()
calculatorConfig.allowsNetworkAccess = false // Calculator doesn't need the network.
```

Use the app and its configuration to create an assessment configuration, and either create an assessment session with that, or update an existing session as shown below:

```swift
let configuration = AEAssessmentConfiguration()
configuration.setConfiguration(calculatorConfig, for: calculator)
session.update(to: configuration)
```

You can get a list of the currently allowed apps by accessing the [`configurationsByApplication`](aeassessmentconfiguration/configurationsbyapplication.md) property. You can disallow a previously allowed app by using the `AEAssessmentConfiguration/remove(_:)` method.

## Parameters

- `configuration`: The configuration of the secondary app.
- `application`: The app that you want to configure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/automaticassessmentconfiguration/aeassessmentconfiguration/setconfiguration(_:for:)-2tjgb)*