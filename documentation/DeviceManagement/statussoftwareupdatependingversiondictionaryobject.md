# StatusSoftwareUpdatePendingVersionDictionaryObject

**Framework**: Device Management  
**Kind**: dictionary

A dictionary that contains details about a pending software update.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- macOS 14.0+
- tvOS 18.4+
- visionOS 26.0+

## Declaration

```swift
object StatusSoftwareUpdatePendingVersionDictionaryObject
```

## Properties

- `build-version` (string) *(required)*: The build version of the pending software update, including any Background Security Improvement version. This string is empty if no update is pending.
- `os-version` (string) *(required)*: The OS version of the pending software update, including any Background Security Improvement version. This string is empty if no update is pending.
- `target-local-date-time` (string): The local date time value that indicates when the pending software update will be installed. This key is only present when the pending software update is being enforced.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/statussoftwareupdatependingversiondictionaryobject)*