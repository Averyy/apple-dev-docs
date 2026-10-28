# NSPrivacyAccessedAPITypeReasons

**Framework**: Bundle Resources  
**Kind**: typealias  
**Role**: Property List Key

An array of strings that identifies the reasons your app or third-party SDK uses required reason API.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 14.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Details

- **Name**: `NSPrivacyAccessedAPITypeReasons` (Privacy Accessed API Reasons)
- **Type**: array of string 

## Possible Values

- `DDA9.1`: Declare this reason to display file timestamps to the person using the device. Information accessed for this reason, or any derived information, may not be sent off-device.
- `C617.1`: Declare this reason to access the timestamps, size, or other metadata of files inside the app container, app group container, or the app’s CloudKit container.
- `3B52.1`: Declare this reason to access the timestamps, size, or other metadata of files or directories that the user specifically granted access to, such as using a document picker view controller.
- `0A2A.1`: Declare this reason if your third-party SDK is providing a wrapper function around file timestamp API(s) for the app to use, and you only access the file timestamp APIs when the app calls your wrapper function. This reason may only be declared by third-party SDKs. This reason may not be declared if your third-party SDK was created primarily to wrap required reason API(s).

  Information accessed for this reason, or any derived information, may not be used for your third-party SDK’s own purposes or sent off-device by your third-party SDK.
- `35F9.1`: Declare this reason to access the system boot time in order to measure the amount of time that has elapsed between events that occurred within the app or to perform calculations to enable timers.

  Information accessed for this reason, or any derived information, may not be sent off-device. There is an exception for information about the amount of time that has elapsed between events that occurred within the app, which may be sent off-device.
- `8FFB.1`: Declare this reason to access the system boot time to calculate absolute timestamps for events that occurred within your app, such as events related to the [UIKit](../../../UIKit/UIKit.md) or [AVFAudio](../../../AVFAudio/AVFAudio.md) frameworks.

  Absolute timestamps for events that occurred within your app may be sent off-device. System boot time accessed for this reason, or any other information derived from system boot time, may not be sent off-device.
- `3D61.1`: Declare this reason to include system boot time information in an optional bug report that the person using the device chooses to submit. The system boot time information must be prominently displayed to the person as part of the report.
- `85F4.1`: Declare this reason to display disk space information to the person using the device. Disk space may be displayed in units of information (such as bytes) or units of time combined with a media type (such as minutes of HD video).

  Information accessed for this reason, or any derived information, may not be sent off-device. There is an exception that allows the app to send disk space information over the local network to another device operated by the same person only for the purpose of displaying disk space information on that device; this exception only applies if the user has provided explicit permission to send disk space information, and the information may not be sent over the Internet.
- `E174.1`: Declare this reason to check whether there is sufficient disk space to write files, or to check whether the disk space is low so that the app can delete files when the disk space is low. The app must behave differently based on disk space in a way that is observable to users.

  Information accessed for this reason, or any derived information, may not be sent off-device. There is an exception that allows the app to avoid downloading files from a server when disk space is insufficient.
- `7D9E.1`: Declare this reason to include disk space information in an optional bug report that the person using the device chooses to submit. The disk space information must be prominently displayed to the person as part of the report.

  Information accessed for this reason, or any derived information, may be sent off-device only after the user affirmatively chooses to submit the specific bug report including disk space information, and only for the purpose of investigating or responding to the bug report.
- `B728.1`: Declare this reason if your app is a health research app, and you access this API category to detect and inform research participants about low disk space impacting the research data collection.

  Your app must comply with [App Store Review Guideline §5.1.3](https://developer.apple.com/app-store/review/guidelines/#health-and-health-research). Your app must not offer any functionality other than providing information about and allowing people to participate in health research.
- `3EC4.1`: Declare this reason if your app is a custom keyboard app, and you access this API category to determine the keyboards that are active on the device. Providing a systemwide custom keyboard to the user must be the primary functionality of the app.

  Information accessed for this reason, or any derived information, may not be sent off-device.
- `54BD.1`: Declare this reason to access active keyboard information to present the correct customized user interface to the person using the device. The app must have text fields for entering or editing text and must behave differently based on active keyboards in a way that is observable to users.

  Information accessed for this reason, or any derived information, may not be sent off-device.
- `CA92.1`: Declare this reason to access user defaults to read and write information that is only accessible to the app itself.

  This reason does not permit reading information that was written by other apps or the system, or writing information that can be accessed by other apps.
- `1C8F.1`: Declare this reason to access user defaults to read and write information that is only accessible to the apps, app extensions, and App Clips that are members of the same App Group as the app itself.

  This reason does not permit reading information that was written by apps, app extensions, or App Clips outside the same App Group or by the system. Your app is not responsible if the system provides information from the global domain because a key is not present in your requested domain while your app is attempting to read information that apps, app extensions, or App Clips in your app’s App Group write.

  This reason also does not permit writing information that can be accessed by apps, app extensions, or App Clips outside the same App Group.
- `C56D.1`: Declare this reason if your third-party SDK is providing a wrapper function around user defaults API(s) for the app to use, and you only access the user defaults APIs when the app calls your wrapper function. This reason may only be declared by third-party SDKs. This reason may not be declared if your third-party SDK was created primarily to wrap required reason API(s).

  Information accessed for this reason, or any derived information, may not be used for your third-party SDK’s own purposes or sent off-device by your third-party SDK.
- `AC6B.1`: Declare this reason to access user defaults to read the `com.apple.configuration.managed` key to retrieve the managed app configuration set by MDM, or to set the `com.apple.feedback.managed` key to store feedback information to be queried over MDM, as described in the Apple Mobile Device Management Protocol Reference documentation.

## Mentions

- [Describing use of required reason API](../../describing-use-of-required-reason-api.md)

## Discussion

For information on which reasons your app or third-party SDK declares for each category of required reasons API it uses, see [`NSPrivacyAccessedAPIType`](./nsprivacyaccessedapitype.md).

For information on required reason API, see [Describing use of required reason API](../../describing-use-of-required-reason-api.md).

## See Also

### Reporting privacy accessed API usage
- [NSPrivacyAccessedAPIType](./nsprivacyaccessedapitype.md)
  A string that describes a category of required reason API your app or third-party SDK uses.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/app-privacy-configuration/nsprivacyaccessedapitypes/nsprivacyaccessedapitypereasons)*