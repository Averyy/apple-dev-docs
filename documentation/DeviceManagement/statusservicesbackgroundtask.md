# StatusServicesBackgroundTask

**Framework**: Device Management  
**Kind**: dictionary

The status item that reports the device’s background task details.

**Availability**:
- macOS 14.0+

## Declaration

```swift
object StatusServicesBackgroundTask
```

#### Discussion

##### Status Item Availability

|  |  |
| --- | --- |
| Allowed in supervised enrollment | macOS |
| Allowed in device enrollment | N/A |
| Allowed in user enrollment | N/A |
| Allowed in local enrollment | macOS |
| Allowed in system scope | macOS |
| Allowed in user scope | N/A |

##### Status Item Example

**New or updated task**:

Reports a new or updated background task.

```json
{
    "services": {
        "background-task": [
            {
                "identifier": "A1B2C3D4-E5F6-7890-ABCD-EF1234567890",
                "uid": 501,
                "path": "/Library/LaunchDaemons/com.example.daemon.plist",
                "state": "enabled",
                "type": "daemon",
                "launchd": {
                    "label": "com.example.daemon",
                    "program": "/usr/local/bin/example-daemon",
                    "program-arguments": [
                        "/usr/local/bin/example-daemon",
                        "--config",
                        "/etc/example/config.json"
                    ],
                    "checksum": "a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6"
                }
            }
        ]
    }
}
```

**Removed task**:

Reports a removed background task.

```json
{
    "services": {
        "background-task": [
            {
                "identifier": "A1B2C3D4-E5F6-7890-ABCD-EF1234567890",
                "_removed": true
            }
        ]
    }
}
```

## Topics

### Objects
- [object StatusServicesBackgroundTaskBackgroundTaskObject](statusservicesbackgroundtaskbackgroundtaskobject.md)
  The status item that reports a background task.

## Properties

- `services.background-task` ([StatusServicesBackgroundTaskBackgroundTaskObject]) *(required)*: The background task.

## See Also

- [object StatusScreenSharingConnectionGroupUnresolvedConnections](statusscreensharingconnectiongroupunresolvedconnections.md)
  The status item that lists connection groups with member connection references that the device couldn’t resolve.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/statusservicesbackgroundtask)*