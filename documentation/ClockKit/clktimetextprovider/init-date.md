# init(date:)

**Framework**: ClockKit  
**Kind**: init

Creates and returns a text provider for displaying the specified time.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
convenience init(date: Date)
```

#### Return Value

A text provider initialized with the specified date.

#### Discussion

The text provider created by this method uses the default time zone information of the current user. The time value is formatted using the current locale information for the user.

## Parameters

- `date`: The date object containing the time to display. This parameter must not be  .

## See Also

- [convenience init(date: Date, timeZone: TimeZone?)](clktimetextprovider/init(date:timezone:).md)
  Creates and returns a text provider for displaying the specified time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clktimetextprovider/init(date:))*