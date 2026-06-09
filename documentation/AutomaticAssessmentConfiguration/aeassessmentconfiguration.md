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

**Swift**:

```swift
let config = AEAssessmentConfiguration()

#if os(iOS) // These exceptions available only on iOS and iPadOS.
config.allowsDictation = true
config.autocorrectMode = [.punctuation, .spelling]
#endif

let session = AEAssessmentSession(configuration: config)
```

**Objective-C**:

```objc
AEAssessmentConfiguration *config = [AEAssessmentConfiguration new];

#if TARGET_OS_IPHONE || TARGET_IPHONE_SIMULATOR // These exceptions available only on iOS and iPadOS.
config.allowsDictation = YES;
config.autocorrectMode = AEAutocorrectModePunctuation | AEAutocorrectModeSpelling;
#endif

AEAssessmentSession *session = [[AEAssessmentSession alloc] initWithConfiguration:config];
```

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
- [var allowLockdownMode: Bool](aeassessmentconfiguration/allowlockdownmode.md)
  A Boolean value that indicates whether the assessment allows Lockdown Mode to be active.
- [var allowOnlyParticipantsToRun: Bool](aeassessmentconfiguration/allowonlyparticipantstorun.md)
  A Boolean value that indicates whether only participant applications are allowed to run during an assessment.
- [var allowPrivateRelay: Bool](aeassessmentconfiguration/allowprivaterelay.md)
  A Boolean value that indicates whether the assessment allows iCloud Private Relay to be active.
- [var allowedAppleMenuItems: Set<AEAppleMenuItem>?](aeassessmentconfiguration/allowedapplemenuitems.md)
  The set of allowed Apple menu items during an assessment.
- [var allowedDirectoriesAndFiles: Set<URL>?](aeassessmentconfiguration/alloweddirectoriesandfiles.md)
  The set of allowed directories and files that participants can access during an assessment.
- [var allowedMenuBarItems: Set<AEMenuBarItem>?](aeassessmentconfiguration/allowedmenubaritems.md)
  The set of menu bar items that should remain visible during an assessment.
- [var allowsAccessibilityAlternativeInputMethods: Bool](aeassessmentconfiguration/allowsaccessibilityalternativeinputmethods.md)
  A Boolean value that indicates whether to allow alternative input methods for accessibility features during an assessment.
- [var allowsAccessibilityBackgroundSounds: Bool](aeassessmentconfiguration/allowsaccessibilitybackgroundsounds.md)
  A Boolean value that indicates whether to allow Background Sounds during an assessment.
- [var allowsAccessibilityHoverText: Bool](aeassessmentconfiguration/allowsaccessibilityhovertext.md)
  A Boolean value that indicates whether to allow Hover Text during an assessment.
- [var allowsAccessibilityKeyboard: Bool](aeassessmentconfiguration/allowsaccessibilitykeyboard.md)
  A Boolean value that indicates whether to allow the Accessibility Keyboard during an assessment.
- [var allowsAccessibilityLiveCaptions: Bool](aeassessmentconfiguration/allowsaccessibilitylivecaptions.md)
  A Boolean value that indicates whether to allow Live Captions during an assessment.
- [var allowsAccessibilityLiveSpeech: Bool](aeassessmentconfiguration/allowsaccessibilitylivespeech.md)
  A Boolean value that indicates whether to allow Live Speech during an assessment.
- [var allowsAccessibilityReader: Bool](aeassessmentconfiguration/allowsaccessibilityreader.md)
  A Boolean value that indicates whether to allow the Accessibility Reader during an assessment.
- [var allowsAccessibilitySpokenContent: Bool](aeassessmentconfiguration/allowsaccessibilityspokencontent.md)
  A Boolean value that indicates whether to allow Spoken Content during an assessment.
- [var allowsAccessibilitySwitchControl: Bool](aeassessmentconfiguration/allowsaccessibilityswitchcontrol.md)
  A Boolean value that indicates whether to allow Switch Control during an assessment.
- [var allowsAccessibilityTypingFeedback: Bool](aeassessmentconfiguration/allowsaccessibilitytypingfeedback.md)
  A Boolean value that indicates whether to allow accessibility typing feedback during an assessment.
- [var allowsAccessibilityVoiceControl: Bool](aeassessmentconfiguration/allowsaccessibilityvoicecontrol.md)
  A Boolean value that indicates whether to allow Voice Control during an assessment.
- [var allowsAccessibilityVoiceOver: Bool](aeassessmentconfiguration/allowsaccessibilityvoiceover.md)
  A Boolean value that indicates whether to allow VoiceOver during an assessment.
- [var allowsAccessibilityZoom: Bool](aeassessmentconfiguration/allowsaccessibilityzoom.md)
  A Boolean value that indicates whether to allow Zoom during an assessment.
- [var allowsAutoFill: Bool](aeassessmentconfiguration/allowsautofill.md)
  A Boolean value that indicates whether to allow autofill during an assessment.
- [var allowsDock: Bool](aeassessmentconfiguration/allowsdock.md)
  A Boolean value that indicates whether to allow the Dock during an assessment.
- [var allowsEmojiKeyboard: Bool](aeassessmentconfiguration/allowsemojikeyboard.md)
  A Boolean value that indicates whether to allow the emoji keyboard during an assessment.
- [var allowsMenuBar: Bool](aeassessmentconfiguration/allowsmenubar.md)
  A Boolean value that indicates whether to allow the menu bar during an assessment.
- [var allowsScreenshots: Bool](aeassessmentconfiguration/allowsscreenshots.md)
  A Boolean value that indicates whether to allow screenshots copied to the clipboard during an assessment.
- [var allowsStructuralInput: Bool](aeassessmentconfiguration/allowsstructuralinput.md)
  A Boolean value that indicates whether to allow Chinese and Japanese structural input during an assessment.
- [var allowsUserScriptExecution: Bool](aeassessmentconfiguration/allowsuserscriptexecution.md)
  A Boolean value that indicates whether to allow user script execution during an assessment.
- [var requiresManagedDevice: Bool](aeassessmentconfiguration/requiresmanageddevice.md)
  A Boolean value that indicates whether the device must be managed to start an assessment.
- [var requiresSIP: Bool](aeassessmentconfiguration/requiressip.md)
  A Boolean value that indicates whether System Integrity Protection (SIP) must be enabled to start an assessment.
- [var requiresSingleUser: Bool](aeassessmentconfiguration/requiressingleuser.md)
  A Boolean value that indicates whether only a single user account must be logged in to start an assessment.
- [var requiresUserAccountType: AEUserAccountType](aeassessmentconfiguration/requiresuseraccounttype.md)
  Specifies the type of user account required to start an assessment.

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