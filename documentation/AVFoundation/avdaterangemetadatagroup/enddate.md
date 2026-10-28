# endDate

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The end date for the metadata date range group.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var endDate: Date? { get }
```

```objc
@property (nonatomic, copy, readonly, nullable) NSDate * endDate;
```

## Discussion

The `endDate` defines the ending date on the timeline for which the associated metadata is valid.

## See Also

### Accessing the date range
- [var startDate: Date](./startdate.md)
  The start date for the metadata date range group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avdaterangemetadatagroup/enddate)*