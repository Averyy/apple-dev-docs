# CFCalendarComposeAbsoluteTime

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Computes the absolute time from components in a description string.

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
extern Boolean CFCalendarComposeAbsoluteTime(CFCalendarRef calendar, CFAbsoluteTime *at, const char *componentDesc, ...);
```

## Return Value

`TRUE`—and in `at` the absolute time computed from the given components—if the `componentDesc` description string can be converted into an absolute time, otherwise `FALSE`. Also returns `FALSE` for out-of-range values.

## Discussion

When there are insufficient components provided to completely specify an absolute time, a calendar uses default values of its choice. When there is inconsistent information, a calendar may ignore some of the parameters or the function may return `FALSE`. Unnecessary components are ignored (for example, Day takes precedence over Weekday + Weekday ordinal). Note that some computations can take a relatively long time to perform.

The following example shows how to use this function to initialize an absolute time, `at`, to 6 January 1965 14:10:00, for a given calendar `gregorian` .

```objc
CFCalendarComposeAbsoluteTime(gregorian, &at, "yMdHms",  1965, 1, 6, 14, 10, 00);
```

## Parameters

- `calendar`: The calendar to use for the computation.
- `at`: Upon return, contains the computed absolute time.
- `componentDesc`: A string that describes the components provided in the varidaic parameters giving the amounts of each calendrical component in the order specified by `componentDesc`. The amounts to add may be negative, zero, positive, or any combination thereof.

## See Also

### Calendrical Calculations
- [CFCalendarAddComponents](./cfcalendaraddcomponents.md)
  Computes the absolute time when specified components are added to a given absolute time.
- [CFCalendarDecomposeAbsoluteTime](./cfcalendardecomposeabsolutetime.md)
  Computes the components which are indicated by the componentDesc description string for the given absolute time.
- [CFCalendarGetComponentDifference](./cfcalendargetcomponentdifference.md)
  Computes the difference between the two absolute times, in terms of specified calendrical components.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfcalendarcomposeabsolutetime)*