# StatusPackageListStatusReasonObject

**Framework**: Device Management  
**Kind**: dictionary

Information about a status error.

**Availability**:
- macOS 26.0+

## Declaration

```swift
object StatusPackageListStatusReasonObject
```

## Topics

### Objects
- [object StatusPackageListStatusReason_DetailsObject](statuspackageliststatusreason_detailsobject.md)
  A dictionary that contains further details about this error.

## Properties

- `code` (string) *(required)*: A code for the state.
- `description` (string): A description of the state.
- `details` (StatusPackageListStatusReason_DetailsObject): A dictionary that contains additional details about the state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/statuspackageliststatusreasonobject)*