# ScheduleOSUpdateCommand.Command.UpdatesItem

**Framework**: Device Management  
**Kind**: dictionary

A dictionary that describes the available operating-system updates item.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- macOS 10.11+
- tvOS 12.0+

## Declaration

```swift
object ScheduleOSUpdateCommand.Command.UpdatesItem
```

## Properties

- `InstallAction` (string) *(required)*: The install action, which is one of the following values: - **`Default`**: Download or install the update, depending on the current state. You can check the `UpdateResults` dictionary to review scheduled updates. This value is available in iOS 9 and later, macOS 10.11 and later, and tvOS 12 and later.
- **`DownloadOnly`**: Download the software update without installing it. This value is available in iOS 9 and later, macOS 11 and later, and tvOS 12 and later.
- **`InstallASAP`**: In iOS and tvOS, install a previously downloaded software update. In macOS, download the software update and trigger the restart countdown notification. This value is available in iOS 9 and later, macOS 10.11 and later, and tvOS 12 and later.
- **`NotifyOnly`**: Download the software update and notify the user through the App Store. This value is available in macOS 10.11 and later.
- **`InstallLater`**: Download the software update and install it at a later time. This value is available in macOS 10.11 and later.
- **`InstallForceRestart`**: Perform the `Default` action, and then force a restart if the update requires it. This value is available in macOS 11 and later. > ⚠️ **Warning**:  `InstallForceRestart` may result in data loss.
- `MaxUserDeferrals` (integer): The maximum number of times the system allows the user to postpone an update before it’s installed. The system prompts the user once a day. This key is only supported when `InstallAction` is `InstallLater` and only supported for minor OS updates (for example, macOS 12.x to 12.y).
- `Priority` (string): The scheduling priority for downloading and preparing the requested update. This is only supported for minor OS updates (macOS 12.x to 12.y). Available in macOS 12.3 and later. Prior versions of macOS used a priority of `Low`.
- `ProductKey` (string): The product key that represents the update.
- `ProductVersion` (string): The version of the update, which the system requires if `ProductKey` isn’t present. This value is available in iOS 11.3 and later, macOS 12 and later, and tvOS 12.2 and later. > **Note**:  This value isn’t available for use with Background Security Improvement updates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/scheduleosupdatecommand/command-data.dictionary/updatesitem)*