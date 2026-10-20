# setNetwork(_:)

**Framework**: Network Extension  
**Kind**: method  
**Role**: Instance Method

Set the network that conveys the confidence level.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
func setNetwork(_ network: NEHotspotNetwork)
```

```objc
- (void) setNetwork:(NEHotspotNetwork *) network;
```

#### Discussion

In response to the [`NEHotspotHelperCommandType.evaluate`](../nehotspothelpercommandtype/evaluate.md) command, the Hotspot Helper app sets the confidence level on the [`NEHotspotNetwork`](../nehotspotnetwork.md) object provided with the command and calls this method to convey the confidence level to the system.

## Parameters

- `network`: The annotated [`NEHotspotNetwork`](../nehotspotnetwork.md) object. This must be the same object that was passed in the corresponding [`NEHotspotHelperCommand`](../nehotspothelpercommand.md) object.

## See Also

### Response properties
- [func setNetworkList([NEHotspotNetwork])](./setnetworklist%28_%29.md)
  Set the list of handled networks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nehotspothelperresponse/setnetwork(_:))*