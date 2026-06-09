# init(timeInterval:since:)

**Framework**: Foundation  
**Kind**: init

Returns a date object initialized relative to another given date by a given number of seconds.

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
convenience init(timeInterval secsToBeAdded: TimeInterval, since date: Date)
```

#### Return Value

An `NSDate` object initialized relative to `date` by `secsToBeAdded` seconds.

## Parameters

- `secsToBeAdded`: The number of seconds to add to `date`. A negative value means the receiver will be earlier than `date`.
- `date`: The reference date.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdate/init(timeinterval:since:))*