# date

**Framework**: Foundation  
**Kind**: property

The date calculated from the current components using the stored calendar.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var date: Date? { get }
```

#### Discussion

Returns `nil` if the [`calendar`](nsdatecomponents/calendar.md) property value of the receiver is `nil` or cannot convert the receiver into an [`NSDate`](nsdate.md) object.

See [`Calendars, Date Components, and Calendar Units`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DatesAndTimes/Articles/dtCalendars.html#//apple_ref/doc/uid/TP40003470) in [`Date and Time Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DatesAndTimes/DatesAndTimes.html#//apple_ref/doc/uid/10000039i).

## See Also

- [Date and Time Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DatesAndTimes/DatesAndTimes.html#//apple_ref/doc/uid/10000039i)
- [var isValidDate: Bool](nsdatecomponents/isvaliddate.md)
  A Boolean value that indicates whether the current combination of properties represents a date which exists in the current calendar.
- [func isValidDate(in: Calendar) -> Bool](nsdatecomponents/isvaliddate(in:).md)
  Returns a Boolean value that indicates whether the current combination of properties represents a date which exists in the specified calendar.
- [Undefined Components](1430344-undefined-components.md)
  Constants that denote that the value of a date component is undefined.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdatecomponents/date)*