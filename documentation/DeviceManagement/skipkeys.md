# SkipKeys

**Framework**: Device Management  
**Kind**: dictionary

The list of skip keys for setup panes.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 7.0+
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

- `Accessibility` (string): The key to skip the Accessibility pane, when creating additional users. > **Note**:  This key doesn’t skip the Accessibility pane in Setup Assistant during initial device set up. It does skip the Accessibility pane when Setup Assistant runs due to a new user log in. Available: macOS 11+
- `AccessibilityAppearance` (string): The key to skip the Accessibility Appearance configuration pane. Available: iOS 17+ | iPadOS 17+
- `ActionButton` (string): The key to skip the Action Button configuration pane. Available: iOS 17+ | iPadOS 17+
- `Android` (string): If the Restore pane isn’t skipped, this is the key to remove the Move from Android option in the Restore pane. Available: iOS 9+ | iPadOS 9+
- `Appearance` (string): The key to skip the Choose Your Look screen. Available: iOS 13+ | iPadOS 13+ | macOS 10.14+
- `AppleID` (string): The key to skip Apple Account setup. Available: iOS 7+ | iPadOS 7+ | macOS 10.9+ | tvOS 10.2+ | visionOS 26+
- `AppStore` (string): The key to skip the App Store pane. Available: iOS 14.3+ | iPadOS 14.3+ | macOS 11.1+
- `Biometric` (string): The key to skip biometric setup. Available: iOS 8.1+ | iPadOS 8.1+ | macOS 10.12.4+ | visionOS 26+
- `CameraButton` (string): The key to skip the Camera Button pane. Available: iOS 18+ | iPadOS 18+
- `DeviceToDeviceMigration` (string): The key to skip Device to Device Migration pane. Available: iOS 12.4+ | iPadOS 12.4+
- `Diagnostics` (string): The key to skip the App Analytics pane. Available: iOS 7+ | iPadOS 7+ | macOS 10.9+ | tvOS 10.2+ | visionOS 26+
- `DisplayTone` (string): The key to skip DisplayTone setup. Available: iOS 9.3.2+ | iPadOS 9.3.2+ | macOS 10.13.6+
Deprecated: iOS 15+ | iPadOS 15+ | macOS 12+
- `EnableLockdownMode` (string): The key to skip the Lockdown Mode pane if an Apple Account is set up. Available: iOS 17.1+ | iPadOS 17.1+ | macOS 14+
- `FileVault` (string): The key to disable the FileVault Setup Assistant screen. Available: macOS 10.10+
- `HomeButtonSensitivity` (string): The key to skip the Meet the New Home Button screen on iPhone 7, iPhone 7 Plus, iPhone 8, iPhone 8 Plus, and iPhone SE. Available: iOS 10+ | iPadOS 10+
Deprecated: iOS 15+ | iPadOS 15+
- `iCloudDiagnostics` (string): The key to skip the iCloud Analytics screen. Available: macOS 10.12.4+
- `iCloudStorage` (string): The key to skip the iCloud Documents and Desktop screen. Available: macOS 10.13.4+
- `iMessageAndFaceTime` (string): The key to skip the iMessage and FaceTime screen. Available: iOS 12+ | iPadOS 12+
- `Intelligence` (string): The key to skip the Intelligence pane. Available: iOS 18+ | iPadOS 18+ | macOS 15+ | visionOS 26+
- `Keyboard` (string): The key to skip the Keyboard pane. This pane isn’t always skippable because it appears before the device retrieves the Cloud Configuration from the server. Available: iOS 13+ | iPadOS 13+
- `LiquidGlass` (string): The key to skip the Liquid Glass pane. Available: iOS 27+ | iPadOS 27+ | macOS 27+
- `Location` (string): The key to disable Location Services. Available: iOS 7+ | iPadOS 7+ | macOS 10.11+ | tvOS 10.2+ | visionOS 26+
- `MessagingActivationUsingPhoneNumber` (string): The key to skip the iMessage pane. Available: iOS 10+ | iPadOS 10+
- `Multitasking` (string): The key to skip the Multitasking pane. Available: iOS 26+ | iPadOS 26+
- `OnBoarding` (string): The key to skip the on-boarding informational screens for user education (Go Home, Cover Sheet, Multitasking & Control Center, for example). Available: iOS 11+ | iPadOS 11+
Deprecated: iOS 14+ | iPadOS 14+
- `OSShowcase` (string): The key to skip the OS Showcase pane. Available: iOS 26+ | iPadOS 26+ | macOS 26.1+
- `Passcode` (string): The key to hide and disable the passcode pane. Available: iOS 7+ | iPadOS 7+ | macOS 10.9+ | visionOS 26+
- `Payment` (string): The key to skip Apple Pay setup. Available: iOS 8.1+ | iPadOS 8.1+ | macOS 10.12.4+ | visionOS 26+
- `Privacy` (string): The key to skip the privacy pane. Available: iOS 11.3+ | iPadOS 11.3+ | macOS 10.13.4+ | tvOS 11.3+ | visionOS 26+
- `Restore` (string): The key to disable restoring from backup. Available: iOS 7+ | iPadOS 7+ | macOS 10.9+
- `RestoreCompleted` (string): The key to skip the Restore Completed pane. Available: iOS 14+ | iPadOS 14+
- `Safety` (string): The key to skip the Safety pane. Available: iOS 16+ | iPadOS 16+
- `SafetyAndHandling` (string): The key to skip the Safety and Handling pane. This pane isn’t always skippable because it appears before the device retrieves the Cloud Configuration from the server. Available: iOS 18.4+ | iPadOS 18.4+
- `ScreenSaver` (string): The key to skip the tvOS screen about using aerial screensavers on an Apple TV. Available: tvOS 10.2+
- `ScreenTime` (string): The key to skip the Screen Time pane. Available: iOS 12+ | iPadOS 12+ | macOS 10.15+ | visionOS 26+
- `SIMSetup` (string): The key to skip the add cellular plan pane. Skipping this pane prevents automatic eSIM setup during Setup Assistant. Available: iOS 12+ | iPadOS 12+
- `Siri` (string): The key to disable Siri. Available: iOS 7+ | iPadOS 7+ | macOS 10.12+ | tvOS 10.2+ | visionOS 26+
- `SoftwareUpdate` (string): The key to skip the mandatory software update screen. Available: iOS 12+ | iPadOS 12+ | macOS 15.4+ | visionOS 26+
- `SpokenLanguage` (string): The key to skip the Dictation pane. This pane isn’t always skippable because it appears before the device retrieves the Cloud Configuration from the server. Available: iOS 13+ | iPadOS 13+
- `TapToSetup` (string): The key to skip the Tap To Set Up option in Apple TV related to using an iOS device to set up your Apple TV. Available: iOS 18+ | iPadOS 18+ | tvOS 10.2+
- `TermsOfAddress` (string): The key to skip the Terms of Address pane. This key isn’t always skippable because this pane appears before the device retrieves the Cloud Configuration from the server. Available: iOS 16+ | iPadOS 16+ | macOS 13+
- `Tips` (string): The key to skip the Tips pane. Available: visionOS 26+
- `TOS` (string): The key to skip Terms and Conditions. Available: iOS 7+ | iPadOS 7+ | macOS 10.9+ | tvOS 10.2+ | visionOS 26+
- `TVHomeScreenSync` (string): The key to skip TV Home Screen layout sync screen. Available: tvOS 11+
- `TVProviderSignIn` (string): The key to skip the TV provider sign in screen. Available: tvOS 11+
- `TVRoom` (string): The key to skip the “Where is this Apple TV?” screen. Available: tvOS 11.4+
- `UnlockWithWatch` (string): The key to skip the “Unlock with Apple Watch” screen. Available: macOS 15+
- `UpdateCompleted` (string): The key to skip the Software Update Complete pane. Available: iOS 14+ | iPadOS 14+ | macOS 26.1+
- `WatchMigration` (string): The key to skip the screen for watch migration. Available: iOS 11+ | iPadOS 11+
- `Welcome` (string): The key to skip the Get Started pane. Available: iOS 13+ | iPadOS 13+ | macOS 15+ | visionOS 26+
- `Zoom` (string): The key to skip zoom setup. Available: iOS 8.3+ | iPadOS 8.3+ | visionOS 26+
Deprecated: iOS 17+ | iPadOS 17+


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/skipkeys)*