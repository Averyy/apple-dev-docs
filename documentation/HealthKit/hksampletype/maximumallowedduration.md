# maximumAllowedDuration

**Framework**: HealthKit  
**Kind**: property

The maximum duration if the sample type has a restricted duration.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
var maximumAllowedDuration: TimeInterval { get }
```

#### Return Value

The maximum time interval between the sample’s [`startDate`](hksample/startdate.md) and [`endDate`](hksample/enddate.md) properties.

#### Discussion

This method throws an exception if [`isMaximumDurationRestricted`](hksampletype/ismaximumdurationrestricted.md) is [`false`](https://developer.apple.com/documentation/swift/false).

## See Also

- [var isMinimumDurationRestricted: Bool](hksampletype/isminimumdurationrestricted.md)
  A Boolean value that indicates whether samples of this type have a minimum time interval between the start and end dates.
- [var minimumAllowedDuration: TimeInterval](hksampletype/minimumallowedduration.md)
  The minimum duration if the sample type has a restricted duration.
- [var isMaximumDurationRestricted: Bool](hksampletype/ismaximumdurationrestricted.md)
  A Boolean value that indicates whether samples of this type have a maximum time interval between the start and end dates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hksampletype/maximumallowedduration)*