# vDSP_biquadm_SetActiveFilters

**Framework**: Accelerate  
**Kind**: func

Activates or deactivates individual sections in a single-precision, multichannel biquadratic filter.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
extern void vDSP_biquadm_SetActiveFilters(vDSP_biquadm_Setup __setup, const _Bool * __filter_states);
```

#### Discussion

For each section in a multichannel biquadratic filter, the corresponding Boolean value in `filter_states` sets the section to active or inactive. The apply function removes inactive filters from the processing chain. The biquadratic filter retains the state of inactive sections for future use.

## Parameters

- `__setup`: The biquadratic filter setup object that the function updates.
- `__filter_states`: An array of Boolean values, each of which corresponds to a section in the biquadratic filter.

## See Also

- [vDSP_biquadm_SetActiveFiltersD](vdsp_biquadm_setactivefiltersd.md)
  Activates or deactivates individual sections in a double-precision, multichannel biquadratic filter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_biquadm_setactivefilters)*