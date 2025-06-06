# NEHotspotHelperResult

**Framework**: Network Extension  
**Kind**: enum

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
enum NEHotspotHelperResult
```

## Topics

### Results
- [NEHotspotHelperResult.success](nehotspothelperresult/success.md)
  The command was handled successfully.
- [NEHotspotHelperResult.failure](nehotspothelperresult/failure.md)
  The command failed to be handled.
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
### Initializers
- [init?(rawValue: Int)](nehotspothelperresult/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [func createResponse(NEHotspotHelperResult) -> NEHotspotHelperResponse](nehotspothelpercommand/createresponse(_:).md)
  Create a response to the command.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nehotspothelperresult)*