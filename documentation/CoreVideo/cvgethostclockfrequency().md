# CVGetHostClockFrequency()

**Framework**: Core Video  
**Kind**: func  
**Role**: Function

Returns the frequency of updates to the system time.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.4+

## Declaration

```swift
func CVGetHostClockFrequency() -> Double
```

```c
extern double CVGetHostClockFrequency();
```

#### Return Value

The current host frequency.

#### Discussion

In macOS, the host time bases for Core Video and CoreAudio are identical—both are based on the `mach_absolute_time` function—so the values returned from either API can be used interchangeably.

## See Also

### Inspecting the Host Clock
- [func CVGetCurrentHostTime() -> UInt64](./cvgetcurrenthosttime%28%29.md)
  Returns the current system time.
- [func CVGetHostClockMinimumTimeDelta() -> UInt32](./cvgethostclockminimumtimedelta%28%29.md)
  Returns the smallest possible increment in the system time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvgethostclockfrequency())*