# CLKRelativeDateStyle.naturalFull

**Framework**: ClockKit  
**Kind**: case

A natural date style using unabbreviated units, when possible.

**Availability**:
- watchOS 6.0+

## Declaration

```swift
case naturalFull
```

#### Discussion

The text provider breaks the time interval into various components. If there’s enough space, it uses the full word for the units; otherwise, it abbreviates them. For example, it formats 10 hours and 9 minutes as “10 hours 9 minutes”.

## See Also

- [CLKRelativeDateStyle.natural](clkrelativedatestyle/natural.md)
  A natural date style.
- [CLKRelativeDateStyle.naturalAbbreviated](clkrelativedatestyle/naturalabbreviated.md)
  An abbreviated, natural date style.
- [CLKRelativeDateStyle.offset](clkrelativedatestyle/offset.md)
  An offset date style.
- [CLKRelativeDateStyle.offsetShort](clkrelativedatestyle/offsetshort.md)
  A short offset date style.
- [CLKRelativeDateStyle.timer](clkrelativedatestyle/timer.md)
  A timer style.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkrelativedatestyle/naturalfull)*