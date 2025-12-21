# AEAssessmentConfiguration

**Framework**: Automatic Assessment Configuration  
**Kind**: class

Configuration information for an assessment session.

**Availability**:
- iOS 13.4+
- iPadOS 13.4+
- Mac Catalyst 14.0+
- macOS 10.15.4+

## Declaration

```swift
class AEAssessmentConfiguration
```

#### Overview

Create a configuration instance and pass it to the [`init(configuration:)`](aeassessmentsession/init(configuration:).md) initializer of an [`AEAssessmentSession`](aeassessmentsession.md) instance to create a new assessment session. Before using the configuration, indicate which exceptions you want to allow for the assessment session’s restrictions by setting values on the configuration instance. For example, you can set values to allow dictation and certain aspects of autocorrect:

While you provide a configuration instance when creating a session on iOS, iPadOS, and macOS, specific exceptions apply only to certain platforms. In particular, on macOS, you can selectively make specific apps besides your own available during an assessment — for example, to allow users to access a calculator or a dictionary. All other exceptions apply only to iOS and iPadOS.

## Topics

### Allowing access to other apps
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
- [class AEAssessmentParticipantConfiguration](aeassessmentparticipantconfiguration.md)
  Configuration information for an app that’s available during an assessment.
### Allowing accessibility
- [var allowsAccessibilitySpeech: Bool](aeassessmentconfiguration/allowsaccessibilityspeech.md)
  A Boolean value that indicates whether to allow the speech-related accessibility features during an assessment.
- [var allowsDictation: Bool](aeassessmentconfiguration/allowsdictation.md)
  A Boolean value that indicates whether to allow the use of dictation during an assessment.
### Allowing typing assistance
- [var allowsContinuousPathKeyboard: Bool](aeassessmentconfiguration/allowscontinuouspathkeyboard.md)
  A Boolean value that indicates whether to allow Slide to Type to operate during an assessment.
- [var allowsKeyboardShortcuts: Bool](aeassessmentconfiguration/allowskeyboardshortcuts.md)
  A Boolean value that indicates whether to allow keyboard shortcuts during an assessment.
- [var allowsPredictiveKeyboard: Bool](aeassessmentconfiguration/allowspredictivekeyboard.md)
  A Boolean value that indicates whether to enable the predictive keyboard during an assessment.
- [var allowsPasswordAutoFill: Bool](aeassessmentconfiguration/allowspasswordautofill.md)
  A Boolean value that indicates whether to allow password autofill during an assessment.
### Allowing corrections
- [var allowsSpellCheck: Bool](aeassessmentconfiguration/allowsspellcheck.md)
  A Boolean value that indicates whether to allow spell check during an assessment.
- [var autocorrectMode: AEAssessmentConfiguration.AutocorrectMode](aeassessmentconfiguration/autocorrectmode-swift.property.md)
  A Boolean value that indicates whether to allow Autocorrect during an assessment.
- [AEAssessmentConfiguration.AutocorrectMode](aeassessmentconfiguration/autocorrectmode-swift.struct.md)
  The set of autocorrect features that you can enable during an assessment.
### Allowing handoff
- [var allowsActivityContinuation: Bool](aeassessmentconfiguration/allowsactivitycontinuation.md)
  A Boolean value that indicates whether to allow Handoff during an assessment.
### Instance Properties
- [var allowsAccessibilityKeyboard: Bool](aeassessmentconfiguration/allowsaccessibilitykeyboard.md)
  A Boolean value that indicates whether to allow alternative input methods in the Accessibility Keyboard during an assessment.
- [var allowsAccessibilityLiveCaptions: Bool](aeassessmentconfiguration/allowsaccessibilitylivecaptions.md)
  A Boolean value that indicates whether to allow Live Captions during an assessment.
- [var allowsAccessibilityReader: Bool](aeassessmentconfiguration/allowsaccessibilityreader.md)
  A Boolean value that indicates whether to allow the Accessibility Reader during an assessment.
- [var allowsAccessibilityTypingFeedback: Bool](aeassessmentconfiguration/allowsaccessibilitytypingfeedback.md)
  A Boolean value that indicates whether to allow accessibility typing feedback during an assessment.
- [var allowsScreenshots: Bool](aeassessmentconfiguration/allowsscreenshots.md)
  A Boolean value that indicates whether to allow screenshots copied to the clipboard during an assessment.

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

- [Preparing an educational assessment app for distribution](preparing-an-educational-assessment-app-for-distribution.md)
  Ensure your app maintains academic integrity by reviewing assessment practices and managing system capabilities.
- [Build an Educational Assessment App](build-an-educational-assessment-app.md)
  Ensure the academic integrity of your assessment app by using Automatic Assessment Configuration.
- [class AEAssessmentSession](aeassessmentsession.md)
  A session that your app uses to protect an assessment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/automaticassessmentconfiguration/aeassessmentconfiguration)*