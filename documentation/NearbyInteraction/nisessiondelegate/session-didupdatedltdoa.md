# session(_:didUpdateDLTDOA:)

**Framework**: Nearby Interaction  
**Kind**: method

Provides device ranging estimates for a Downlink Time-Difference-of-Arrival session.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Declaration

```swift
optional func session(_ session: NISession, didUpdateDLTDOA measurements: [NIDLTDOAMeasurement])
```

#### Discussion

The framework invokes this callback to provide measurements for sessions that run [`NIDLTDOAConfiguration`](nidltdoaconfiguration.md).

## Parameters

- `session`: The session that provides a Downlink Time-Difference-of-Arrival measurement.
- `measurements`: The measurement updates for the session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/nearbyinteraction/nisessiondelegate/session(_:didupdatedltdoa:))*