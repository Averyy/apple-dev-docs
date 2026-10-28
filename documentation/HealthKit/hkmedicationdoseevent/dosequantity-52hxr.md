# doseQuantity

**Framework**: HealthKit  
**Kind**: property  
**Role**: Instance Property

The dose quantity the person reports as taken.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```objc
@property (nonatomic, copy, readonly, nullable) NSNumber * doseQuantity;
```

## Discussion

For scheduled dose events, the value defaults to the [`scheduledDoseQuantity`](./scheduleddosequantity-477ge.md), when logged from a reminder. For as needed dose events, the value defaults to `1` in the medication tracking experience, but can always be edited by the person logging.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkmedicationdoseevent/dosequantity-52hxr)*