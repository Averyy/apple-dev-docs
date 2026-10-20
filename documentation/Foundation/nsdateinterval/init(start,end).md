# init(start:end:)

**Framework**: Foundation  
**Kind**: init  
**Role**: Initializer

Initializes a date interval from a given start date and end date.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
convenience init(start startDate: Date, end endDate: Date)
```

```objc
- (instancetype) initWithStartDate:(NSDate *) startDate endDate:(NSDate *) endDate;
```

## Parameters

- `startDate`: The start date of the date interval.
- `endDate`: The end date of the date interval.

  > ❗ **Important**:  This method raises an `NSArgumentException` if [`endDate`](./enddate.md) occurs earlier than [`startDate`](./startdate.md).

## See Also

### Creating Date Intervals
- [convenience init()](./init%28%29.md)
  Initializes a date interval by setting the start and end date to the current date.
- [init(start: Date, duration: TimeInterval)](./init%28start,duration%29.md)
  Initializes a date interval with a given start date and duration.
- [init(coder: NSCoder)](./init%28coder%29.md)
  Returns a date interval initialized from data in the given unarchiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdateinterval/init(start:end:))*