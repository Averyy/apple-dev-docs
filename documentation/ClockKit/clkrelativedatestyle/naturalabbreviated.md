# CLKRelativeDateStyle.naturalAbbreviated

**Framework**: ClockKit  
**Kind**: case  
**Role**: Case

An abbreviated, natural date style.

**Availability**:
- watchOS 5.0+ - Deprecated in 27.2

## Declaration

```swift
case naturalAbbreviated
```

```c
CLKRelativeDateStyleNaturalAbbreviated
```

#### Discussion

The smallest possible abbreviation of the natural date style. For example, ten hours and nine minutes always formats as “10H 9M.” The [`CLKRelativeDateStyle.natural`](./natural.md) style may provide a longer string like “10hrs 9min” if there’s enough space.

## See Also

### Date Styles
- [CLKRelativeDateStyle.natural](./natural.md)
  A natural date style.
- [CLKRelativeDateStyle.naturalFull](./naturalfull.md)
  A natural date style using unabbreviated units, when possible.
- [CLKRelativeDateStyle.offset](./offset.md)
  An offset date style.
- [CLKRelativeDateStyle.offsetShort](./offsetshort.md)
  A short offset date style.
- [CLKRelativeDateStyle.timer](./timer.md)
  A timer style.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkrelativedatestyle/naturalabbreviated)*