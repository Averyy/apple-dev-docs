# StatusSoftwareUpdateInstallReasonDictionaryObject

**Framework**: Device Management  
**Kind**: dictionary

Details about the reason for a pending software update.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 18.4+
- visionOS 26.0+

## Declaration

```swift
object StatusSoftwareUpdateInstallReasonDictionaryObject
```

## Properties

- `declaration-id` (string): The identifier of the declaration that caused the software update to occur. This key is present only if the `reason` array contains the `declaration` value.
- `reason` ([string]) *(required)*: A list of reasons for the pending software update. An empty list indicates that no software update is pending.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/statussoftwareupdateinstallreasondictionaryobject)*