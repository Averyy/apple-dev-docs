# setNetworkList(_:)

**Framework**: Network Extension  
**Kind**: method

Set the list of handled networks.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
func setNetworkList(_ networkList: [NEHotspotNetwork])
```

#### Discussion

The Hotspot Helper app calls this method on its response to the [`NEHotspotHelperCommandType.filterScanList`](nehotspothelpercommandtype/filterscanlist.md). The helper provides the list of network objects that it is capable of handling with at least low confidence. Networks that it has no confidence in handling should not be specified.

## Parameters

- `networkList`: The list of networks that the caller is capable of handling.

## See Also

- [func setNetwork(NEHotspotNetwork)](nehotspothelperresponse/setnetwork(_:).md)
  Set the network that conveys the confidence level.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nehotspothelperresponse/setnetworklist(_:))*