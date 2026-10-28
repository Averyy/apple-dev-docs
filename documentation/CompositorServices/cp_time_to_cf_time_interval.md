# cp_time_to_cf_time_interval

**Framework**: Compositor Services  
**Kind**: func  
**Role**: Function

Converts a Mach absolute time value to a Core Foundation time value.

**Availability**:
- macOS 26.0+
- visionOS 1.0+

## Declaration

```c
CFTimeInterval cp_time_to_cf_time_interval(cp_time_t time);
```

## Return Value

The elapsed time in seconds that correspond to the specified time value.

## Parameters

- `time`: The time value to convert.

## See Also

### Converting time values
- [cp_time_t](./cp_time_t.md)
  A Mach absolute time clock value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/cp_time_to_cf_time_interval)*