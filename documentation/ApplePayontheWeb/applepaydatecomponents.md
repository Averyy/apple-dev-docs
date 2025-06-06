# ApplePayDateComponents

**Framework**: Apple Pay on the Web  
**Kind**: struct

A dictionary that specifies the values for the calendrical units for a date.

**Availability**:
- Safari Desktop 10.0+
- Safari Mobile 10.0+

## Declaration

```swift
dictionary ApplePayDateComponents {
	long years;
	long months;
	long days;
	long hours;
};
```

#### Overview

When specifying a range using date components, provide all elements of the [`ApplePayDateComponents`](applepaydatecomponents.md) down to the level of granularity that you want to expose. For example, if you specify a range of days, be sure to include values for both [`months`](applepaydatecomponents/months.md) and [`years`](applepaydatecomponents/years.md) in addition to [`days`](applepaydatecomponents/days.md) in the [`ApplePayDateComponents`](applepaydatecomponents.md).

[`Apple Pay on the Web`](ApplePayontheWeb.md) uses the Gregorian calendar when processing dates.

## Topics

### Date Components
- [years](applepaydatecomponents/years.md)
  A number that represents a year.
- [months](applepaydatecomponents/months.md)
  A number between 1 and 12 that represents a month.
- [days](applepaydatecomponents/days.md)
  A number that represents a day.
- [hours](applepaydatecomponents/hours.md)
  A number that represents an hour.

## See Also

- [startDateComponents](applepaydatecomponentsrange/startdatecomponents.md)
  The start date and time of the range.
- [endDateComponents](applepaydatecomponentsrange/enddatecomponents.md)
  The end date and time of the range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applepayontheweb/applepaydatecomponents)*