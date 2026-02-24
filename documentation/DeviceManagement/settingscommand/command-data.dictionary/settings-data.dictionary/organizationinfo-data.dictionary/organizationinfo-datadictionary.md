# SettingsCommand.Command.Settings.OrganizationInfo.OrganizationInfo

**Framework**: Device Management  
**Kind**: dictionary

A dictionary that contains information about the organization operating the MDM server.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.1+
- watchOS 10.0+

## Declaration

```swift
object SettingsCommand.Command.Settings.OrganizationInfo.OrganizationInfo
```

## Properties

- `OrganizationAddress` (string): The organization’s address. Use the LF character (`&#10`) to insert line breaks.
- `OrganizationEmail` (string): The organization’s support email address.
- `OrganizationMagic` (string): A unique identifier for the various services a single organization manages.
- `OrganizationName` (string) *(required)*: A string that describes the organization operating the MDM server for display to the user during certain operations, such as purchasing or installing apps.
- `OrganizationPhone` (string): The organization’s phone number.
- `OrganizationShortName` (string): A shorter version of `OrganizationName`, preferably a single word or abbreviation, suitable for display to the user in places where a very short name is necessary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/settingscommand/command-data.dictionary/settings-data.dictionary/organizationinfo-data.dictionary/organizationinfo-data.dictionary)*