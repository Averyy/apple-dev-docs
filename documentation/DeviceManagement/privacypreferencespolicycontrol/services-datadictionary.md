# PrivacyPreferencesPolicyControl.Services

**Framework**: Device Management  
**Kind**: dictionary

The privacy policy control services dictionary that controls access on a per app basis.

**Availability**:
- macOS 10.14+
- Device Assignment Services ?+
- VPP License Management ?+

## Declaration

```swift
object PrivacyPreferencesPolicyControl.Services
```

## Topics

### Objects
- [object PrivacyPreferencesPolicyControl.Services.Identity](privacypreferencespolicycontrol/services-data.dictionary/identity.md)
  A dictionary listing apps and the privacy policy to apply to them.

## Properties

- `Accessibility` ([PrivacyPreferencesPolicyControl.Services.Identity]): Specifies the policies for the app via the Accessibility subsystem. The ability to grant access by this profile is deprecated as of macOS 26.2, and will be removed in macOS 27.0.
- `AddressBook` ([PrivacyPreferencesPolicyControl.Services.Identity]): Specifies the policies for contact information managed by the Contacts.app.
- `AppleEvents` ([PrivacyPreferencesPolicyControl.Services.Identity]): Specifies the policies for the app sending restricted AppleEvents to another process.
- `BluetoothAlways` ([PrivacyPreferencesPolicyControl.Services.Identity]): Specifies the policies for the app to access Bluetooth devices.
- `Calendar` ([PrivacyPreferencesPolicyControl.Services.Identity]): Specifies the policies for calendar information managed by the Calendar.app.
- `Camera` ([PrivacyPreferencesPolicyControl.Services.Identity]): A system camera. Access to the camera can’t be given in a profile; it can only be denied.
- `FileProviderPresence` ([PrivacyPreferencesPolicyControl.Services.Identity]): Allows a File Provider application to know when the user is using files managed by the File Provider.
- `ListenEvent` ([PrivacyPreferencesPolicyControl.Services.Identity]): Allows the application to use CoreGraphics and HID APIs to listen to (receive) CGEvents and HID events from all processes. Access to these events can’t be given in a profile; it can only be denied.
- `MediaLibrary` ([PrivacyPreferencesPolicyControl.Services.Identity]): Allows the application to access Apple Music, music and video activity, and the media library.
- `Microphone` ([PrivacyPreferencesPolicyControl.Services.Identity]): A system microphone. Access to the microphone can’t be given in a profile; it can only be denied.
- `Photos` ([PrivacyPreferencesPolicyControl.Services.Identity]): The pictures managed by the Photos app in `~/Pictures/.photoslibrary`.
- `PostEvent` ([PrivacyPreferencesPolicyControl.Services.Identity]): Specifies the policies for the application to use CoreGraphics APIs to send CGEvents to the system event stream.
- `Reminders` ([PrivacyPreferencesPolicyControl.Services.Identity]): Specifies the policies for reminders information managed by the Reminders app.
- `ScreenCapture` ([PrivacyPreferencesPolicyControl.Services.Identity]): Allows the application to capture (read) the contents of the system display. Access to the contents can’t be given in a profile; it can only be denied.
- `SpeechRecognition` ([PrivacyPreferencesPolicyControl.Services.Identity]): Allows the application to use the system Speech Recognition facility and to send speech data to Apple.
- `SystemPolicyAllFiles` ([PrivacyPreferencesPolicyControl.Services.Identity]): Allows the application access to all protected files, including system administration files.
- `SystemPolicyAppBundles` ([PrivacyPreferencesPolicyControl.Services.Identity]): Allows the application to update or delete other apps. Available in macOS 13 and later.
- `SystemPolicyAppData` ([PrivacyPreferencesPolicyControl.Services.Identity]): Specifies the policies for the app to access the data of other apps.
- `SystemPolicyDesktopFolder` ([PrivacyPreferencesPolicyControl.Services.Identity]): Allows the application to access files in the user’s Desktop folder.
- `SystemPolicyDocumentsFolder` ([PrivacyPreferencesPolicyControl.Services.Identity]): Allows the application to access files in the user’s Documents folder.
- `SystemPolicyDownloadsFolder` ([PrivacyPreferencesPolicyControl.Services.Identity]): Allows the application to access files in the user’s Downloads folder.
- `SystemPolicyNetworkVolumes` ([PrivacyPreferencesPolicyControl.Services.Identity]): Allows the application to access files on network volumes.
- `SystemPolicyRemovableVolumes` ([PrivacyPreferencesPolicyControl.Services.Identity]): Allows the application to access files on removable volumes.
- `SystemPolicySysAdminFiles` ([PrivacyPreferencesPolicyControl.Services.Identity]): Allows the application access to some files used in system administration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/privacypreferencespolicycontrol/services-data.dictionary)*