# value(forComponent:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Returns the value for a given calendar unit.

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
func value(forComponent unit: NSCalendar.Unit) -> Int
```

```objc
- (NSInteger) valueForComponent:(NSCalendarUnit) unit;
```

## Return Value

The value for the given calendar unit.

## Discussion

This method allows for component values to be retrieved for an [`NSCalendar.Unit`](../nscalendar/unit.md) value.

## Parameters

- `unit`: The calendar unit for which to retrieve its value. Do not pass [`calendar`](../nscalendar/unit/calendar.md) or [`timeZone`](../nscalendar/unit/timezone.md).

## See Also

### Accessing Components as Calendrical Units
- [func setValue(Int, forComponent: NSCalendar.Unit)](./setvalue%28_,forcomponent%29.md)
  Sets a value for a given calendar unit.
- [NSCalendar.Unit](../nscalendar/unit.md)
  Calendrical units such as year, month, day and hour.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdatecomponents/value(forcomponent:))*