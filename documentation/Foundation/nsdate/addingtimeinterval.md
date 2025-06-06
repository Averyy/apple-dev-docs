# addingTimeInterval(_:)

**Framework**: Foundation  
**Kind**: method

Returns a new date object that is set to a given number of seconds relative to the receiver.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func addingTimeInterval(_ ti: TimeInterval) -> Self
```

#### Return Value

A new `NSDate` object that is set to `seconds` seconds relative to the receiver. The date returned might have a representation different from the receiver’s.

## Parameters

- `ti`: The number of seconds to add to the receiver. Use a negative value for seconds to have the returned object specify a date before the receiver.

## See Also

- [convenience init(timeInterval: TimeInterval, sinceDate: Date)](nsdate/init(timeinterval:sincedate:)-71m1f.md)
  Returns a date object initialized relative to another given date by a given number of seconds.
- [func timeIntervalSince(Date) -> TimeInterval](nsdate/timeintervalsince(_:).md)
  Returns the interval between the receiver and another given date.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdate/addingtimeinterval(_:))*