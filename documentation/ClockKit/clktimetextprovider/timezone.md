# timeZone

**Framework**: ClockKit  
**Kind**: property

The time zone used to format time values.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
var timeZone: TimeZone? { get set }
```

#### Discussion

If the value of this property is `nil`, the text provider uses the time zone currently configured for the user.

## See Also

- [convenience init(date: Date, timeZone: TimeZone?)](clktimetextprovider/init(date:timezone:).md)
  Creates and returns a text provider for displaying the specified time.
- [var date: Date](clktimetextprovider/date.md)
  The date object containing the time value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clktimetextprovider/timezone)*