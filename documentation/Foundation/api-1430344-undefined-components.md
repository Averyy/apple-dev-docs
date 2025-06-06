# Undefined Components

**Framework**: Foundation

Constants that denote that the value of a date component is undefined.

#### Overview

For example, when an [`NSDateComponents`](nsdatecomponents.md) object is created as the result of calculating the distance in time between two dates represented by a particular calendar, the value for the [`weekOfYear`](nscalendar/unit/weekofyear.md) component would be set to [`NSDateComponentUndefined`](nsdatecomponentundefined.md).

## Topics

### Constants
- [var NSDateComponentUndefined: Int](nsdatecomponentundefined.md)
  Specifies a date component without a value.
- [var NSUndefinedDateComponent: Int](nsundefineddatecomponent.md)
  Specifies a date component without a value.

## See Also

- [var isValidDate: Bool](nsdatecomponents/isvaliddate.md)
  A Boolean value that indicates whether the current combination of properties represents a date which exists in the current calendar.
- [func isValidDate(in: Calendar) -> Bool](nsdatecomponents/isvaliddate(in:).md)
  Returns a Boolean value that indicates whether the current combination of properties represents a date which exists in the specified calendar.
- [var date: Date?](nsdatecomponents/date.md)
  The date calculated from the current components using the stored calendar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/1430344-undefined-components)*