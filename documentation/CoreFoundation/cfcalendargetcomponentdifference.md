# CFCalendarGetComponentDifference

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Computes the difference between the two absolute times, in terms of specified calendrical components.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```c
extern Boolean CFCalendarGetComponentDifference(CFCalendarRef calendar, CFAbsoluteTime startingAT, CFAbsoluteTime resultAT, CFOptionFlags options, const char *componentDesc, ...);
```

## Return Value

`TRUE`—and in the varargs the differences—if it is possible to calculate the difference (result - starting) between `resultAT` and `startingAT` in terms of the calendrical components specified by `componentDesc`. Returns `FALSE` if either absolute time falls outside the defined range of the calendar, or the computation cannot be performed.

## Discussion

The result is lossy if there isn’t a small enough unit requested to hold the full precision of the difference. Some operations can be ambiguous, and the behavior of the computation is calendar-specific, but generally larger components will be computed before smaller components; for example, in the Gregorian calendar a result might be `1` month and `5` days, instead of, for example, `0` months and `35` days. The resulting component values may be negative if later is before earlier.

This computation is roughly the inverse of the [`CFCalendarAddComponents`](./cfcalendaraddcomponents.md) operation, but calendrical arithmetic is invertible only in simple cases. This computation tends to be several times more expensive than the Add operation.

The following example shows how to get the approximate number of days between two absolute times (`at1`, `at2`) using an existing calendar (`gregorian`):

```objc
CFCalendarGetComponentDifference(gregorian, at1, at2, 0, "d",  &days);
```

## Parameters

- `calendar`: The calendar to use for the computation.
- `startingAT`: The starting absolute time.
- `resultAT`: The result absolute time.
- `options`: Options for the calculation. For valid values, see Constants.
- `componentDesc`: A string that describes the components provided in the variadic parameters with pointers to storage for each of the desired components. On successful return, the pointers are filled with values of the corresponding components. The type of all units is `int`.

## See Also

### Calendrical Calculations
- [CFCalendarAddComponents](./cfcalendaraddcomponents.md)
  Computes the absolute time when specified components are added to a given absolute time.
- [CFCalendarComposeAbsoluteTime](./cfcalendarcomposeabsolutetime.md)
  Computes the absolute time from components in a description string.
- [CFCalendarDecomposeAbsoluteTime](./cfcalendardecomposeabsolutetime.md)
  Computes the components which are indicated by the componentDesc description string for the given absolute time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfcalendargetcomponentdifference)*