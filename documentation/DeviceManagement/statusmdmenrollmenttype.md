# StatusMDMEnrollmentType

**Framework**: Device Management  
**Kind**: dictionary  
**Role**: Object

The status item that reports the device’s management enrollment type.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```
object StatusMDMEnrollmentType
```

## Discussion

### Status item availability

|  |  |
| --- | --- |
| Allowed in supervised enrollment | iOS, macOS, Shared iPad, tvOS, visionOS, watchOS |
| Allowed in device enrollment | iOS, Shared iPad, tvOS, visionOS |
| Allowed in user enrollment | iOS, macOS, Shared iPad, visionOS |
| Allowed in local enrollment | N/A |
| Allowed in system scope | iOS, macOS, Shared iPad, tvOS, visionOS, watchOS |
| Allowed in user scope | macOS, Shared iPad |

### Status item example

```json
{
    "mdm": {
        "enrollment-type": "supervised"
    }
}
```

## Properties

- `mdm.enrollment-type` (string) *(required)*: The device management enrollment type that indicates how the device is enrolled, which has the following possible values:

  - `none`: Device isn’t enrolled
  - `supervised`: Device is supervised
  - `device`: Device enrollment
  - `user`: User enrollment

  **Allowed Values**: `none`, `supervised`, `device`, `user`

## See Also

### MDM protocol items
- [object StatusMDMIsAwaitingConfiguration](./statusmdmisawaitingconfiguration.md)
  The status item that reports the device management awaiting configuration state.
- [object StatusMDMIsReturnToService](./statusmdmisreturntoservice.md)
  The status item that reports the device’s return to service with app preservation state.
- [object StatusMDMIsSharedIPad](./statusmdmissharedipad.md)
  The status item that reports the device’s Shared iPad state.
- [object StatusMDMPushMagic](./statusmdmpushmagic.md)
  The status item that reports the device’s push magic value.
- [object StatusMDMPushToken](./statusmdmpushtoken.md)
  The status item that reports the device’s push token.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/statusmdmenrollmenttype)*