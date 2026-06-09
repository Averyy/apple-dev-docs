# DeviceInformationCommand.Command

**Framework**: Device Management  
**Kind**: dictionary

The command to get detailed information about a device.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 4.0+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.1+
- watchOS 10.0+

## Declaration

```swift
object DeviceInformationCommand.Command
```

## Topics

### Objects
- [object DeviceInformationCommand.Command.Queries](deviceinformationcommand/command-data.dictionary/queries-data.dictionary.md)
  An array of query dictionaries to get information about a device.

## Properties

- `DeviceAttestationNonce` (data): A freshness code that appears in the resulting attestation. This value can contain up to 32 bytes of data. If specified, queries need to contain `DevicePropertiesAttestation`. The MDM server uses this value to prove that an attestation was recently generated. The system caches the most recently generated attestation on the device. If omitted or if the value matches the cached attestation, the system returns the cached attestation. To request a new attestation, provide a new freshness code. Requests for new attestations are rate limited. If it is fewer than 7 days since the system generated an attestation, the device returns the cached attestation rather than generating a new one. The hardware requirements for attestation are described below. Available: iOS 16+ | iPadOS 16+ | macOS 14+ | tvOS 16+ | visionOS 1.1+ | watchOS 10+
- `Queries` ([DeviceInformationCommand.Command.Queries]) *(required)*: An array of query dictionaries to get information about a device.
- `RequestRequiresNetworkTether` (boolean): If `true`, the device needs to be network-tethered to run the command.
- `RequestType` (string) *(required)*: The request type for this command.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/deviceinformationcommand/command-data.dictionary)*