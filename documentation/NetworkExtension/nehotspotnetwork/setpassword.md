# setPassword(_:)

**Framework**: Network Extension  
**Kind**: method

Provide the password for a protected network.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
func setPassword(_ password: String)
```

#### Discussion

The Hotspot Helper may set a password for a protected network. The password string must adhere to IEEE 802.11 guidelines appropriate for the particular security scheme.

Hotspot Helper apps use this method only in the response to the [`NEHotspotHelperCommandType.filterScanList`](nehotspothelpercommandtype/filterscanlist.md) command.

## Parameters

- `password`: The network password.

## See Also

- [func setConfidence(NEHotspotHelperConfidence)](nehotspotnetwork/setconfidence(_:).md)
  Indicate the level of confidence in being able to handle the network.
- [enum NEHotspotHelperConfidence](nehotspothelperconfidence.md)
  A type that indicates the hotspot helper’s confidence in its ability to handle the network.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nehotspotnetwork/setpassword(_:))*