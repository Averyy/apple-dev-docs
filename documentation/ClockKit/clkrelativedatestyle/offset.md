# CLKRelativeDateStyle.offset

**Framework**: ClockKit  
**Kind**: case  
**Role**: Case

An offset date style.

**Availability**:
- watchOS 2.0+ - Deprecated in 27.2

> **Deprecated**: On watchOS 9.0 or later, use WidgetKit instead

## Declaration

```swift
case offset
```

```c
CLKRelativeDateStyleOffset
```

## Discussion

The resulting value gives the time offset using a single key unit. For example, values might be “10 hours”, or “9 minutes” depending on the total amount of time between the current date and the date you specified.

## See Also

### Date Styles
- [CLKRelativeDateStyle.natural](./natural.md)
  A natural date style.
- [CLKRelativeDateStyle.naturalAbbreviated](./naturalabbreviated.md)
  An abbreviated, natural date style.
- [CLKRelativeDateStyle.naturalFull](./naturalfull.md)
  A natural date style using unabbreviated units, when possible.
- [CLKRelativeDateStyle.offsetShort](./offsetshort.md)
  A short offset date style.
- [CLKRelativeDateStyle.timer](./timer.md)
  A timer style.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkrelativedatestyle/offset)*