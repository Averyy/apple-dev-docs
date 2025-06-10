# logoff(_:)

**Framework**: Network Extension  
**Kind**: method

Terminate the authentication session for a Hotspot network.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
class func logoff(_ network: NEHotspotNetwork) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the logoff command was successfully queued, [`false`](https://developer.apple.com/documentation/swift/false) otherwise.

#### Discussion

The application invokes this method when it wants to log off from the current network. Invoking this method causes an [`NEHotspotHelperCommand`](nehotspothelpercommand.md) of type [`NEHotspotHelperCommandType.logoff`](nehotspothelpercommandtype/logoff.md) to be issued to the application’s ‘handler’ block, which is registered with the system by calling `NEHotspotHelper registerWithOptions:queue:handler`.

The `network` parameter must correspond to the currently associated Wi-Fi network i.e. it must have come from the `network` property of the [`NEHotspotHelperCommand`](nehotspothelpercommand.md) or from the `supportedInterfaces` method.

> ⚠️ **Warning**:  The application must not actually log off from the network until it receives the command to log off.

## Parameters

- `network`: A   corresponding to the currently associated Wi-Fi network.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nehotspothelper/logoff(_:))*