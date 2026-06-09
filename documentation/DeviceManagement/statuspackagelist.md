# StatusPackageList

**Framework**: Device Management  
**Kind**: dictionary

The status item that lists the device’s declarative packages.

**Availability**:
- macOS 26.0+

## Declaration

```swift
object StatusPackageList
```

## Mentions

- [Installing packages](installing-packages.md)

#### Discussion

##### Status Item Availability

|  |  |
| --- | --- |
| Allowed in supervised enrollment | macOS |
| Allowed in device enrollment | N/A |
| Allowed in user enrollment | N/A |
| Allowed in local enrollment | N/A |
| Allowed in system scope | macOS |
| Allowed in user scope | N/A |

##### Reason Codes

- `Error.DownloadFailed`: The package download failed. - `Timestamp`: (string) The RFC 3339 timestamp of the last download failure.
- `Error.InstallFailed`: The package install failed. - `Timestamp`: (string) The RFC 3339 timestamp of the last install failure.

##### Status Item Example

**New or updated package**:

Reports a new or updated package.

```json
{
    "package": {
        "list": [
            {
                "identifier": "com.example.package.enterprise-tools",
                "declaration-identifier": "com.example.package-management",
                "name": "Enterprise Tools",
                "version": "2.1.0",
                "state": "installed"
            }
        ]
    }
}
```

**Removed package**:

Reports a removed package.

```json
{
    "package": {
        "list": [
            {
                "identifier": "com.example.package.enterprise-tools",
                "_removed": true
            }
        ]
    }
}
```

## Topics

### Objects
- [object StatusPackageListPackageObject](statuspackagelistpackageobject.md)
  A dictionary that describes a declarative package.

## Properties

- `package.list` ([StatusPackageListPackageObject]) *(required)*: An array of dictionaries that describe the device’s declarative packages.

## See Also

- [object StatusAppManagedList](statusappmanagedlist.md)
  The status item that lists the device’s declarative managed apps.
- [object StatusMDMApp](statusmdmapp.md)
  The status item that lists the devices’s MDM-installed apps.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/statuspackagelist)*