# StatusManagementDeclarations

**Framework**: Device Management  
**Kind**: dictionary

The status item that reports the device’s processed declarations.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.1+
- watchOS 10.0+

## Declaration

```swift
object StatusManagementDeclarations
```

## Mentions

- [Installing, managing, updating, and removing apps](installing-managing-updating-and-removing-apps.md)
- [Installing packages](installing-packages.md)

#### Discussion

The name of the declaration status item is `management.declarations`.

##### Status Item Availability

|  |  |
| --- | --- |
| Allowed in supervised enrollment | iOS, macOS, Shared iPad, tvOS, visionOS, watchOS |
| Allowed in device enrollment | iOS, Shared iPad, tvOS, visionOS |
| Allowed in user enrollment | iOS, macOS, Shared iPad, visionOS |
| Allowed in local enrollment | N/A |
| Allowed in system scope | iOS, macOS, Shared iPad, tvOS, visionOS, watchOS |
| Allowed in user scope | macOS, Shared iPad |

##### Status Item Example

```json
{
    "management": {
        "declarations": {
            "activations": [
                {
                    "identifier": "com.example.activation.main",
                    "server-token": "A1B2C3D4-E5F6-7890-ABCD-EF1234567890",
                    "active": true,
                    "valid": "valid"
                }
            ],
            "configurations": [
                {
                    "identifier": "com.example.config.passcode",
                    "server-token": "B2C3D4E5-F6A7-8901-BCDE-F01234567891",
                    "active": true,
                    "valid": "valid"
                }
            ],
            "assets": [],
            "management": []
        }
    }
}
```

## Topics

### Objects
- [object StatusManagementDeclarationsDeclarationsObject](statusmanagementdeclarationsdeclarationsobject.md)
  A collection of the client’s processed declarations.

## Properties

- `management.declarations` (StatusManagementDeclarationsDeclarationsObject) *(required)*: A collection of the client’s processed declarations.

## See Also

- [object StatusManagementClientCapabilities](statusmanagementclientcapabilities.md)
  The status item that reports the devices’s protocol capabilities.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/statusmanagementdeclarations)*