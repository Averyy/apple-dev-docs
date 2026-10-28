# StatusMDMIsSharedIPad

**Framework**: Device Management  
**Kind**: dictionary  
**Role**: Object

The status item that reports the device’s Shared iPad state.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```
object StatusMDMIsSharedIPad
```

## Discussion

### Status item availability

|  |  |
| --- | --- |
| Allowed in supervised enrollment | iOS, Shared iPad |
| Allowed in device enrollment | iOS, Shared iPad |
| Allowed in user enrollment | iOS, Shared iPad |
| Allowed in local enrollment | N/A |
| Allowed in system scope | iOS, Shared iPad |
| Allowed in user scope | Shared iPad |

### Status item example

```json
{
    "mdm": {
        "is-shared-ipad": false
    }
}
```

## Properties

- `mdm.is-shared-ipad` (boolean) *(required)*: If `true`, the device is a Shared iPad.

## See Also

### MDM protocol items
- [object StatusMDMEnrollmentType](./statusmdmenrollmenttype.md)
  The status item that reports the device’s management enrollment type.
- [object StatusMDMIsAwaitingConfiguration](./statusmdmisawaitingconfiguration.md)
  The status item that reports the device management awaiting configuration state.
- [object StatusMDMIsReturnToService](./statusmdmisreturntoservice.md)
  The status item that reports the device’s return to service with app preservation state.
- [object StatusMDMPushMagic](./statusmdmpushmagic.md)
  The status item that reports the device’s push magic value.
- [object StatusMDMPushToken](./statusmdmpushtoken.md)
  The status item that reports the device’s push token.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/statusmdmissharedipad)*