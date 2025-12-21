# evaluatedSSIDs

**Framework**: Network Extension  
**Kind**: property

An array of pre-evaluated Wi-Fi SSID strings.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- visionOS 26.0+

## Declaration

```swift
final var evaluatedSSIDs: [String] { get set }
```

#### Discussion

The system doesn’t call [`NEHotspotEvaluationProvider`](nehotspotevaluationprovider.md) to evaluate any Wi-Fi network whose SSID is found in this array.

> **Note**: You can specify a maximum of two SSIDs for this property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nehotspotmanager/evaluatedssids)*