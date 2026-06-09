# Restrictions

**Framework**: Device Management  
**Kind**: dictionary

The payload that configures restrictions on a device.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 4.0+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.1+
- watchOS 10.0+

## Declaration

```swift
object Restrictions
```

#### Discussion

Specify `com.apple.applicationaccess` as the payload type.

> ❗ **Important**:  The system allows multiple Restrictions payloads. However, don’t attempt to manage the same restriction in different payloads. Doing so results in unexpected behavior.

##### Profile Availability

|  |  |
| --- | --- |
| Device channel | iOS, macOS, Shared iPad, tvOS, visionOS, watchOS |
| User channel | macOS, Shared iPad |
| Allow manual install | iOS, macOS, tvOS, visionOS, watchOS |
| Requires supervision | N/A |
| Requires user-approved MDM | N/A |
| Allowed in user enrollment | iOS, macOS, visionOS |
| Allow multiple payloads | iOS, macOS, Shared iPad, tvOS, visionOS, watchOS |

##### Profile Example

```plist
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>PayloadContent</key>
    <array>
        <dict>
            <key>allowActivityContinuation</key>
            <false/>
            <key>blockedAppBundleIDs</key>
            <array>
                <string>com.apple.mobilesafari</string>
            </array>
            <key>ratingApps</key>
            <integer>500</integer>
            <key>PayloadIdentifier</key>
            <string>com.example.myrestrictionspayload</string>
            <key>PayloadType</key>
            <string>com.apple.applicationaccess</string>
            <key>PayloadUUID</key>
            <string>53bec1be-ffec-4f88-acbd-b02aee8f04a9</string>
            <key>PayloadVersion</key>
            <integer>1</integer>
        </dict>
    </array>
    <key>PayloadDisplayName</key>
    <string>Restrictions</string>
    <key>PayloadIdentifier</key>
    <string>com.example.myprofile</string>
    <key>PayloadType</key>
    <string>Configuration</string>
    <key>PayloadUUID</key>
    <string>6020206c-12c2-4ada-987a-dd4c560ca73a</string>
    <key>PayloadVersion</key>
    <integer>1</integer>
</dict>
</plist>
```

## Properties

