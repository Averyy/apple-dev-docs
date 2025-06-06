# init(start:duration:)

**Framework**: Foundation  
**Kind**: init

Initializes a date interval with a given start date and duration.

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
init(start startDate: Date, duration: TimeInterval)
```

#### Discussion

This is the designated initializer.

## Parameters

- `startDate`: The start date of the date interval.
- `duration`: The duration from the start date for the date interval.

## See Also

- [convenience init()](nsdateinterval/init.md)
  Initializes a date interval by setting the start and end date to the current date.
- [convenience init(start: Date, end: Date)](nsdateinterval/init(start:end:).md)
  Initializes a date interval from a given start date and end date.
- [init(coder: NSCoder)](nsdateinterval/init(coder:).md)
  Returns a date interval initialized from data in the given unarchiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdateinterval/init(start:duration:))*