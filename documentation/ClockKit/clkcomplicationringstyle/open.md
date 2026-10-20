# CLKComplicationRingStyle.open

**Framework**: ClockKit  
**Kind**: case  
**Role**: Case

A ring in which the values increase clockwise, starting in the lower-left corner, leaving an opening at the bottom of the circle.

**Availability**:
- watchOS 2.0+ - Deprecated in 27.2

> **Deprecated**: On watchOS 9.0 or later, use WidgetKit instead

## Declaration

```swift
case open
```

```c
CLKComplicationRingStyleOpen
```

#### Discussion

Use this style when you want to convey a value that’s in between two other values that don’t represent an absolute minimum or maximum. For example, you might use this style for a temperature gauge or speedometer.

## See Also

### Constants
- [CLKComplicationRingStyle.closed](./closed.md)
  A ring in which the values increase clockwise, starting at 12 o’clock, to create a closed circle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationringstyle/open)*