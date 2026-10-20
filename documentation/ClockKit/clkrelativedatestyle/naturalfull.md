# CLKRelativeDateStyle.naturalFull

**Framework**: ClockKit  
**Kind**: case  
**Role**: Case

A natural date style using unabbreviated units, when possible.

**Availability**:
- watchOS 6.0+ - Deprecated in 27.2

## Declaration

```swift
case naturalFull
```

```c
CLKRelativeDateStyleNaturalFull
```

#### Discussion

The text provider breaks the time interval into various components. If there’s enough space, it uses the full word for the units; otherwise, it abbreviates them. For example, it formats 10 hours and 9 minutes as “10 hours 9 minutes”.

## See Also

### Date Styles
- [CLKRelativeDateStyle.natural](./natural.md)
  A natural date style.
- [CLKRelativeDateStyle.naturalAbbreviated](./naturalabbreviated.md)
  An abbreviated, natural date style.
- [CLKRelativeDateStyle.offset](./offset.md)
  An offset date style.
- [CLKRelativeDateStyle.offsetShort](./offsetshort.md)
  A short offset date style.
- [CLKRelativeDateStyle.timer](./timer.md)
  A timer style.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkrelativedatestyle/naturalfull)*