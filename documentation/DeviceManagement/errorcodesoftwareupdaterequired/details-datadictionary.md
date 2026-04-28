# ErrorCodeSoftwareUpdateRequired.Details

**Framework**: Device Management  
**Kind**: dictionary

A dictionary that contains additional data about the software update required error code.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 26.0+
- Device Assignment Services ?+
- VPP License Management ?+

## Declaration

```swift
object ErrorCodeSoftwareUpdateRequired.Details
```

## Topics

### Objects
- [object ErrorCodeSoftwareUpdateRequired.Details.RequireBetaProgram](errorcodesoftwareupdaterequired/details-data.dictionary/requirebetaprogram-data.dictionary.md)
  A dictionary containing details of the beta program.

## Properties

- `BuildVersion` (string): The build version that the device needs to update to, for example, “20A242. The systems uses the build version for testing during seeding periods. This identifier can include a supplemental version identifier, for example, “20A242a”. If the `BuildVersion` isn’t consistent with the `OSVersion`, `OSVersion` take precedence.
- `OSVersion` (string) *(required)*: The OS version that the device needs to update to, for example, “16.1”. This identifier can include a supplemental version identifier, for example, “16.1 (a)”.
- `RequireBetaProgram` (ErrorCodeSoftwareUpdateRequired.Details.RequireBetaProgram): The device enrolls in the beta program, allowing enforced software updates to beta program OS versions. The device remains in the beta program after the system completes the enforced software update.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/errorcodesoftwareupdaterequired/details-data.dictionary)*