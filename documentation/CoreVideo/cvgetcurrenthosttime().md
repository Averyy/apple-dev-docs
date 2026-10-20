# CVGetCurrentHostTime()

**Framework**: Core Video  
**Kind**: func  
**Role**: Function

Returns the current system time.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.4+

## Declaration

```swift
func CVGetCurrentHostTime() -> UInt64
```

```c
extern uint64_t CVGetCurrentHostTime();
```

#### Return Value

The current host time.

#### Discussion

In macOS, the host time bases for Core Video and CoreAudio are identical—both are based on the `mach_absolute_time` function—so the values returned from either API can be used interchangeably.

## See Also

### Inspecting the Host Clock
- [func CVGetHostClockFrequency() -> Double](./cvgethostclockfrequency%28%29.md)
  Returns the frequency of updates to the system time.
- [func CVGetHostClockMinimumTimeDelta() -> UInt32](./cvgethostclockminimumtimedelta%28%29.md)
  Returns the smallest possible increment in the system time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvgetcurrenthosttime())*