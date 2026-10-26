# initWithDate:

**Framework**: ClockKit  
**Kind**: method  
**Role**: Instance Method

Creates and returns a text provider for displaying the specified time.

**Availability**:
- watchOS 7.0+ - Deprecated in 27.2

## Declaration

```objc
- (instancetype) initWithDate:(NSDate *) date;
```

#### Return Value

A text provider initialized with the specified date.

#### Discussion

The text provider created by this method uses the default time zone information of the current user. The time value is formatted using the current locale information for the user.

## Parameters

- `date`: The date object containing the time to display. This parameter must not be `nil`.

## See Also

### Creating a Text Provider
- [convenience init(date: Date)](./init%28date%29.md)
  Creates and returns a text provider for displaying the specified time.
- [convenience init(date: Date, timeZone: TimeZone?)](./init%28date,timezone%29.md)
  Creates and returns a text provider for displaying the specified time.
- [- initWithDate:timeZone:](./initwithdate_timezone_.md)
  Creates and returns a text provider for displaying the specified time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clktimetextprovider/initwithdate:)*