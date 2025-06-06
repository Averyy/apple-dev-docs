# date

**Framework**: ClockKit  
**Kind**: property

The date object containing the time value.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
var date: Date { get set }
```

#### Discussion

You can make changes to this property until you hand off the timeline entry containing it to ClockKit. The value of this property must not be `nil`.

## See Also

- [convenience init(date: Date)](clktimetextprovider/init(date:).md)
  Creates and returns a text provider for displaying the specified time.
- [convenience init(date: Date, timeZone: TimeZone?)](clktimetextprovider/init(date:timezone:).md)
  Creates and returns a text provider for displaying the specified time.
- [var timeZone: TimeZone?](clktimetextprovider/timezone.md)
  The time zone used to format time values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clktimetextprovider/date)*