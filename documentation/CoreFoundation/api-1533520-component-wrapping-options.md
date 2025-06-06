# Component Wrapping Options

**Framework**: Core Foundation

The wrapping option specifies overflow behavior for calendar components in calendrical calculations

#### Overview

The wrapping option specifies overflow behavior for calendar components in calendrical calculations—see [`CFCalendarAddComponents`](cfcalendaraddcomponents.md) and [`CFCalendarGetComponentDifference`](cfcalendargetcomponentdifference.md).

## Topics

### Constants
- [var kCFCalendarComponentsWrap: CFOptionFlags](kcfcalendarcomponentswrap.md)
  Specifies that the components specified for calendar components should be incremented and wrap around to zero/one on overflow, but should not cause higher units to be incremented.

## See Also

- [struct CFCalendarUnit](cfcalendarunit.md)
  CFCalendarUnit constants are used to specify calendrical units, such as day or month, in various calendar calculations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/1533520-component-wrapping-options)*