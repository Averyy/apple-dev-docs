# ErrorCodeSoftwareUpdateRequired.Details.RequireBetaProgram

**Framework**: Device Management  
**Kind**: dictionary

A dictionary containing details of the beta program.

**Availability**:
- iOS 17.5+
- iPadOS 17.5+
- Mac Catalyst 17.5+
- macOS 14.5+
- visionOS 26.0+

## Declaration

```swift
object ErrorCodeSoftwareUpdateRequired.Details.RequireBetaProgram
```

## Properties

- `Description` (string) *(required)*: A human readable description of the beta program.
- `Token` (string) *(required)*: The AxM seeding service token for the AxM organization the MDM server is part of. The system uses this token to enroll the device in the corresponding beta program.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/errorcodesoftwareupdaterequired/details-data.dictionary/requirebetaprogram-data.dictionary)*