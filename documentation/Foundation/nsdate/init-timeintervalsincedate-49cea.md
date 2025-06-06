# init(timeInterval:sinceDate:)

**Framework**: Foundation  
**Kind**: init

Creates and returns a date object set to a given number of seconds from the specified date.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
convenience init(timeInterval secsToBeAdded: TimeInterval, sinceDate date: Date)
```

#### Return Value

An `NSDate` object set to `secsToBeAdded` seconds from `date`.

## Parameters

- `secsToBeAdded`: The number of seconds to add to  . Use a negative argument to specify a date and time before  .
- `date`: The date.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdate/init(timeinterval:sincedate:)-49cea)*