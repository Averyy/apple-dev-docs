# SoftwareUpdateSettingsBeta_RequireProgramObject

**Framework**: Device Management  
**Kind**: dictionary

The object that configures beta program requirement settings.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- macOS 15.4+

## Declaration

```swift
object SoftwareUpdateSettingsBeta_RequireProgramObject
```

## Properties

- `Description` (string) *(required)*: A human readable description of the beta program.
- `Token` (string) *(required)*: The Apple Business Manager or Apple School Manager seeding service token for the organization the MDM server is part of. The system uses this token to enroll the device in the corresponding beta program.

## See Also

- [object SoftwareUpdateSettingsBeta_ProgramObject](softwareupdatesettingsbeta_programobject.md)
  The object that configures a specific beta program.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/softwareupdatesettingsbeta_requireprogramobject)*