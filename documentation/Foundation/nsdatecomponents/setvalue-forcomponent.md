# setValue(_:forComponent:)

**Framework**: Foundation  
**Kind**: method

Sets a value for a given calendar unit.

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
func setValue(_ value: Int, forComponent unit: NSCalendar.Unit)
```

#### Discussion

This method allows for component values to be set for an [`NSCalendar.Unit`](nscalendar/unit.md) value.

## Parameters

- `value`: The value to set for the   component.
- `unit`: The calendar unit for which to set  . Do not pass   or  .

## See Also

- [func value(forComponent: NSCalendar.Unit) -> Int](nsdatecomponents/value(forcomponent:).md)
  Returns the value for a given calendar unit.
- [NSCalendar.Unit](nscalendar/unit.md)
  Calendrical units such as year, month, day and hour.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdatecomponents/setvalue(_:forcomponent:))*