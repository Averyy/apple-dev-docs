# minimumAllowedDuration

**Framework**: HealthKit  
**Kind**: property  
**Role**: Instance Property

The minimum duration if the sample type has a restricted duration.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
var minimumAllowedDuration: TimeInterval { get }
```

```objc
@property (nonatomic, readonly) NSTimeInterval minimumAllowedDuration;
```

#### Return Value

The minimum time interval between the sample’s [`startDate`](../hksample/startdate.md) and [`endDate`](../hksample/enddate.md) properties.

#### Discussion

This method throws an exception if [`isMinimumDurationRestricted`](./isminimumdurationrestricted.md) is [`false`](../../Swift/false.md).

## See Also

### Checking the Duration Restriction
- [var isMinimumDurationRestricted: Bool](./isminimumdurationrestricted.md)
  A Boolean value that indicates whether samples of this type have a minimum time interval between the start and end dates.
- [var isMaximumDurationRestricted: Bool](./ismaximumdurationrestricted.md)
  A Boolean value that indicates whether samples of this type have a maximum time interval between the start and end dates.
- [var maximumAllowedDuration: TimeInterval](./maximumallowedduration.md)
  The maximum duration if the sample type has a restricted duration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hksampletype/minimumallowedduration)*