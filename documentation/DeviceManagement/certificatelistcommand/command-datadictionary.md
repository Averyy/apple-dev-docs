# CertificateListCommand.Command

**Framework**: Device Management  
**Kind**: dictionary

The command to get a list of installed certificates on a device.

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
object CertificateListCommand.Command
```

## Properties

- `ManagedOnly` (boolean): If `true`, only include certificates that MDM installed or that are in the same profile as the MDM payload. User-enrolled devices ignore this value and always only include managed certificates. Available: iOS 13+ | iPadOS 13+ | macOS 10.15+ | tvOS 13+ | visionOS 1.1+ | watchOS 10+
- `RequestRequiresNetworkTether` (boolean): If `true`, the device needs to be network-tethered to run the command.
- `RequestType` (string) *(required)*: The request type for this command.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/certificatelistcommand/command-data.dictionary)*