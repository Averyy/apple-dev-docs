# StatusAppManagedListStatusReasonObject

**Framework**: Device Management  
**Kind**: dictionary

Information about a status error.

**Availability**:
- iOS 17.2+
- iPadOS 17.2+
- Mac Catalyst 17.2+
- macOS 26.0+
- visionOS 2.4+

## Declaration

```swift
object StatusAppManagedListStatusReasonObject
```

## Topics

### Objects
- [object StatusAppManagedListStatusReason_DetailsObject](statusappmanagedliststatusreason_detailsobject.md)
  A dictionary that contains additional details about the state.

## Properties

- `code` (string) *(required)*: A code for the state.
- `description` (string): A description of the state.
- `details` (StatusAppManagedListStatusReason_DetailsObject): A dictionary that contains additional details about the state.

## See Also

- [object StatusAppManagedListManagedConfigurationObject](statusappmanagedlistmanagedconfigurationobject.md)
  The status of app or extension managed configurations. This key is only present when managed configurations are available for the managed app or any of its extensions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/statusappmanagedliststatusreasonobject)*