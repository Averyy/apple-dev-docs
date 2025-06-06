# ENIntervalNumber

**Framework**: Exposure Notification  
**Kind**: typealias

A number assigned to each 10-minute window shared between all devices participating in the protocol.

**Availability**:
- iOS 12.5+
- iPadOS 12.5+
- Mac Catalyst 12.5+

## Declaration

```swift
typealias ENIntervalNumber = UInt32
```

#### Discussion

These shared intervals of time derive from timestamps in UNIX Epoch Time.

`ENIntervalNumber(Timestamp) ← Timestamp / (60×10)`

## See Also

- [var transmissionRiskLevel: ENRiskLevel](entemporaryexposurekey/transmissionrisklevel.md)
  The risk of transmission associated with the person a key came from.
- [var rollingPeriod: ENIntervalNumber](entemporaryexposurekey/rollingperiod.md)
  The length of time that this key is valid.
- [var keyData: Data](entemporaryexposurekey/keydata.md)
  The temporary exposure key information.
- [var rollingStartNumber: ENIntervalNumber](entemporaryexposurekey/rollingstartnumber.md)
  A number that indicates when a key’s rolling period started.


---

*[View on Apple Developer](https://developer.apple.com/documentation/exposurenotification/enintervalnumber)*