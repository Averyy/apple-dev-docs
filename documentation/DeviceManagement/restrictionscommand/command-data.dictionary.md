# RestrictionsCommand.Command

**Framework**: Device Management  
**Kind**: dictionary  
**Role**: Device Management Command

The command to get a list of restrictions on the device.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 4.0+
- tvOS 9.0+
- visionOS 1.1+
- watchOS 10.0+

## Declaration

```
object RestrictionsCommand.Command
```

## Properties

- `ProfileRestrictions` (boolean): If `true`, the device reports restrictions from each profile.

  **Default**: `false`
- `RequestRequiresNetworkTether` (boolean): If `true`, the device needs to be network-tethered to run the command.

  **Default**: `false`
- `RequestType` (string) *(required)*: The request type for this command.

  **Allowed Values**: `Restrictions`


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/restrictionscommand/command-data.dictionary)*