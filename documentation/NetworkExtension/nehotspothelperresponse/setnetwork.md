# setNetwork(_:)

**Framework**: Network Extension  
**Kind**: method

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

#### Discussion

In response to the [`NEHotspotHelperCommandType.evaluate`](nehotspothelpercommandtype/evaluate.md) command, the Hotspot Helper app sets the confidence level on the [`NEHotspotNetwork`](nehotspotnetwork.md) object provided with the command and calls this method to convey the confidence level to the system.

## Parameters

- `network`: The annotated   object. This must be the same object that was passed in the corresponding   object.

## See Also

- [func setNetworkList([NEHotspotNetwork])](nehotspothelperresponse/setnetworklist(_:).md)
  Set the list of handled networks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nehotspothelperresponse/setnetwork(_:))*