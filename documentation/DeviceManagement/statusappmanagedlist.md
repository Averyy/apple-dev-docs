# StatusAppManagedList

**Framework**: Device Management  
**Kind**: dictionary

The status item that lists the device’s declarative managed apps.

**Availability**:
- iOS 17.2+
- iPadOS 17.2+
- Mac Catalyst 17.2+
- macOS 26.0+
- visionOS 2.4+

## Declaration

```swift
object StatusAppManagedList
```

## Mentions

- [Installing, managing, updating, and removing apps](installing-managing-updating-and-removing-apps.md)
- [Processing status for managed apps](processing-status-for-managed-apps.md)
- [Transferring management of apps to declarative management](transferring-management-of-apps-to-declarative-management.md)
- [Implementing Platform SSO for unattended device enrollment](implementing-platform-sso-for-unattended-device-enrollment.md)

#### Discussion

##### Status Item Availability

|  |  |
| --- | --- |
| Allowed in supervised enrollment | iOS, macOS, Shared iPad, visionOS |
| Allowed in device enrollment | iOS, Shared iPad, visionOS |
| Allowed in user enrollment | iOS, macOS, Shared iPad, visionOS |
| Allowed in local enrollment | N/A |
| Allowed in system scope | iOS, macOS, Shared iPad, visionOS |
| Allowed in user scope | macOS |

##### Reason Codes

- `Error.AppStoreDisabled`: The App Store is disabled.
- `Error.DownloadFailed`: The app download failed. - `Timestamp`: (string) The RFC 3339 timestamp of the last download failure.
- `Error.DuplicateConfiguredApp`: The app is already being managed.
- `Error.InstallFailed`: The app install failed. - `Timestamp`: (string) The RFC 3339 timestamp of the last install failure.
- `Error.InvalidAppID`: The app id could not be found.
- `Error.InvalidCodeSignature`: The code signature of the app does not match the composed identifier, and the app cannot be managed.
- `Error.IsSystemApp`: The app is a system app that cannot be managed.
- `Error.LicenseNotFound`: A license for the app was not available.
- `Error.NotAnApp`: The downloaded data is not a valid app.
- `Error.NotSupported`: The app is not supported on this device.
- `Error.UnmanagedAppAlreadyInstalled`: An unmanaged app is already installed and cannot be managed.
- `Error.UserRejected`: The user rejected management of the app.
- `Info.UpdateAvailable`: An update is available for the app.
- `Error.UpdateFailed`: The app update failed. - `Timestamp`: (string) The RFC 3339 timestamp of the last update failure.

##### Status Item Example

**New or updated app**:

Reports a new or updated app.

```json
{
    "app": {
        "managed": {
            "list": [
                {
                    "identifier": "com.example.productivity",
                    "declaration-identifier": "com.example.app-management",
                    "name": "Productivity App",
                    "external-version-id": 845960,
                    "version": "5.2.1",
                    "short-version": "5.2.1",
                    "state": "managed"
                }
            ]
        }
    }
}
```

**Removed app**:

Reports a removed app.

```json
{
    "app": {
        "managed": {
            "list": [
                {
                    "identifier": "com.example.productivity",
                    "_removed": true
                }
            ]
        }
    }
}
```

## Topics

### Objects
- [object StatusAppManagedListAppObject](statusappmanagedlistappobject.md)
  A managed app.

## Properties

- `app.managed.list` ([StatusAppManagedListAppObject]) *(required)*: An array of dictionaries that describe the device’s declarative managed apps.

## See Also

- [object StatusMDMApp](statusmdmapp.md)
  The status item that lists the devices’s MDM-installed apps.
- [object StatusPackageList](statuspackagelist.md)
  The status item that lists the device’s declarative packages.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/statusappmanagedlist)*