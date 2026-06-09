# StatusScreenSharingConnectionGroupUnresolvedConnections

**Framework**: Device Management  
**Kind**: dictionary

The status item that lists connection groups with member connection references that the device couldn’t resolve.

**Availability**:
- macOS 14.1+

## Declaration

```swift
object StatusScreenSharingConnectionGroupUnresolvedConnections
```

#### Discussion

##### Status Item Availability

|  |  |
| --- | --- |
| Allowed in supervised enrollment | macOS |
| Allowed in device enrollment | N/A |
| Allowed in user enrollment | macOS |
| Allowed in local enrollment | macOS |
| Allowed in system scope | macOS |
| Allowed in user scope | macOS |

##### Status Item Example

**New or updated connection group**:

Reports a new or updated connection group.

```json
{
    "screensharing": {
        "connection": {
            "group": {
                "unresolved-connection": [
                    {
                        "identifier": "D4E5F6A7-B8C9-0123-DEFA-123456789012",
                        "unresolved_connections": [
                            "E5F6A7B8-C9D0-1234-EFAB-234567890123"
                        ]
                    }
                ]
            }
        }
    }
}
```

**Removed connection group**:

Reports a removed connection group.

```json
{
    "screensharing": {
        "connection": {
            "group": {
                "unresolved-connection": [
                    {
                        "identifier": "D4E5F6A7-B8C9-0123-DEFA-123456789012",
                        "_removed": true
                    }
                ]
            }
        }
    }
}
```

## Topics

### Objects
- [object StatusScreenSharingConnectionGroupUnresolvedConnectionsUnresolvedGroupObject](statusscreensharingconnectiongroupunresolvedconnectionsunresolvedgroupobject.md)
  The status item that contains an unresolved connection group.

## Properties

- `screensharing.connection.group.unresolved-connection` ([StatusScreenSharingConnectionGroupUnresolvedConnectionsUnresolvedGroupObject]) *(required)*: The status item that contains an array of unresolved connection groups.

## See Also

- [object StatusServicesBackgroundTask](statusservicesbackgroundtask.md)
  The status item that reports the device’s background task details.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/statusscreensharingconnectiongroupunresolvedconnections)*