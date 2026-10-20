# endDate

**Framework**: Core Motion  
**Kind**: property  
**Role**: Instance Property

The result’s end time and date.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- watchOS 5.0+

## Declaration

```swift
var endDate: Date { get }
```

```objc
@property (nonatomic, copy, readonly) NSDate * endDate;
```

#### Discussion

The result’s `endDate` is always one minute or less after the [`startDate`](./startdate.md).

## See Also

### Reading the Time Interval
- [var startDate: Date](./startdate.md)
  The result’s start time and date.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmdyskineticsymptomresult/enddate)*