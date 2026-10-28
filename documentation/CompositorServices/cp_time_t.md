# cp_time_t

**Framework**: Compositor Services  
**Kind**: typealias  
**Role**: Type Alias

A Mach absolute time clock value.

**Availability**:
- macOS 26.0+
- visionOS 1.0+

## Declaration

```c
typedef struct cp_time cp_time_t;
```

## Discussion

Mach absolute time measures the number of ticks that have elapsed since an arbitrary point after system startup. Each value represents a unique point in time during the course of your app’s execution.

## Topics

### Getting the time value
- [cp_mach_abs_time](./cp_time/cp_mach_abs_time.md)
  The Mach absolute time value.

## See Also

### Converting time values
- [cp_time_to_cf_time_interval](./cp_time_to_cf_time_interval.md)
  Converts a Mach absolute time value to a Core Foundation time value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/cp_time_t)*