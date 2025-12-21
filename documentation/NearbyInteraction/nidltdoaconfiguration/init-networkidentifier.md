# init(networkIdentifier:)

**Framework**: Nearby Interaction  
**Kind**: init

Initializes a Downlink Time-Difference-of-Arrival (DL-TDoA) configuration for a specific tracked area.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Declaration

```swift
init(networkIdentifier: Int)
```

## Parameters

- `networkIdentifier`: An ID that distinguishes among multiple tracked areas, if there’s more than one tracked area in the vicinity. Pass the value of the session ID in the DL-TDoA anchor’s configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/nearbyinteraction/nidltdoaconfiguration/init(networkidentifier:))*