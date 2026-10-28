# startDate

**Framework**: Core Motion  
**Kind**: property  
**Role**: Instance Property

The start time for the pedometer data.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- watchOS 2.0+

## Declaration

```swift
var startDate: Date { get }
```

```objc
@property (nonatomic, readonly) NSDate * startDate;
```

## Discussion

The `startDate` and [`endDate`](./enddate.md) represent the period of time over which the pedometer data was gathered.

## See Also

### Getting the Dates
- [var endDate: Date](./enddate.md)
  The end time for the pedometer data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmpedometerdata/startdate)*