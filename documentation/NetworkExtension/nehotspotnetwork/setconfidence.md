# setConfidence(_:)

**Framework**: Network Extension  
**Kind**: method

Indicate the level of confidence in being able to handle the network.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
func setConfidence(_ confidence: NEHotspotHelperConfidence)
```

#### Discussion

Hotspot Helper apps use this method in the response to the [`NEHotspotHelperCommandType.evaluate`](nehotspothelpercommandtype/evaluate.md) and [`NEHotspotHelperCommandType.filterScanList`](nehotspothelpercommandtype/filterscanlist.md) commands.

## Parameters

- `confidence`: The level of confidence that the caller has in being able to help the system connect to this network.

## See Also

- [enum NEHotspotHelperConfidence](nehotspothelperconfidence.md)
  A type that indicates the hotspot helper’s confidence in its ability to handle the network.
- [func setPassword(String)](nehotspotnetwork/setpassword(_:).md)
  Provide the password for a protected network.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nehotspotnetwork/setconfidence(_:))*