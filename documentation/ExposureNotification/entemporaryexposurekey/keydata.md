# keyData

**Framework**: Exposure Notification  
**Kind**: property  
**Role**: Instance Property

The temporary exposure key information.

**Availability**:
- iOS 12.5+ - Deprecated in 27.0
- iPadOS 12.5+ - Deprecated in 27.0
- Mac Catalyst 12.5+ - Deprecated in 27.0

> **Deprecated**: No longer supported.

## Declaration

```swift
var keyData: Data { get set }
```

```objc
@property (nonatomic, copy, readwrite) NSData * keyData;
```

#### Discussion

> ❗ **Important**:  This property is available in iOS 12.5, and in iOS 13.5 and later.

## See Also

### Exposure Criteria
- [var transmissionRiskLevel: ENRiskLevel](./transmissionrisklevel.md)
  The risk of transmission associated with the person a key came from.
- [var rollingPeriod: ENIntervalNumber](./rollingperiod.md)
  The length of time that this key is valid.
- [var rollingStartNumber: ENIntervalNumber](./rollingstartnumber.md)
  A number that indicates when a key’s rolling period started.
- [typealias ENIntervalNumber](../enintervalnumber.md)
  A number assigned to each 10-minute window shared between all devices participating in the protocol.


---

*[View on Apple Developer](https://developer.apple.com/documentation/exposurenotification/entemporaryexposurekey/keydata)*