# CVGetCurrentHostTime()

**Framework**: Core Video  
**Kind**: func

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

#### Return Value

The current host time.

#### Discussion

In macOS, the host time bases for Core Video and CoreAudio are identical—both are based on the `mach_absolute_time` function—so the values returned from either API can be used interchangeably.

## See Also

- [func CVGetHostClockFrequency() -> Double](cvgethostclockfrequency().md)
  Returns the frequency of updates to the system time.
- [func CVGetHostClockMinimumTimeDelta() -> UInt32](cvgethostclockminimumtimedelta().md)
  Returns the smallest possible increment in the system time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvgetcurrenthosttime())*