# StatusManagementDeclarationsDeclarationObject

**Framework**: Device Management  
**Kind**: dictionary

Status for a declaration processed by the client.

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
object StatusManagementDeclarationsDeclarationObject
```

## Topics

### Objects
- [object StatusManagementDeclarationsStatusReasonObject](statusmanagementdeclarationsstatusreasonobject.md)
  Information about a status error.

## Properties

- `active` (boolean) *(required)*: If `true`, the declaration is active on the device.
- `identifier` (string) *(required)*: The `identifier` of the declaration this status report refers to.
- `reasons` ([StatusManagementDeclarationsStatusReasonObject]): The details of any client errors.
- `server-token` (string) *(required)*: The `ServerToken` of the declaration this status report refers to.
- `valid` (string) *(required)*: This string defines the validity of the declaration. If it’s `invalid`, the `reasons` property contains more details.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/statusmanagementdeclarationsdeclarationobject)*