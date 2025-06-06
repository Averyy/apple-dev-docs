# init(date:timeZone:)

**Framework**: ClockKit  
**Kind**: init

Creates and returns a text provider for displaying the specified time.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
convenience init(date: Date, timeZone: TimeZone?)
```

#### Return Value

A text provider initialized with the specified date and time zone value.

## Parameters

- `date`: The date object containing the time to display. This parameter must not be  .
- `timeZone`: The time zone to use when formatting the date. If you specify  , the text provider uses the default time zone currently associated with the user.

## See Also

- [convenience init(date: Date)](clktimetextprovider/init(date:).md)
  Creates and returns a text provider for displaying the specified time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clktimetextprovider/init(date:timezone:))*