# rollingStartNumber

**Framework**: Exposure Notification  
**Kind**: property  
**Role**: Instance Property

A number that indicates when a key’s rolling period started.

**Availability**:
- iOS 12.5+ - Deprecated in 27.0
- iPadOS 12.5+ - Deprecated in 27.0
- Mac Catalyst 12.5+ - Deprecated in 27.0

> **Deprecated**: No longer supported.

## Declaration

```swift
var rollingStartNumber: ENIntervalNumber { get set }
```

```objc
@property (nonatomic, assign, readwrite) ENIntervalNumber rollingStartNumber;
```

## Discussion

> ❗ **Important**:  This property is available in iOS 12.5, and in iOS 13.5 and later.

## See Also

### Exposure Criteria
- [var transmissionRiskLevel: ENRiskLevel](./transmissionrisklevel.md)
  The risk of transmission associated with the person a key came from.
- [var rollingPeriod: ENIntervalNumber](./rollingperiod.md)
  The length of time that this key is valid.
- [var keyData: Data](./keydata.md)
  The temporary exposure key information.
- [typealias ENIntervalNumber](../enintervalnumber.md)
  A number assigned to each 10-minute window shared between all devices participating in the protocol.


---

*[View on Apple Developer](https://developer.apple.com/documentation/exposurenotification/entemporaryexposurekey/rollingstartnumber)*