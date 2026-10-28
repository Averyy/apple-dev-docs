# logoff(_:)

**Framework**: Network Extension  
**Kind**: method  
**Role**: Type Method

Terminate the authentication session for a Hotspot network.

**Availability**:
- iOS 9.0+ - Deprecated in 26.0
- iPadOS 9.0+ - Deprecated in 26.0
- Mac Catalyst 13.1+ - Deprecated in 26.0
- visionOS 1.0+ - Deprecated in 26.0

> **Deprecated**: Use NEHotspotManager API

## Declaration

```swift
class func logoff(_ network: NEHotspotNetwork) -> Bool
```

```objc
+ (BOOL) logoff:(NEHotspotNetwork *) network;
```

## Return Value

[`true`](../../Swift/true.md) if the logoff command was successfully queued, [`false`](../../Swift/false.md) otherwise.

## Discussion

The application invokes this method when it wants to log off from the current network. Invoking this method causes an [`NEHotspotHelperCommand`](../nehotspothelpercommand.md) of type [`NEHotspotHelperCommandType.logoff`](../nehotspothelpercommandtype/logoff.md) to be issued to the application’s ‘handler’ block, which is registered with the system by calling `NEHotspotHelper registerWithOptions:queue:handler`.

The `network` parameter must correspond to the currently associated Wi-Fi network i.e. it must have come from the `network` property of the [`NEHotspotHelperCommand`](../nehotspothelpercommand.md) or from the `supportedInterfaces` method.

> ⚠️ **Warning**:  The application must not actually log off from the network until it receives the command to log off.

## Parameters

- `network`: A [`NEHotspotNetwork`](../nehotspotnetwork.md) corresponding to the currently associated Wi-Fi network.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nehotspothelper/logoff(_:))*