- `allowAccountModification` (boolean): If `false`, the system disables modification of accounts, such as Apple Accounts, and internet-based accounts, such as Mail, Contacts, and Calendar. Available: iOS 7+ | iPadOS 7+ | macOS 14+ | visionOS 2+ | watchOS 10+
Requires supervision: iOS | visionOS | watchOS
- `allowActivityContinuation` (boolean): If `false`, the system disables activity continuation. Support for this restriction on unsupervised devices and with Managed Apple Accounts is deprecated. In a future release, this restriction will begin requiring supervision and will apply to personal Apple Accounts only. Available: iOS 8+ | iPadOS 8+ | macOS 10.15+ | visionOS 2+
- `allowAddingGameCenterFriends` (boolean): If `false`, the system prohibits adding friends to Game Center. Requires a supervised device in iOS 13 and later. Available: iOS 4.2.1+ | iPadOS 4.2.1+ | macOS 10.13+
Requires supervision: iOS
- `allowAirDrop` (boolean): If `false`, the system disables AirDrop. Available: iOS 7+ | iPadOS 7+ | macOS 10.13+ | visionOS 2+
Requires supervision: iOS | visionOS
- `allowAirPlayIncomingRequests` (boolean): If `false`, the system disables incoming AirPlay requests. Available: macOS 12.3+ | tvOS 10.2+
Requires supervision: tvOS
- `allowAirPrint` (boolean): If `false`, the system disables AirPrint. Available: iOS 11+ | iPadOS 11+
Requires supervision: iOS
- `allowAirPrintCredentialsStorage` (boolean): If `false`, the system disables Keychain storage of user name and password for AirPrint. Available: iOS 11+ | iPadOS 11+
Requires supervision: iOS
- `allowAirPrintiBeaconDiscovery` (boolean): If `false`, the system disables iBeacon discovery of AirPrint printers, which prevents spurious AirPrint Bluetooth beacons from phishing for network traffic. Available: iOS 11+ | iPadOS 11+
Requires supervision: iOS
- `allowAppCellularDataModification` (boolean): If `false`, the system disables changing settings for cellular data usage for apps. Available: iOS 7+ | iPadOS 7+
Requires supervision: iOS
- `allowAppClips` (boolean): If `false`, the system prevents a user from adding any App Clips, and removes any existing App Clips on the device. Available: iOS 14+ | iPadOS 14+
Requires supervision: iOS
- `allowAppInstallation` (boolean): If `false`, the system disables the App Store and removes its icon from the Home Screen. Users are unable to install or update their apps. This applies to App Store apps, marketplace apps, and locally installed apps (using Configurator, Xcode, and so forth). In iOS 10 and later, MDM commands can override this restriction. Requires a supervised device in iOS 13 and later. Available: iOS 4+ | iPadOS 4+ | visionOS 2+ | watchOS 10+
Requires supervision: iOS | visionOS | watchOS
- `allowAppleIntelligenceReport` (boolean): If `false`, the system disables Apple Intelligence reports. Deprecated: use the declarative management `com.apple.configuration.intelligence.settings` configuration. Available: iOS 18.4+ | iPadOS 18.4+ | macOS 15.4+
Deprecated: iOS 26.4+ | iPadOS 26.4+ | macOS 26.4+
Requires supervision: iOS
- `allowApplePersonalizedAdvertising` (boolean): If `false`, the system limits Apple personalized advertising. Available: iOS 14+ | iPadOS 14+ | macOS 12+ | visionOS 2+
- `allowAppRemoval` (boolean): If `false`, the system disables removal of apps from an iOS device. This applies to App Store apps, marketplace apps, and locally installed apps (using Configurator, Xcode, and so forth). Available: iOS 4.2.1+ | iPadOS 4.2.1+ | watchOS 10+
Requires supervision: iOS | watchOS
- `allowAppsToBeHidden` (boolean): If `false`, disables the ability for the user to hide apps. It doesn’t affect the user’s ability to leave it in the App Library, while removing it from the Home Screen. Available: iOS 18+ | iPadOS 18+
Requires supervision: iOS
- `allowAppsToBeLocked` (boolean): If `false`, disables the ability for the user to lock apps. Because hiding apps also requires locking them, disallowing locking also disallows hiding. Available: iOS 18+ | iPadOS 18+
Requires supervision: iOS
- `allowARDRemoteManagementModification` (boolean): If `false`, the system prevents modifying the Remote Management Sharing setting in System Settings. Available: macOS 14+
- `allowAssistant` (boolean): If `false`, the system disables Siri. Deprecated: use the declarative management `com.apple.configuration.siri.settings` configuration. Available: iOS 5+ | iPadOS 5+ | macOS 14+ | visionOS 2+
Deprecated: iOS 26.4+ | iPadOS 26.4+ | macOS 26.4+ | visionOS 26.4+
Allowed for user enrollments: iOS | visionOS
- `allowAssistantUserGeneratedContent` (boolean): If `false`, the system prevents Siri from querying user-generated content from the web. Deprecated: use the declarative management `com.apple.configuration.siri.settings` configuration. Available: iOS 7+ | iPadOS 7+ | watchOS 10+
Deprecated: iOS 26.4+ | iPadOS 26.4+ | watchOS 26.4+
Requires supervision: iOS | watchOS
- `allowAssistantWhileLocked` (boolean): If `false`, the system disables Siri when the device is locked. The system ignores this restriction if the device doesn’t have a passcode set. Deprecated: use the declarative management `com.apple.configuration.siri.settings` configuration. Available: iOS 5.1+ | iPadOS 5.1+ | watchOS 10+
Deprecated: iOS 26.4+ | iPadOS 26.4+ | watchOS 26.4+
Allowed for user enrollments: iOS
- `allowAutoCorrection` (boolean): If `false`, the system disables keyboard autocorrection. Deprecated: use the declarative management `com.apple.configuration.keyboard.settings` configuration. Available: iOS 8.1.3+ | iPadOS 8.1.3+
Deprecated: iOS 26.4+ | iPadOS 26.4+
Requires supervision: iOS
- `allowAutoDim` (boolean): If `false`, disables auto dim on iPads with OLED displays. Available: iOS 17.4+ | iPadOS 17.4+
Requires supervision: iOS
- `allowAutomaticAppDownloads` (boolean): If `false`, the system prevents automatic downloading of apps purchased on other devices. This setting doesn’t affect updates to existing apps. Available: iOS 9+ | iPadOS 9+ | watchOS 10+
Requires supervision: iOS | watchOS
- `allowAutomaticScreenSaver` (boolean): If `false`, the system disables Apple TV’s automatic screen saver. Available: tvOS 15.4+
Requires supervision: tvOS
- `allowAutoUnlock` (boolean): If `false`, the system disallows auto unlock. Support for this restriction on unsupervised devices is deprecated. Available: iOS 14.5+ | iPadOS 14.5+ | macOS 10.12+
- `allowBluetoothModification` (boolean): If `false`, the system prevents modification of Bluetooth settings. Available: iOS 11+ | iPadOS 11+ | macOS 13+ | visionOS 27+
Requires supervision: iOS | visionOS
- `allowBluetoothSharingModification` (boolean): If `false`, the system prevents modifying Bluetooth settings in System Settings. Available: macOS 14+
- `allowBookstore` (boolean): If `false`, the system removes the Book Store tab from the Books app. Available: iOS 6+ | iPadOS 6+ | macOS 15+
Requires supervision: iOS
- `allowBookstoreErotica` (boolean): If `false`, the system prevents the user from downloading Apple Books media that’s tagged as erotica. Support for this restriction on unsupervised devices is deprecated. Available: iOS 6+ | iPadOS 6+ | macOS 15+ | tvOS 11.3+
Deprecated: tvOS 17+
- `allowCallRecording` (boolean): If `false`, disables call recording. Available: iOS 18.1+ | iPadOS 18.1+ | macOS 26+
Requires supervision: iOS
- `allowCamera` (boolean): If `false`, the system disables the camera and removes its icon from the Home Screen, and users are unable to take photographs. Support for this restriction on unsupervised devices is deprecated. Available: iOS 4+ | iPadOS 4+ | macOS 10.11+ | tvOS 17+ | visionOS 2+
- `allowCellularPlanModification` (boolean): If `false`, the system prevents users from changing settings related to their cellular plan (available only on select carriers). Available: iOS 11+ | iPadOS 11+
Requires supervision: iOS
- `allowChat` (boolean): If `false`, the system disables the use of iMessage with supervised devices. If the device supports text messaging, the user can still send and receive text messages. Available: iOS 5+ | iPadOS 5+ | visionOS 27+
Requires supervision: iOS | visionOS
- `allowCloudAddressBook` (boolean): If `false`, the system disables iCloud Contacts services. Available: macOS 10.12+
- `allowCloudBackup` (boolean): If `false`, the system disables backing up the device to iCloud. Support for this restriction on unsupervised devices is deprecated. Available: iOS 5+ | iPadOS 5+ | visionOS 2+
- `allowCloudBookmarks` (boolean): If `false`, the system disables iCloud Bookmark sync. Available: macOS 10.12+
- `allowCloudCalendar` (boolean): If `false`, the system disables iCloud Calendar services. Available: macOS 10.12+
- `allowCloudDesktopAndDocuments` (boolean): If `false`, the system disables iCloud Desktop and Document services. Available: macOS 10.12.4+
- `allowCloudDocumentSync` (boolean): If `false`, the system disables document and key-value syncing to iCloud. Requires a supervised device in iOS 13 and later, and Shared iPad doesn’t support it. Support for this restriction on unsupervised devices and with Managed Apple Accounts is deprecated. Available: iOS 5+ | iPadOS 5+ | macOS 10.11+ | visionOS 2+
Requires supervision: iOS | visionOS
- `allowCloudFreeform` (boolean): If `false`, the system disallows iCloud Freeform services. Available: macOS 14+
- `allowCloudKeychainSync` (boolean): If `false`, the system disables iCloud Keychain synchronization. Support for this restriction on unsupervised devices and with Managed Apple Accounts is deprecated. Available: iOS 7+ | iPadOS 7+ | macOS 10.12+ | visionOS 2+
- `allowCloudMail` (boolean): If `false`, the system disables iCloud Mail services. Available: macOS 10.12+
- `allowCloudNotes` (boolean): If `false`, the system disables iCloud Notes services. Available: macOS 10.12+
- `allowCloudPhotoLibrary` (boolean): If `false`, the system disables iCloud Photo Library. The system removes any photos from local storage that aren’t fully downloaded from iCloud Photo Library to the device. Support for this restriction on unsupervised devices and with Managed Apple Accounts is deprecated. Available: iOS 9+ | iPadOS 9+ | macOS 10.12+ | visionOS 2+
- `allowCloudPrivateRelay` (boolean): If `false`, the system disables iCloud Private Relay. Support for this restriction on unsupervised devices and with Managed Apple Accounts is deprecated. Available: iOS 15+ | iPadOS 15+ | macOS 12+ | visionOS 2+
Requires supervision: iOS | visionOS
- `allowCloudReminders` (boolean): If `false`, the system disables iCloud Reminder services. Available: macOS 10.12+
- `allowContentCaching` (boolean): If `false`, the system disables content caching. This restriction is not supported on the user channel. Available: macOS 10.13+
- `allowContinuousPathKeyboard` (boolean): If `false`, the system disables QuickPath keyboard. Deprecated: use the declarative management `com.apple.configuration.keyboard.settings` configuration. Available: iOS 13+ | iPadOS 13+
Deprecated: iOS 26.4+ | iPadOS 26.4+
Requires supervision: iOS
- `allowDefaultBrowserModification` (boolean): If `false`, disables default browser preference modification. The MDM Settings command to set the default browser preference still works when applying this. Available: iOS 18.2+ | iPadOS 18.2+
Requires supervision: iOS
- `allowDefaultCallingAppModification` (boolean): If `false`, disables default calling app preference modification. The MDM Settings command to set the default calling app preference still works when applying this. Available: iOS 18.4+ | iPadOS 18.4+
Requires supervision: iOS
- `allowDefaultMessagingAppModification` (boolean): If `false`, disables default messaging app preference modification. The MDM Settings command to set the default messaging app preference still works when applying this. Available: iOS 18.4+ | iPadOS 18.4+
Requires supervision: iOS
- `allowDefinitionLookup` (boolean): If `false`, the system disables definition lookup. Deprecated: use the declarative management `com.apple.configuration.keyboard.settings` configuration. Available: iOS 8.1.3+ | iPadOS 8.1.3+ | macOS 10.11+
Deprecated: iOS 26.4+ | iPadOS 26.4+ | macOS 26.4+
Requires supervision: iOS
- `allowDeviceNameModification` (boolean): If `false`, the system prevents the user from changing the device name. Available: iOS 9+ | iPadOS 9+ | macOS 14+ | tvOS 11+ | visionOS 2+
Requires supervision: iOS | tvOS | visionOS
- `allowDeviceSleep` (boolean): If `false`, the system prevents the device from automatically sleeping. Available: tvOS 13+
Requires supervision: tvOS
- `allowDiagnosticSubmission` (boolean): If `false`, the system prevents the device from automatically submitting diagnostic reports to Apple. Available: iOS 6+ | iPadOS 6+ | macOS 10.13+ | visionOS 2+ | watchOS 10+
Allowed for user enrollments: iOS | macOS | visionOS
- `allowDiagnosticSubmissionModification` (boolean): If `false`, the system disables changing the diagnostic submission and app analytics settings in the Diagnostics & Usage UI in Settings. Available: iOS 9.3.2+ | iPadOS 9.3.2+ | visionOS 2+
Requires supervision: iOS | visionOS
- `allowDictation` (boolean): If `false`, the system disallows dictation input. Deprecated: use the declarative management `com.apple.configuration.keyboard.settings` configuration. Available: iOS 10.3+ | iPadOS 10.3+ | macOS 10.13+
Deprecated: iOS 26.4+ | iPadOS 26.4+ | macOS 26.4+
Requires supervision: iOS
- `allowedCameraRestrictionBundleIDs` ([string]): If present, the system exempts apps with bundle IDs in the array from the `allowCamera` restriction. The system doesn’t grant these apps access to the camera automatically; they’re only exempted from the `allowCamera` restriction. This key has no effect when the camera isn’t restricted. Multiple payloads combine using an intersect operation. Requires a supervised device. Available: iOS 26+ | iPadOS 26+
Requires supervision: iOS
- `allowedExternalIntelligenceWorkspaceIDs` ([string]): An array of strings, but currently restricted to a single element. If present, Apple Intelligence allows use of only the given external integration workspace ID, and requires a sign-in to make requests. The user is required to sign in to integrations that support signing in. Multiple payloads combine using an intersect operation. This means the allowed set of workspace IDs can become the empty set if multiple payloads specify conflicting values. Deprecated: use the declarative management `com.apple.configuration.external-intelligence.settings` configuration. Available: iOS 18.3+ | iPadOS 18.3+ | macOS 15.3+ | visionOS 2.4+
Deprecated: iOS 26.4+ | iPadOS 26.4+ | macOS 26.4+ | visionOS 26.4+
Requires supervision: iOS | visionOS
- `allowEnablingRestrictions` (boolean): If `false`, the system disables the Enable Restrictions option in the Restrictions UI in Settings. If `false` in iOS 12 and later, the system disables the Enable ScreenTime option in the ScreenTime UI in Settings and disables ScreenTime if already enabled. Available: iOS 8+ | iPadOS 8+ | visionOS 2+
Requires supervision: iOS | visionOS
- `allowEnterpriseAppTrust` (boolean): If `false`, the system removes the Trust Enterprise Developer button in Settings > General > VPN & Device Management, which prevents provisioning apps by universal provisioning profiles. This restriction applies to free developer accounts and enterprise app developers that aren’t implicitly trusted by apps that install through MDM. This restriction doesn’t revoke previously granted trust. Available: iOS 9+ | iPadOS 9+ | visionOS 2+
- `allowEnterpriseBookBackup` (boolean): If `false`, the system disables backup of Enterprise books. Available: iOS 8+ | iPadOS 8+
Allowed for user enrollments: iOS
- `allowEnterpriseBookMetadataSync` (boolean): If `false`, the system disables sync of Enterprise books, notes, and highlights. Available: iOS 8+ | iPadOS 8+
Allowed for user enrollments: iOS
- `allowEraseContentAndSettings` (boolean): If `false`, the system disables the Erase All Content and Settings option in the Reset UI. Available: iOS 8+ | iPadOS 8+ | macOS 12+ | visionOS 2+
Requires supervision: iOS | visionOS
- `allowESIMModification` (boolean): If `false`, the system disables modifications of eSIMs. This also disables the phone number sharing setup on iPhones, in iOS 27 and later. Available: iOS 12.1+ | iPadOS 12.1+
Requires supervision: iOS
- `allowESIMOutgoingTransfers` (boolean): If `false`, prevents the transfer of an eSIM from the device on which the restriction is installed to a different device. Available: iOS 18+ | iPadOS 18+
Requires supervision: iOS
- `allowExplicitContent` (boolean): If `false`, the system hides explicit music or video content purchased from the iTunes Store. The system marks explicit content as such by content providers, such as record labels, when sold through the iTunes Store. Explicit content in the News and Podcast apps is also hidden. Requires a supervised device in iOS 13 and later. Support for this restriction on unsupervised devices is deprecated. Available: iOS 4+ | iPadOS 4+ | macOS 15+ | tvOS 11.3+
Requires supervision: iOS | tvOS
- `allowExternalIntelligenceIntegrations` (boolean): If `false`, disables the use of external, cloud-based intelligence services with Siri. In iOS, this restriction is temporarily allowed on unsupervised and user enrollments. In a future release, this restriction will require supervision, and will be ignored on unsupervised devices. Deprecated: use the declarative management `com.apple.configuration.external-intelligence.settings` configuration. Available: iOS 18.2+ | iPadOS 18.2+ | macOS 15.2+ | visionOS 2.4+
Deprecated: iOS 26.4+ | iPadOS 26.4+ | macOS 26.4+ | visionOS 26.4+
Allowed for user enrollments: iOS | macOS | visionOS
- `allowExternalIntelligenceIntegrationsSignIn` (boolean): If `false`, forces external intelligence providers into anonymous mode. If a user is already signed in to an external intelligence provider, applying this restriction signs them out when attempting the next request. Deprecated: use the declarative management `com.apple.configuration.external-intelligence.settings` configuration. Available: iOS 18.2+ | iPadOS 18.2+ | macOS 15.2+ | visionOS 2.4+
Deprecated: iOS 26.4+ | iPadOS 26.4+ | macOS 26.4+ | visionOS 26.4+
Allowed for user enrollments: iOS | macOS | visionOS
- `allowFileSharingModification` (boolean): If `false`, the system prevents modifying File Sharing setting in System Settings. Available: macOS 14+
- `allowFilesNetworkDriveAccess` (boolean): If `false`, the system prevents connecting to network drives in the Files app. Available: iOS 13.1+ | iPadOS 13.1+ | visionOS 2+
Requires supervision: iOS | visionOS
- `allowFilesUSBDriveAccess` (boolean): If `false`, the system prevents connecting to any connected USB devices in the Files app. Available: iOS 13+ | iPadOS 13+
Requires supervision: iOS
- `allowFindMyDevice` (boolean): If `false`, the system disables Find My Device in the Find My app. Available: iOS 13+ | iPadOS 13+ | macOS 10.15+
Requires supervision: iOS
- `allowFindMyFriends` (boolean): If `false`, the system disables Find My Friends in the Find My app. Available: iOS 13+ | iPadOS 13+ | macOS 10.15+
Requires supervision: iOS
- `allowFindMyFriendsModification` (boolean): If `false`, the system disables changes to Find My Friends. Available: iOS 7+ | iPadOS 7+
Requires supervision: iOS
- `allowFingerprintForUnlock` (boolean): If `false`, the system prevents Touch ID, Face ID, or Optic ID from unlocking a device. Support for this restriction on unsupervised devices is deprecated. Available: iOS 7+ | iPadOS 7+ | macOS 10.12.4+ | visionOS 2+
- `allowFingerprintModification` (boolean): If `false`, the system prevents the user from modifying Touch ID or Face ID. Available: iOS 8.3+ | iPadOS 8.3+ | macOS 14+ | visionOS 2+
Requires supervision: iOS | visionOS
- `allowGameCenter` (boolean): If `false`, the system disables Game Center, and the system removes its icon from the Home Screen. Available: iOS 6+ | iPadOS 6+ | macOS 10.13+
Requires supervision: iOS
- `allowGenmoji` (boolean): If `false`, prohibits creating new Genmoji. Deprecated: use the declarative management `com.apple.configuration.intelligence.settings` configuration. Available: iOS 18+ | iPadOS 18+ | macOS 15+ | visionOS 2.4+
Deprecated: iOS 26.4+ | iPadOS 26.4+ | macOS 26.4+ | visionOS 26.4+
Requires supervision: iOS | visionOS
- `allowGlobalBackgroundFetchWhenRoaming` (boolean): If `false`, the system disables global background fetch activity when an iOS phone is roaming. Support for this restriction on unsupervised devices is deprecated. Available: iOS 4+ | iPadOS 4+
- `allowHostPairing` (boolean): If `false`, the system disables host pairing with the exception of the supervision host. If there’s no configured supervision host certificate, the system disables all pairing. Host pairing lets the administrator control whether an iOS device can pair with a host Mac or PC. Available: iOS 7+ | iPadOS 7+
Requires supervision: iOS
- `allowImagePlayground` (boolean): If `false`, prohibits the use of image generation. Deprecated: use the declarative management `com.apple.configuration.intelligence.settings` configuration. Available: iOS 18+ | iPadOS 18+ | macOS 15+ | visionOS 2.4+
Deprecated: iOS 26.4+ | iPadOS 26.4+ | macOS 26.4+ | visionOS 26.4+
Requires supervision: iOS | visionOS
- `allowImageWand` (boolean): If `false`, prohibits the use of Image Wand. Deprecated: use the declarative management `com.apple.configuration.intelligence.settings` configuration. Available: iOS 18+ | iPadOS 18+ | visionOS 2.4+
Deprecated: iOS 26.4+ | iPadOS 26.4+ | visionOS 26.4+
Requires supervision: iOS | visionOS
- `allowInAppPurchases` (boolean): If `false`, the system prohibits in-app purchasing. Support for this restriction on unsupervised devices is deprecated. Available: iOS 4+ | iPadOS 4+
- `allowInternetSharingModification` (boolean): If `false`, the system prevents modifying the Internet Sharing setting in System Settings. Available: macOS 14+
- `allowiPhoneMirroring` (boolean): If `false`, prohibits the use of iPhone Mirroring. In macOS, this prevents the Mac from mirroring any iPhone. In iOS, this prevents the iPhone from mirroring to any Mac. Available: iOS 18+ | iPadOS 18+ | macOS 15+
Requires supervision: iOS
- `allowiPhoneWidgetsOnMac` (boolean): If `false`, the system disallows iPhone widgets on a Mac that signs in with the same Apple Account for iCloud. Available: iOS 17+ | iPadOS 17+
Requires supervision: iOS
- `allowiTunes` (boolean): If `false`, the system disables the iTunes Music Store and removes its icon from the Home Screen. Users can’t preview, purchase, or download content. Requires a supervised device in iOS 13 and later. Available: iOS 4+ | iPadOS 4+
Requires supervision: iOS
- `allowiTunesFileSharing` (boolean): If `false`, the system disables iTunes file sharing services. Available: macOS 10.13+
- `allowKeyboardShortcuts` (boolean): If `false`, the system disables keyboard shortcuts. Deprecated: use the declarative management `com.apple.configuration.keyboard.settings` configuration. Available: iOS 9+ | iPadOS 9+
Deprecated: iOS 26.4+ | iPadOS 26.4+
Requires supervision: iOS
- `allowListedAppBundleIDs` ([string]): If present, the system only shows or can launch apps with bundle IDs in the array. Include the value `com.apple.webapp` to allow all webclips. This applies to App Store apps, marketplace apps, and locally installed apps (using Configurator, Xcode, and so forth). Deprecated: use the declarative management `com.apple.configuration.app.settings` configuration. Available: iOS 15+ | iPadOS 15+ | tvOS 15+ | visionOS 27+
Deprecated: iOS 27+ | iPadOS 27+ | tvOS 27+ | visionOS 27+
Requires supervision: iOS | tvOS | visionOS
- `allowLiveVoicemail` (boolean): If `false`, the system disables live voicemail on the device. Available: iOS 17.2+ | iPadOS 17.2+ | macOS 26+
Requires supervision: iOS
- `allowLocalUserCreation` (boolean): If `false`, the system prevents creating users in System Settings. Available: macOS 14+
- `allowLockScreenControlCenter` (boolean): If `false`, the system prevents Control Center from appearing on the Lock Screen. Available: iOS 7+ | iPadOS 7+
Allowed for user enrollments: iOS
- `allowLockScreenNotificationsView` (boolean): If `false`, the system disables the Notifications history view on the Lock Screen, so users can’t view past notifications. However, they can still see notifications when they arrive. Available: iOS 7+ | iPadOS 7+ | watchOS 10+
Allowed for user enrollments: iOS
- `allowLockScreenTodayView` (boolean): If `false`, the system disables the Today view in Notification Center on the Lock Screen. Available: iOS 7+ | iPadOS 7+
Allowed for user enrollments: iOS
- `allowMailPrivacyProtection` (boolean): If `false`, the system disables Mail Privacy Protection on the device. Available: iOS 15.2+ | iPadOS 15.2+
Requires supervision: iOS
- `allowMailSmartReplies` (boolean): If `false`, disables smart replies in Mail. Deprecated: use the declarative management `com.apple.configuration.intelligence.settings` configuration. Available: iOS 18.4+ | iPadOS 18.4+ | macOS 15.4+ | visionOS 2.4+
Deprecated: iOS 26.4+ | iPadOS 26.4+ | macOS 26.4+ | visionOS 26.4+
Requires supervision: iOS | visionOS
- `allowMailSummary` (boolean): If `false`, disables the ability to create summaries of email messages manually. This doesn’t affect automatic summary generation. Deprecated: use the declarative management `com.apple.configuration.intelligence.settings` configuration. Available: iOS 18.1+ | iPadOS 18.1+ | macOS 15.1+ | visionOS 2.4+
Deprecated: iOS 26.4+ | iPadOS 26.4+ | macOS 26.4+ | visionOS 26.4+
Requires supervision: iOS | visionOS
- `allowManagedAppsCloudSync` (boolean): If `false`, the system prevents managed apps from using iCloud sync. Available: iOS 8+ | iPadOS 8+ | visionOS 2+
Allowed for user enrollments: iOS | visionOS
- `allowManagedToWriteUnmanagedContacts` (boolean): If `true`, the system allows managed apps to write contacts to unmanaged accounts. If `allowOpenFromManagedToUnmanaged` is `true`, this restriction has no effect. > ❗ **Important**:  Use MDM to install profiles that contain this restriction. Available: iOS 12+ | iPadOS 12+ | visionOS 2+
- `allowMarketplaceAppInstallation` (boolean): If `false`, the system prevents installation of alternative marketplace apps from the web and prevents any installed alternative marketplace apps from installing apps. Available: iOS 17.4+ | iPadOS 17.4+
Requires supervision: iOS
- `allowMediaSharingModification` (boolean): If `false`, prevents modification of Media Sharing settings. Available: macOS 15.1+
- `allowMultiplayerGaming` (boolean): If `false`, the system prohibits multiplayer gaming. Available: iOS 4.1+ | iPadOS 4.1+ | macOS 10.13+
Requires supervision: iOS
- `allowMusicService` (boolean): If `false`, the system disables the Music service, and the Music app reverts to classic mode. Available: iOS 9.3+ | iPadOS 9.3+ | macOS 10.12+
Requires supervision: iOS
- `allowNews` (boolean): If `false`, the system disables News. Available: iOS 9+ | iPadOS 9+
Requires supervision: iOS
- `allowNFC` (boolean): If `false`, the system disables NFC. Available: iOS 14.2+ | iPadOS 14.2+
Requires supervision: iOS
- `allowNotesTranscription` (boolean): If `false`, disables transcription in Notes. Deprecated: use the declarative management `com.apple.configuration.intelligence.settings` configuration. Available: iOS 18.4+ | iPadOS 18.4+ | macOS 15.4+
Deprecated: iOS 26.4+ | iPadOS 26.4+ | macOS 26.4+
Requires supervision: iOS
- `allowNotesTranscriptionSummary` (boolean): If `false`, disables transcription summarization in Notes. Deprecated: use the declarative management `com.apple.configuration.intelligence.settings` configuration. Available: iOS 18.3+ | iPadOS 18.3+ | macOS 15.3+
Deprecated: iOS 26.4+ | iPadOS 26.4+ | macOS 26.4+
Requires supervision: iOS
- `allowNotificationsModification` (boolean): If `false`, the system disables modification of notification settings. Available: iOS 9.3+ | iPadOS 9.3+ | visionOS 2+
Requires supervision: iOS | visionOS
- `allowOpenFromManagedToUnmanaged` (boolean): If `false`, documents in managed apps and accounts open only in other managed apps and accounts. Available: iOS 7+ | iPadOS 7+ | visionOS 2+
Allowed for user enrollments: iOS | visionOS
- `allowOpenFromUnmanagedToManaged` (boolean): If `false`, documents in unmanaged apps and accounts open only in other unmanaged apps and accounts. Available: iOS 7+ | iPadOS 7+ | visionOS 2+
Allowed for user enrollments: iOS | visionOS
- `allowOTAPKIUpdates` (boolean): If `false`, the system disables over-the-air PKI updates. Setting this restriction to `false` doesn’t disable CRL and OCSP checks. Available: iOS 7+ | iPadOS 7+
- `allowPairedWatch` (boolean): If `false`, the system disables pairing with an Apple Watch, and the system unpairs any currently paired Apple Watch and erases its content. Available: iOS 9+ | iPadOS 9+
Requires supervision: iOS
- `allowPassbookWhileLocked` (boolean): If `false`, the system hides Passbook notifications from the Lock Screen. Available: iOS 6+ | iPadOS 6+
- `allowPasscodeModification` (boolean): If `false`, the system prevents adding, changing, or removing the passcode. The system ignores this restriction on Shared iPad. Available: iOS 9+ | iPadOS 9+ | macOS 10.13+ | visionOS 2+
Requires supervision: iOS | visionOS
- `allowPasswordAutoFill` (boolean): If `false`, the system disables: - The AutoFill Passwords feature in iOS, with Keychain and third-party password managers
- Prompting the user to use a saved password in Safari or in apps
- Automatic strong passwords
- Suggesting strong passwords to users However, if `false`, the system doesn’t prevent AutoFill for contact info and credit cards in Safari. Available: iOS 12+ | iPadOS 12+ | macOS 10.14+ | visionOS 2+
Requires supervision: iOS | visionOS
- `allowPasswordProximityRequests` (boolean): If `false`, the system disables requesting passwords from nearby devices. Available: iOS 12+ | iPadOS 12+ | macOS 10.14+ | tvOS 12+
Deprecated: tvOS 17.4+
Removed: tvOS 26.4+
Requires supervision: iOS | tvOS
- `allowPasswordSharing` (boolean): If `false`, the system disables sharing passwords with the AirDrop passwords feature, or with the Passwords app. Available: iOS 12+ | iPadOS 12+ | macOS 10.14+ | visionOS 2+
Requires supervision: iOS | visionOS
- `allowPersonalHotspotModification` (boolean): If `false`, the system disables modifications of the personal hotspot setting. Available: iOS 12.2+ | iPadOS 12.2+
Requires supervision: iOS
- `allowPersonalizedHandwritingResults` (boolean): If false, prevents the system from generating text in the user’s handwriting. Deprecated: use the declarative management `com.apple.configuration.intelligence.settings` configuration. Available: iOS 18+ | iPadOS 18+
Deprecated: iOS 26.4+ | iPadOS 26.4+
Requires supervision: iOS
- `allowPhotoStream` (boolean): If `false`, the system disables Photo Stream. Available: iOS 5+ | iPadOS 5+
Deprecated: iOS 17+ | iPadOS 17+
- `allowPodcasts` (boolean): If `false`, the system disables podcasts. Available: iOS 8+ | iPadOS 8+
Requires supervision: iOS
- `allowPredictiveKeyboard` (boolean): If `false`, the system disables predictive keyboards. Deprecated: use the declarative management `com.apple.configuration.keyboard.settings` configuration. Available: iOS 8.1.3+ | iPadOS 8.1.3+
Deprecated: iOS 26.4+ | iPadOS 26.4+
Requires supervision: iOS
- `allowPrinterSharingModification` (boolean): If `false`, the system prevents modifying Printer Sharing settings in System Settings. Available: macOS 14+
- `allowProximitySetupToNewDevice` (boolean): If `false`, disables the prompt to set up new devices that are nearby. Starting with iOS 26.3, this also prevents exporting iOS data to set up new Android devices. Available: iOS 11+ | iPadOS 11+
Requires supervision: iOS
- `allowRadioService` (boolean): If `false`, the system disables Apple Music Radio. Available: iOS 9.3+ | iPadOS 9.3+
Requires supervision: iOS
- `allowRCSMessaging` (boolean): If `false`, prevents the use of RCS messaging. Available: iOS 18.1+ | iPadOS 18.1+
Requires supervision: iOS
- `allowRemoteAppleEventsModification` (boolean): If `false`, the system prevents modifying Remote Apple Events Sharing settings in System Settings. Available: macOS 14+
- `allowRemoteAppPairing` (boolean): If `false`, the system disables pairing Apple TV for use with the Control Center widget. Available: tvOS 10.2+
Requires supervision: tvOS
- `allowRemoteScreenObservation` (boolean): If `false`, the system disables remote screen observation by the Classroom app. Nest this key beneath `allowScreenShot` as a subrestriction. If `allowScreenShot` is `false`, the Classroom app doesn’t observe remote screens. Requires a supervised device until iOS 13 and macOS 10.15. Allowed for user enrollments in macOS 12 and later. Available: iOS 9.3+ | iPadOS 9.3+ | macOS 10.14.4+
Allowed for user enrollments: iOS | macOS
- `allowRosettaUsageAwareness` (boolean): If `false`, disables Rosetta usage awareness. When Rosetta usage awareness is active, a pop-up dialog is displayed to the user when an app that is using Rosetta is launched. The pop-up dialog indicates that Rosetta will be removed in a future version of the operating system so that the user can contact the app vendor regarding a replacement for the current app. Available: macOS 26.4+
- `allowSafari` (boolean): If `false`, the system disables the Safari web browser app, and the system removes its icon from the Home Screen. This setting also prevents users from opening web clips. Requires a supervised device in iOS 13 and later. Available: iOS 4+ | iPadOS 4+
Requires supervision: iOS
- `allowSafariHistoryClearing` (boolean): If `false`, the system disables the ability to clear browsing history in Safari. Available: iOS 26+ | iPadOS 26+ | macOS 26+ | visionOS 26+
Requires supervision: iOS | visionOS
- `allowSafariPrivateBrowsing` (boolean): If `false`, the system disables the ability to use private browsing in Safari. Available: iOS 26+ | iPadOS 26+ | macOS 26+ | visionOS 26+
Requires supervision: iOS | visionOS
- `allowSafariSummary` (boolean): If `false`, the system disables the ability to summarize content in Safari. Deprecated: use the declarative management `com.apple.configuration.intelligence.settings` configuration. Available: iOS 18.4+ | iPadOS 18.4+ | macOS 15.4+ | visionOS 2.4+
Deprecated: iOS 26.4+ | iPadOS 26.4+ | macOS 26.4+ | visionOS 26.4+
Requires supervision: iOS | visionOS
- `allowSatelliteConnection` (boolean): If `false`, the system prohibits the connection to and use of satellite services. Available: iOS 18.2+ | iPadOS 18.2+
Requires supervision: iOS
- `allowScreenShot` (boolean): If `false`, the system disables saving a screenshot of the display and capturing a screen recording. It also disables the Classroom app from observing remote screens. Available: iOS 3.1+ | iPadOS 3.1+ | macOS 10.14.4+ | visionOS 2+ | watchOS 10+
Allowed for user enrollments: iOS | macOS | visionOS
- `allowSharedDeviceTemporarySession` (boolean): If `false`, the system makes temporary sessions unavailable on Shared iPad. Available: iOS 13.4+ | iPadOS 13.4+
Requires supervision: iOS
- `allowSharedStream` (boolean): If `false`, the system disables Shared Photo Stream. Support for this restriction on unsupervised devices is deprecated. Available: iOS 6+ | iPadOS 6+
- `allowSpellCheck` (boolean): If `false`, the system disables the keyboard spell checker. Deprecated: use the declarative management `com.apple.configuration.keyboard.settings` configuration. Available: iOS 8.1.3+ | iPadOS 8.1.3+
Deprecated: iOS 26.4+ | iPadOS 26.4+
Requires supervision: iOS
- `allowSpotlightInternetResults` (boolean): If `false`, the system disables Spotlight Internet search results in Siri Suggestions. Support for this restriction on unsupervised devices is deprecated. Available: iOS 8+ | iPadOS 8+ | macOS 10.11+
- `allowStartupDiskModification` (boolean): If `false`, the system prevents modification of Startup Disk settings in System Settings. Available: macOS 14+
- `allowSystemAppRemoval` (boolean): If `false`, the system disables the removal of system apps from the device. Available: iOS 11+ | iPadOS 11+ | visionOS 2+
Requires supervision: iOS | visionOS
- `allowTimeMachineBackup` (boolean): If `false`, the system prevents modification of Time Machine settings in System Settings. This restriction is not supported on the user channel. Available: macOS 14+
- `allowUIAppInstallation` (boolean): If `false`, the system disables the App Store and removes its icon from the Home Screen. However, users can continue to install or update their apps either locally (via Configurator, Xcode, and so forth), or using alternative marketplace apps. In iOS 10 and later, MDM commands can override this restriction. Available: iOS 9+ | iPadOS 9+ | visionOS 2+ | watchOS 10+
Requires supervision: iOS | visionOS | watchOS
- `allowUIConfigurationProfileInstallation` (boolean): If `false`, the system prohibits the user from installing configuration profiles and certificates interactively. Available: iOS 6+ | iPadOS 6+ | macOS 13+ | visionOS 2+
Requires supervision: iOS | visionOS
- `allowUniversalControl` (boolean): If `false`, the system disables Universal Control. Available: macOS 13+
- `allowUnmanagedToReadManagedContacts` (boolean): If `true`, the system allows unmanaged apps to read from managed contacts accounts. If `allowOpenFromManagedToUnmanaged` is `true`, this restriction has no effect. > ❗ **Important**:  Use MDM to install profiles that contain this restriction. Available: iOS 12+ | iPadOS 12+ | visionOS 2+
Allowed for user enrollments: iOS | visionOS
- `allowUnpairedExternalBootToRecovery` (boolean): If `true`, the system allows unpaired devices to boot devices into recovery. Available: iOS 14.5+ | iPadOS 14.5+
Requires supervision: iOS
- `allowUntrustedTLSPrompt` (boolean): If `false`, the system automatically rejects untrusted HTTPS certificates without prompting the user. Available: iOS 5+ | iPadOS 5+ | visionOS 1.1+
- `allowUSBRestrictedMode` (boolean): If `false`, the system allows iOS devices to always connect to USB accessories while locked. In macOS, allows new USB and Thunderbolt accessories, and SD cards to connect without authorization. If the system has Lockdown mode enabled, it ignores this value. This restriction is not supported on the user channel. Available: iOS 11.4.1+ | iPadOS 11.4.1+ | macOS 13+
Requires supervision: iOS
- `allowVideoConferencing` (boolean): If `false`, the system hides the FaceTime app. Requires a supervised device in iOS 13 and later. Available: iOS 4+ | iPadOS 4+ | visionOS 2+
Requires supervision: iOS | visionOS
- `allowVideoConferencingRemoteControl` (boolean): If `false`, disables the ability for a remote FaceTime session to request control of the device. Available: iOS 18.4+ | iPadOS 18.4+
Requires supervision: iOS
- `allowVisualIntelligenceSummary` (boolean): If `false`, the system disables visual intelligence summarization. Deprecated: use the declarative management `com.apple.configuration.intelligence.settings` configuration. Available: iOS 18.3+ | iPadOS 18.3+
Deprecated: iOS 26.4+ | iPadOS 26.4+
Requires supervision: iOS
- `allowVoiceDialing` (boolean): If `false`, the system disables voice dialing if the device is locked with a passcode. Available: iOS 4+ | iPadOS 4+
Deprecated: iOS 17+ | iPadOS 17+
- `allowVPNCreation` (boolean): If `false`, the system allows only managed apps to create VPN configurations. Prior to iOS 18, the system also allows unmanaged apps to create VPN configurations. Available: iOS 11+ | iPadOS 11+ | visionOS 2+
Requires supervision: iOS | visionOS
- `allowWallpaperModification` (boolean): If `false`, the system prevents changing the wallpaper. Available: iOS 9+ | iPadOS 9+ | macOS 10.13+
Requires supervision: iOS
- `allowWebDistributionAppInstallation` (boolean): If `false`, the device prevents installation of apps directly from the web. Available: iOS 17.5+ | iPadOS 17.5+
Requires supervision: iOS
- `allowWritingTools` (boolean): If `false`, disables Apple Intelligence writing tools. Deprecated: use the declarative management `com.apple.configuration.intelligence.settings` configuration. Available: iOS 18+ | iPadOS 18+ | macOS 15+ | visionOS 2.4+
Deprecated: iOS 26.4+ | iPadOS 26.4+ | macOS 26.4+ | visionOS 26.4+
Requires supervision: iOS | visionOS
- `autonomousSingleAppModePermittedAppIDs` ([string]): If present, the system allows apps identified by the bundle IDs listed in the array to autonomously enter Single App Mode. Available: iOS 7+ | iPadOS 7+
Requires supervision: iOS
- `blacklistedAppBundleIDs` ([string]): Deprecated: use the declarative management `com.apple.configuration.app.settings` configuration. Available: iOS 9.3+ | iPadOS 9.3+ | tvOS 11+
Deprecated: iOS 15+ | iPadOS 15+ | tvOS 15+
Requires supervision: iOS | tvOS
- `blockedAppBundleIDs` ([string]): If present, the system prevents showing or launching apps with bundle IDs in the array. Include the value `com.apple.webapp` to restrict all webclips. This applies to App Store apps, marketplace apps, and locally installed apps (using Configurator, Xcode, and so forth). Deprecated: use the declarative management `com.apple.configuration.app.settings` configuration. > **Note**:  Denying system apps may disable other functionality. For example, denying the App Store app may prevent users from accepting the terms and conditions for the user-based Volume Purchase Program (VPP). Available: iOS 15+ | iPadOS 15+ | tvOS 15+ | visionOS 27+
Deprecated: iOS 27+ | iPadOS 27+ | tvOS 27+ | visionOS 27+
Requires supervision: iOS | tvOS | visionOS
- `deniedICCIDsForiMessageFaceTime` ([string]): An array of strings representing ICCIDs of cellular plans. The device prevents use of any matching cellular networks in iMessage and FaceTime. The array must contain no more than 4 ICCID strings. Available: iOS 26+ | iPadOS 26+
Requires supervision: iOS
- `deniedICCIDsForRCS` ([string]): An array of strings representing ICCIDs of cellular plans. The device prevents use of any matching cellular networks with RCS messaging. The array must contain no more than 4 ICCID strings. Available: iOS 26+ | iPadOS 26+
Requires supervision: iOS
- `enforcedFingerprintTimeout` (integer): The value, in seconds, after which the fingerprint unlock requires a password to authenticate. The default value is 48 hours. Available: macOS 12+
- `forceAirDropUnmanaged` (boolean): If `true`, the system considers AirDrop to be an unmanaged drop target. Available: iOS 9+ | iPadOS 9+ | visionOS 2+
Allowed for user enrollments: iOS | visionOS
- `forceAirPlayIncomingRequestsPairingPassword` (boolean): If `true`, the system forces all devices sending AirPlay requests to this device to use a pairing password. This key isn’t supported in tvOS 10.2 and later. Use the AirPlay Security Payload instead. Available: tvOS 9+
- `forceAirPlayOutgoingRequestsPairingPassword` (boolean): If `true`, the system forces all devices receiving AirPlay requests from this device to use a pairing password. Available: iOS 7.1+ | iPadOS 7.1+
Allowed for user enrollments: iOS
- `forceAirPrintTrustedTLSRequirement` (boolean): If `true`, the system requires trusted certificates for TLS printing communication. Available: iOS 11+ | iPadOS 11+
Requires supervision: iOS
- `forceAssistantProfanityFilter` (boolean): If `true`, the system forces the use of the profanity filter for Siri and dictation. Requires a supervised device in iOS. Deprecated: use the declarative management `com.apple.configuration.siri.settings` configuration. Available: iOS 5+ | iPadOS 5+ | macOS 10.13+
Deprecated: iOS 26.4+ | iPadOS 26.4+ | macOS 26.4+
Requires supervision: iOS
- `forceAuthenticationBeforeAutoFill` (boolean): If `true`, the user needs to authenticate before the system can autofill passwords or credit card information in Safari and apps. If this restriction isn’t enforced, the user can toggle this feature in Settings. Only supported on devices with Face ID or Touch ID. Available: iOS 11+ | iPadOS 11+ | visionOS 2+
Requires supervision: iOS | visionOS
- `forceAutomaticDateAndTime` (boolean): If `true`, the system enables the Set Automatically feature in Date & Time and the user can’t disable it. The system updates the device’s time zone only when the device can determine its location using a cellular connection or Wi-Fi with location services enabled. Available: iOS 12+ | iPadOS 12+ | tvOS 12.2+ | visionOS 2+
Requires supervision: iOS | tvOS | visionOS
- `forceBypassScreenCaptureAlert` (boolean): If `true`, then the system bypasses the presentation of a screen capture alert. Available: macOS 15.1+
- `ForceCaptivePortalConnectionFromLockScreen` (boolean): If `true`, the system allows use of the captive WiFi portal at login or unlock. Available: macOS 27+
Requires supervision: macOS
- `forceClassroomAutomaticallyJoinClasses` (boolean): If `true`, the system automatically gives permission to the teacher’s requests without prompting the student. Available: iOS 11+ | iPadOS 11+ | macOS 10.14.4+
Requires supervision: iOS | macOS
- `forceClassroomRequestPermissionToLeaveClasses` (boolean): If `true`, a student enrolled in an unmanaged course through Classroom needs to request permission from the teacher to leave the course. Available: iOS 11.3+ | iPadOS 11.3+ | macOS 10.14.4+
Requires supervision: iOS | macOS
- `forceClassroomUnpromptedAppAndDeviceLock` (boolean): If `true`, the system allows the teacher to lock apps or the device without prompting the student. Available: iOS 11+ | iPadOS 11+ | macOS 10.14.4+
Requires supervision: iOS | macOS
- `forceClassroomUnpromptedScreenObservation` (boolean): If `true` and `ScreenObservationPermissionModificationAllowed` is also `true` in the Education payload, a student enrolled in a managed course through the Classroom app automatically gives permission to that course teacher’s requests to observe the student’s screen without prompting the student. Available: iOS 11+ | iPadOS 11+ | macOS 10.14.4+
Requires supervision: iOS | macOS
- `forceEncryptedBackup` (boolean): If `true`, the system encrypts all backups. Available: iOS 4+ | iPadOS 4+
Allowed for user enrollments: iOS
- `forceITunesStorePasswordEntry` (boolean): If `true`, the system forces the user to enter their iTunes password for each transaction. Available: iOS 6+ | iPadOS 6+
Deprecated: iOS 17+ | iPadOS 17+
- `forceLimitAdTracking` (boolean): If `true`, the system limits ad tracking. Additionally, it disables app tracking and the Allow Apps to Request to Track setting. Available: iOS 7+ | iPadOS 7+
- `forceOnDeviceOnlyDictation` (boolean): If `true`, the system disables connections to Siri servers for the purposes of dictation. Deprecated: use the declarative management `com.apple.configuration.intelligence.settings` configuration. Available: iOS 14.5+ | iPadOS 14.5+ | macOS 14+ | visionOS 2+ | watchOS 10+
Deprecated: iOS 26.4+ | iPadOS 26.4+ | macOS 26.4+ | visionOS 26.4+ | watchOS 26.4+
Allowed for user enrollments: iOS | macOS | visionOS
- `forceOnDeviceOnlyTranslation` (boolean): If `true`, the device can’t connect to Siri servers for the purposes of translation. Deprecated: use the declarative management `com.apple.configuration.intelligence.settings` configuration. Available: iOS 15+ | iPadOS 15+ | watchOS 10+
Deprecated: iOS 26.4+ | iPadOS 26.4+ | watchOS 26.4+
Allowed for user enrollments: iOS
- `forcePreserveESIMOnErase` (boolean): If `true`, the system preserves eSIM when it erases the device due to too many failed password attempts or the Erase All Content and Settings option in Settings > General > Reset. > **Note**:  The system doesn’t preserve eSIM if Find My initiates erasing the device. Available: iOS 17.2+ | iPadOS 17.2+
Requires supervision: iOS
- `forceWatchWristDetection` (boolean): If `true`, the system forces a paired Apple Watch to use Wrist Detection. Available: iOS 8.2+ | iPadOS 8.2+ | watchOS 10+
Allowed for user enrollments: iOS
- `ForceWifiConfigurationOnLockScreen` (boolean): If `true`, the system allows the user to select WiFi networks at login or unlock. Available: macOS 27+
Requires supervision: macOS
- `forceWiFiPowerOn` (boolean): If `true`, the system prevents turning off Wi-Fi in Settings or Control Center, even by entering or leaving Airplane Mode. It doesn’t prevent selecting which Wi-Fi network to use. and later. Available: iOS 13+ | iPadOS 13+
Requires supervision: iOS
- `forceWiFiToAllowedNetworksOnly` (boolean): If `true`, the system limits the device to only join Wi-Fi networks set up through a configuration profile. Available: iOS 14.5+ | iPadOS 14.5+ | visionOS 2+
Requires supervision: iOS | visionOS
- `forceWiFiWhitelisting` (boolean): Use `forceWiFiToAllowedNetworksOnly` instead. Available: iOS 10.3+ | iPadOS 10.3+
Deprecated: iOS 14.5+ | iPadOS 14.5+
Requires supervision: iOS
- `ratingApps` (integer): The maximum level of app content allowed on the device. Starting with iOS 26.2, this rating may apply to certain system apps. Age bands and the number of discrete age values vary by region, but the values are consistent across regions. For example, in a region that defines rating level 14+, its value is guaranteed to be larger than 300 (12+) and smaller than 600 (17+). Also, the value of rating level 15+ is guaranteed to be larger than the assigned value of rating level 14+. For more information about age ratings, see [`Age ratings values and definitions`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/reference/age-ratings-values-and-definitions). Below is the complete list of age rating values used across all App Store regions. - `1000`: All
- `621`: 21+
- `620`: 20+
- `619`: 19+
- `618`: 18+
- `600`: 17+
- `416`: 16+
- `415`: 15+
- `314`: 14+
- `313`: 13+
- `300`: 12+
- `211`: 11+
- `210`: 10+
- `200`: 9+
- `108`: 8+
- `107`: 7+
- `106`: 6+
- `105`: 5+
- `100`: 4+
- `3`: 3+
- `2`: 2+
- `1`: 1+
- `0`: None This restriction will require supervision in a future release. Available: iOS 4+ | iPadOS 4+ | macOS 15+ | tvOS 11.3+
- `ratingAppsExemptedBundleIDs` ([string]): If present, the system exempts apps with bundle IDs in the array from age-based rating restrictions. The system uses intersection combine rules to combine multiple payloads and any exceptions that parental control apps provide, including ScreenTime. Available: iOS 26.1+ | iPadOS 26.1+
- `ratingMovies` (integer): The maximum level of movie content allowed on the device. Support for this restriction on unsupervised devices is deprecated. Possible values, with the U.S. description of the rating level: - `1000`: All
- `500`: NC-17
- `400`: R
- `300`: PG-13
- `200`: PG
- `100`: G
- `0`: None Available: iOS 4+ | iPadOS 4+ | macOS 15+ | tvOS 11.3+
- `ratingRegion` (string): The two-letter key that profile tools use to display the proper ratings for the given region. The client doesn’t recognize or report this data. Available: iOS 4+ | iPadOS 4+ | macOS 10.7+ | tvOS 9+
Allowed for user enrollments: iOS | macOS
- `ratingTVShows` (integer): The maximum level of TV content allowed on the device. Support for this restriction on unsupervised devices is deprecated. Possible values, with the U.S. description of the rating level: - `1000`: All
- `600`: TV-MA
- `500`: TV-14
- `400`: TV-PG
- `300`: TV-G
- `200`: TV-Y7
- `100`: TV-Y
- `0`: None Available: iOS 4+ | iPadOS 4+ | macOS 15+ | tvOS 11.3+
- `requireManagedPasteboard` (boolean): If `true`, copy-and-paste functionality is limited by the `allowOpenFromManagedToUnmanaged` and `allowOpenFromUnmanagedToManaged` restrictions. Available: iOS 15+ | iPadOS 15+ | visionOS 2+
Allowed for user enrollments: iOS | visionOS
- `safariAcceptCookies` (number): Defines the conditions under which the device accepts cookies. The user-facing settings changed in iOS 11, although the possible values remain the same. Support for this restriction on unsupervised devices is deprecated. Allowed values: - `0`: Enables Prevent Cross-Site Tracking and Block All Cookies, and the user canʼt disable either setting.
- `1` or `1.5`: Enables Prevent Cross-Site Tracking, and the user canʼt disable it. Doesn’t enable Block All Cookies, but the user can enable it.
- `2`: Enables Prevent Cross-Site Tracking, but doesn’t enable Block All Cookies. The user can toggle either setting. Available: iOS 4+ | iPadOS 4+
- `safariAllowAutoFill` (boolean): If `false`, the system disables Safari AutoFill for passwords, contact info, and credit cards, and also prevents using the Keychain for AutoFill. Requires a supervised device in iOS 13 and later. > **Note**:  The system still allows third-party password managers, and apps can use AutoFill. Available: iOS 4+ | iPadOS 4+ | macOS 10.13+ | visionOS 2+
Requires supervision: iOS | visionOS
- `safariAllowJavaScript` (boolean): If `false`, Safari doesn’t execute JavaScript. This restriction will require supervision in a future release. Available: iOS 4+ | iPadOS 4+
- `safariAllowPopups` (boolean): If `false`, Safari doesn’t allow pop-up windows. Support for this restriction on unsupervised devices is deprecated. Available: iOS 4+ | iPadOS 4+
- `safariForceFraudWarning` (boolean): If `true`, the system enables Safari fraud warning. Available: iOS 4+ | iPadOS 4+
Allowed for user enrollments: iOS
- `whitelistedAppBundleIDs` ([string]): Deprecated: use the declarative management `com.apple.configuration.app.settings` configuration. Available: iOS 9.3+ | iPadOS 9.3+ | tvOS 11+
Deprecated: iOS 15+ | iPadOS 15+ | tvOS 15+
Requires supervision: iOS | tvOS


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/restrictions)*