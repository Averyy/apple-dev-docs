# NEHotspotHelperResult.failure

**Framework**: Network Extension  
**Kind**: case

The command failed to be handled.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
case failure
```

## See Also

- [NEHotspotHelperResult.success](nehotspothelperresult/success.md)
  The command was handled successfully.
- [NEHotspotHelperResult.uiRequired](nehotspothelperresult/uirequired.md)
  The operation requires user interaction. This result is only valid in response to a command with type [`NEHotspotHelperCommandType.authenticate`](nehotspothelpercommandtype/authenticate.md).
- [NEHotspotHelperResult.commandNotRecognized](nehotspothelperresult/commandnotrecognized.md)
  The helper did not recognize the command type.
- [NEHotspotHelperResult.authenticationRequired](nehotspothelperresult/authenticationrequired.md)
  The network requires authentication again. This result is only valid in response to a command with type [`NEHotspotHelperCommandType.maintain`](nehotspothelpercommandtype/maintain.md).
- [NEHotspotHelperResult.unsupportedNetwork](nehotspothelperresult/unsupportednetwork.md)
  After attempting to authenticate, the Hotspot Helper app determined that it can’t perform the authentication. This result is only valid in response to commands of type [`NEHotspotHelperCommandType.authenticate`](nehotspothelpercommandtype/authenticate.md) and [`NEHotspotHelperCommandType.presentUI`](nehotspothelpercommandtype/presentui.md).
- [NEHotspotHelperResult.temporaryFailure](nehotspothelperresult/temporaryfailure.md)
  The Hotspot Helper app determined that it is temporarily unable to perform the authentication. This result is only valid in response to commands of type [`NEHotspotHelperCommandType.authenticate`](nehotspothelpercommandtype/authenticate.md) and [`NEHotspotHelperCommandType.presentUI`](nehotspothelpercommandtype/presentui.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nehotspothelperresult/failure)*