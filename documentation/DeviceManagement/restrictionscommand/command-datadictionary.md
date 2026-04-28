# RestrictionsCommand.Command

**Framework**: Device Management  
**Kind**: dictionary

The command to get a list of restrictions on the device.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 4.0+
- tvOS 9.0+
- visionOS 1.1+
- watchOS 10.0+
- Device Assignment Services ?+
- VPP License Management ?+

## Declaration

```swift
object RestrictionsCommand.Command
```

## Properties

- `ProfileRestrictions` (boolean): If `true`, the device reports restrictions from each profile. This value is available in iOS 4 and later, and tvOS 6.1 and later.
- `RequestRequiresNetworkTether` (boolean): If `true`, the device needs to be network-tethered to run the command.
- `RequestType` (string) *(required)*: The request type for this command.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/restrictionscommand/command-data.dictionary)*