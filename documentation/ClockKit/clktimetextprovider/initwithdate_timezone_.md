# initWithDate:timeZone:

**Framework**: ClockKit  
**Kind**: method  
**Role**: Instance Method

Creates and returns a text provider for displaying the specified time.

**Availability**:
- watchOS 7.0+ - Deprecated in 27.2

## Declaration

```objc
- (instancetype) initWithDate:(NSDate *) date timeZone:(NSTimeZone *) timeZone;
```

## Return Value

A text provider initialized with the specified date and time zone value.

## Parameters

- `date`: The date object containing the time to display. This parameter must not be `nil`.
- `timeZone`: The time zone to use when formatting the date. If you specify `nil`, the text provider uses the default time zone currently associated with the user.

## See Also

### Creating a Text Provider
- [convenience init(date: Date)](./init%28date%29.md)
  Creates and returns a text provider for displaying the specified time.
- [- initWithDate:](./initwithdate_.md)
  Creates and returns a text provider for displaying the specified time.
- [convenience init(date: Date, timeZone: TimeZone?)](./init%28date,timezone%29.md)
  Creates and returns a text provider for displaying the specified time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clktimetextprovider/initwithdate:timezone:)*