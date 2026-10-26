# CFCalendarAddComponents

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Computes the absolute time when specified components are added to a given absolute time.

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
extern Boolean CFCalendarAddComponents(CFCalendarRef calendar, CFAbsoluteTime *at, CFOptionFlags options, const char *componentDesc, ...);
```

#### Return Value

`TRUE`—and in `at` the computed time—if `at` falls inside the defined range of the calendar and it is possible to calculate the absolute time when the components (the calendrical components specified by `componentDesc` and given in the varargs) are added to the input absolute time `at`; otherwise `FALSE`.

#### Discussion

Some operations can be ambiguous, and the behavior of the computation is calendar-specific, but generally components are added in the order specified.

If you specify a “wrap” option ([`kCFCalendarComponentsWrap`](./kcfcalendarcomponentswrap.md)), the specified components should be incremented and wrap around to zero/one on overflow, but should not cause higher units to be incremented. When “Wrap” is false, overflow in a unit carries into the higher units, as in typical addition.

Note that some computations can take a relatively long time to perform.

The following example shows how to add 2 months and 3 days to absolute time `at`’s current value using an existing calendar (`gregorian`):

```objc
CFCalendarAddComponents(gregorian, &at, 0, "Md",  2, 3);
```

## Parameters

- `calendar`: The calendar to use for the computation.
- `at`: A reference to an absolute time. On input, points to the absolute time to which components are to be added; on output, points to the result of the computation.
- `options`: Options for the calculation. For valid values, see Constants.
- `componentDesc`: A string that describes the components provided in the variadic parameters giving amounts of each calendrical component in the order specified by `componentDesc`. The amounts to add may be negative, zero, positive, or any combination thereof.

## See Also

### Calendrical Calculations
- [CFCalendarComposeAbsoluteTime](./cfcalendarcomposeabsolutetime.md)
  Computes the absolute time from components in a description string.
- [CFCalendarDecomposeAbsoluteTime](./cfcalendardecomposeabsolutetime.md)
  Computes the components which are indicated by the componentDesc description string for the given absolute time.
- [CFCalendarGetComponentDifference](./cfcalendargetcomponentdifference.md)
  Computes the difference between the two absolute times, in terms of specified calendrical components.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfcalendaraddcomponents)*