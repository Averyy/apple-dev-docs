# cp_time

**Framework**: Compositor Services  
**Kind**: struct  
**Role**: Structure

A Mach absolute time clock value.

**Availability**:
- macOS 26.0+
- visionOS 1.0+

## Declaration

```c
struct cp_time;
```

#### Overview

Mach absolute time measures the number of ticks that have elapsed since an arbitrary point after system startup. Each value represents a unique point in time during the course of your app’s execution.

## Topics

### Instance Properties
- [cp_mach_abs_time](./cp_time/cp_mach_abs_time.md)
  The Mach absolute time value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/cp_time)*