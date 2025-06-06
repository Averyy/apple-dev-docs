# rollingPeriod

**Framework**: Exposure Notification  
**Kind**: property

The length of time that this key is valid.

**Availability**:
- iOS 12.5+
- iPadOS 12.5+
- Mac Catalyst 12.5+

## Declaration

```swift
var rollingPeriod: ENIntervalNumber { get set }
```

#### Discussion

> ❗ **Important**:  This property is available in iOS 12.5, and in iOS 13.5 and later.

 This property is available in iOS 12.5, and in iOS 13.5 and later.

The value of this property is the number of 10-minute windows between key rolling.

## See Also

- [var transmissionRiskLevel: ENRiskLevel](entemporaryexposurekey/transmissionrisklevel.md)
  The risk of transmission associated with the person a key came from.
- [var keyData: Data](entemporaryexposurekey/keydata.md)
  The temporary exposure key information.
- [var rollingStartNumber: ENIntervalNumber](entemporaryexposurekey/rollingstartnumber.md)
  A number that indicates when a key’s rolling period started.
- [typealias ENIntervalNumber](enintervalnumber.md)
  A number assigned to each 10-minute window shared between all devices participating in the protocol.


---

*[View on Apple Developer](https://developer.apple.com/documentation/exposurenotification/entemporaryexposurekey/rollingperiod)*