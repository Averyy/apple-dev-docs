# CVGetHostClockMinimumTimeDelta()

**Framework**: Core Video  
**Kind**: func  
**Role**: Function

Returns the smallest possible increment in the system time.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.4+

## Declaration

```swift
func CVGetHostClockMinimumTimeDelta() -> UInt32
```

```c
extern uint32_t CVGetHostClockMinimumTimeDelta();
```

#### Return Value

The smallest valid increment in the system time.

## See Also

### Inspecting the Host Clock
- [func CVGetCurrentHostTime() -> UInt64](./cvgetcurrenthosttime%28%29.md)
  Returns the current system time.
- [func CVGetHostClockFrequency() -> Double](./cvgethostclockfrequency%28%29.md)
  Returns the frequency of updates to the system time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvgethostclockminimumtimedelta())*