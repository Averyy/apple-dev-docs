# SkipKeys

**Framework**: Device Management  
**Kind**: dictionary

The list of skip keys for setup panes.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- macOS 10.9+
- tvOS 10.2+
- visionOS 26.0+

## Declaration

```swift
object SkipKeys
```

## Mentions

- [Returning a managed device to service](returning-a-managed-device-to-service.md)

## Properties

- `Accessibility` (string): The key to skip the Accessibility pane, when creating additional users. > **Note**:  This key doesn’t skip the Accessibility pane in Setup Assistant during initial device set up. It does skip the Accessibility pane when Setup Assistant runs due to a new user log in. Available in macOS 11 and later.
- `ActionButton` (string): The key to skip the Action Button configuration pane. Available in iOS 17 and later.
- `Android` (string): If the Restore pane isn’t skipped, this is the key to remove the Move from Android option in the Restore pane. Available in iOS 9 and later.
- `Appearance` (string): The key to skip the Choose Your Look screen. Available in iOS 13 and later, and macOS 10.14 and later.
- `AppleID` (string): The key to skip Apple Account setup. Available in iOS 7 and later, macOS 10.9 and later, tvOS 10.2 and later, and visionOS 26 and later.
- `AppStore` (string): The key to skip the App Store pane. Available in iOS 14.3 and later, and macOS 11.1 and later.
- `Biometric` (string): The key to skip biometric setup. Available in iOS 8.1 and later, macOS 10.12.4 and later, and visionOS 26 and later.
- `CameraButton` (string): The key to skip the Camera Button pane. Available in iOS 18 and later.
- `DeviceToDeviceMigration` (string): The key to skip Device to Device Migration pane. Available in iOS 12.4 and later.
- `Diagnostics` (string): The key to skip the App Analytics pane. Available in iOS 7 and later, macOS 10.9 and later, tvOS 10.2 and later, and visionOS 26 and later.
- `DisplayTone` (string): The key to skip DisplayTone setup. Available in iOS 9.3.2 and later, and macOS 10.13.6 and later. Deprecated in iOS 15 and later, and macOS 12 and later.
- `EnableLockdownMode` (string): The key to skip the Lockdown Mode pane if an Apple Account is set up. Available in iOS 17.1 and later, and macOS 14 and later.
- `FileVault` (string): The key to disable the FileVault Setup Assistant screen. Available in macOS 10.10 and later.
- `HomeButtonSensitivity` (string): The key to skip the Meet the New Home Button screen on iPhone 7, iPhone 7 Plus, iPhone 8, iPhone 8 Plus, and iPhone SE. Available in iOS 10 and later. Deprecated in iOS 15 and later.
- `iCloudDiagnostics` (string): The key to skip the iCloud Analytics screen. Available in macOS 10.12.4 and later.
- `iCloudStorage` (string): The key to skip the iCloud Documents and Desktop screen. Available in macOS 10.13.4 and later.
- `iMessageAndFaceTime` (string): The key to skip the iMessage and FaceTime screen. Available in iOS 12 and later.
- `Intelligence` (string): The key to skip the Intelligence pane. Available in iOS 18 and later, macOS 15 and later, and visionOS 26 and later.
- `Keyboard` (string): The key to skip the Keyboard pane. This pane isn’t always skippable because it appears before the device retrieves the Cloud Configuration from the server. Available in iOS 13 and later.
- `Location` (string): The key to disable Location Services. Available in iOS 7 and later, macOS 10.11 and later, tvOS 10.2 and later, and visionOS 26 and later.
- `MessagingActivationUsingPhoneNumber` (string): The key to skip the iMessage pane. Available in iOS 10 and later.
- `Multitasking` (string): The key to skip the Multitasking pane. Available in iOS 26 and later.
- `OnBoarding` (string): The key to skip the on-boarding informational screens for user education (Go Home, Cover Sheet, Multitasking & Control Center, for example). Available in iOS 11 and later. Deprecated in iOS 14 and later.
- `OSShowcase` (string): The key to skip the OS Showcase pane. Available in iOS 26 and later, and macOS 26.1 and later.
- `Passcode` (string): The key to hide and disable the passcode pane. Available in iOS 7 and later, macOS 10.9 and later, and visionOS 26 and later.
- `Payment` (string): The key to skip Apple Pay setup. Available in iOS 8.1 and later, macOS 10.12.4 and later, and visionOS 26 and later.
- `Privacy` (string): The key to skip the privacy pane. Available in iOS 11.3 and later, macOS 10.13.4 and later, tvOS 11.3 and later, and visionOS 26 and later.
- `Restore` (string): The key to disable restoring from backup. Available in iOS 7 and later, and macOS 10.9 and later.
- `RestoreCompleted` (string): The key to skip the Restore Completed pane. Available in iOS 14 and later.
- `Safety` (string): The key to skip the Safety pane. Available in iOS 16 and later.
- `SafetyAndHandling` (string): The key to skip the Safety and Handling pane. This pane isn’t always skippable because it appears before the device retrieves the Cloud Configuration from the server. Available in iOS 18.4 and later.
- `ScreenSaver` (string): The key to skip the tvOS screen about using aerial screensavers on an Apple TV. Available in tvOS 10.2 and later.
- `ScreenTime` (string): The key to skip the Screen Time pane. Available in iOS 12 and later, macOS 10.15 and later, and visionOS 26 and later.
- `SIMSetup` (string): The key to skip the add cellular plan pane. Skipping this pane prevents automatic eSIM setup during Setup Assistant. Available in iOS 12 and later.
- `Siri` (string): The key to disable Siri. Available in iOS 7 and later, macOS 10.12 and later, tvOS 10.2 and later, and visionOS 26 and later.
- `SoftwareUpdate` (string): The key to skip the mandatory software update screen. Available in iOS 12 and later, macOS 15.4 and later, and visionOS 26 and later.
- `SpokenLanguage` (string): The key to skip the Dictation pane. This pane isn’t always skippable because it appears before the device retrieves the Cloud Configuration from the server. Available in iOS 13 and later.
- `TapToSetup` (string): The key to skip the Tap To Set Up option in Apple TV related to using an iOS device to set up your Apple TV. Available in iOS 18 and later, and tvOS 10.2 and later.
- `TermsOfAddress` (string): The key to skip the Terms of Address pane. This key isn’t always skippable because this pane appears before the device retrieves the Cloud Configuration from the server. Available in iOS 16 and later, and macOS 13 and later.
- `Tips` (string): The key to skip the Tips pane. Available in visionOS 26 and later.
- `TOS` (string): The key to skip Terms and Conditions. Available in iOS 7 and later, macOS 10.9 and later, tvOS 10.2 and later, and visionOS 26 and later.
- `TVHomeScreenSync` (string): The key to skip TV Home Screen layout sync screen. Available in tvOS 11 and later.
- `TVProviderSignIn` (string): The key to skip the TV provider sign in screen. Available in tvOS 11 and later.
- `TVRoom` (string): The key to skip the “Where is this Apple TV?” screen. Available in tvOS 11.4 and later.
- `UnlockWithWatch` (string): The key to skip the “Unlock with Apple Watch” screen. Available in macOS 15 and later.
- `UpdateCompleted` (string): The key to skip the Software Update Complete pane. Available in iOS 14 and later, and macOS 26.1 and later.
- `WatchMigration` (string): The key to skip the screen for watch migration. Available in iOS 11 and later.
- `WebContentFiltering` (string): The key to skip the Web Content Filtering pane. Available in iOS 18.2 and later.
- `Welcome` (string): The key to skip the Get Started pane. Available in iOS 13 and later, macOS 15 and later, and visionOS 26 and later.
- `Zoom` (string): The key to skip zoom setup. Available in iOS 8.3 and later, and visionOS 26 and later. Deprecated in iOS 17 and later.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/skipkeys)*