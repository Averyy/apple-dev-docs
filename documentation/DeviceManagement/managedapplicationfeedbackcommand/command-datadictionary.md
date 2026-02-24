# ManagedApplicationFeedbackCommand.Command

**Framework**: Device Management  
**Kind**: dictionary

The command to get app feedback from a managed app on the device.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- macOS 11.0+
- tvOS 10.2+
- visionOS 1.1+

## Declaration

```swift
object ManagedApplicationFeedbackCommand.Command
```

## Properties

- `DeleteFeedback` (boolean): If `true`, delete the app’s feedback dictionary after the server reads it. Apps that are managed by Declarative Device Management are ignored.
- `Identifiers` ([string]) *(required)*: The bundle identifiers of the managed apps.
- `RequestRequiresNetworkTether` (boolean): If `true`, the device needs to be network-tethered to run the command.
- `RequestType` (string) *(required)*: The request type for this command.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/managedapplicationfeedbackcommand/command-data.dictionary)*