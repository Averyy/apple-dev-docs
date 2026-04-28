# ValidateApplicationsCommand.Command

**Framework**: Device Management  
**Kind**: dictionary

The command to force validation of developer and universal provisioning profiles for enterprise apps.

**Availability**:
- iOS 9.2+
- iPadOS 9.2+
- Mac Catalyst 9.2+
- tvOS 10.2+
- visionOS 1.1+
- Device Assignment Services ?+
- VPP License Management ?+

## Declaration

```swift
object ValidateApplicationsCommand.Command
```

## Properties

- `Identifiers` ([string]): The bundle identifiers of the enterprise apps to include for validation of associated provisioning profiles, if you choose to provide them. Otherwise, validation occurs for the provisioning profiles for the installed managed apps.
- `RequestRequiresNetworkTether` (boolean): If `true`, the device needs to be network-tethered to run the command.
- `RequestType` (string) *(required)*: The request type for this command.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/validateapplicationscommand/command-data.dictionary)*