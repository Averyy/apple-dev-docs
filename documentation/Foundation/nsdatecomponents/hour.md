# hour

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

The number of hour units for the receiver.

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
var hour: Int { get set }
```

```objc
@property NSInteger hour;
```

#### Discussion

This value is interpreted in the context of the calendar with which it is used—see [Calendars, Date Components, and Calendar Units](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DatesAndTimes/Articles/dtCalendars.html#//apple_ref/doc/uid/TP40003470) in [Date and Time Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DatesAndTimes/DatesAndTimes.html#//apple_ref/doc/uid/10000039i).

## See Also

### Accessing Hours and Seconds
- [var minute: Int](./minute.md)
  The number of minute units for the receiver.
- [var second: Int](./second.md)
  The number of second units for the receiver.
- [var nanosecond: Int](./nanosecond.md)
  The number of nanosecond units for the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdatecomponents/hour)*