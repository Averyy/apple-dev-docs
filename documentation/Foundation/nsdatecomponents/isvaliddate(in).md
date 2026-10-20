# isValidDate(in:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Returns a Boolean value that indicates whether the current combination of properties represents a date which exists in the specified calendar.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func isValidDate(in calendar: Calendar) -> Bool
```

```objc
- (BOOL) isValidDateInCalendar:(NSCalendar *) calendar;
```

#### Return Value

[`true`](../../Swift/true.md) if the date corresponding to the receiver’s values is valid and exists in the given calendar, otherwise [`false`](../../Swift/false.md).

#### Discussion

If the [`timeZone`](./timezone.md) property is set on the receiver, the time zone property value is used.

This property should not be used for [`NSDateComponents`](../nsdatecomponents.md) objects that represent relative quantities of calendar components. To find the the next or previous date that matches a particular set of date components, use the [`NSCalendar`](../nscalendar.md) instance method [`nextDate(after:matching:value:options:)`](../nscalendar/nextdate%28after,matching,value,options%29.md) instead.

## Parameters

- `calendar`: The calendar for which to use in the calculation.

## See Also

### Validating a Date
- [var isValidDate: Bool](./isvaliddate.md)
  A Boolean value that indicates whether the current combination of properties represents a date which exists in the current calendar.
- [var date: Date?](./date.md)
  The date calculated from the current components using the stored calendar.
- [Undefined Components](../api-1430344-undefined-components.md)
  Constants that denote that the value of a date component is undefined.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdatecomponents/isvaliddate(in:))*