# endDate

**Framework**: Core Motion  
**Kind**: property  
**Role**: Instance Property

The end time for the pedometer data.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- watchOS 2.0+

## Declaration

```swift
var endDate: Date { get }
```

```objc
@property (nonatomic, readonly) NSDate * endDate;
```

## Discussion

The [`startDate`](./startdate.md) and `endDate` represent the period of time over which the pedometer data was gathered.

## See Also

### Getting the Dates
- [var startDate: Date](./startdate.md)
  The start time for the pedometer data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmpedometerdata/enddate)*