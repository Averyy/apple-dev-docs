# CMClockGetPreferredStartTimePattern

**Framework**: Core Media  
**Kind**: func  
**Role**: Function

Retrieves a description of the pattern of preferred start times, such as for synchronization with an external genlock signal.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```c
extern OSStatus CMClockGetPreferredStartTimePattern(CMClockRef clock, CMTime *outClockStartTime, CMTime *outHostClockStartTime, CMTime *outDeltaBetweenPreferredStartTimes);
```

## Return Value

`noErr` on success, `kCMClockError_UnsupportedOperation` if the clock does not support this function, or `kCMClockError_PreferredStartTimeNotAvailable` if the system is not disciplined to a present signal.

## Discussion

When the system is disciplined to a sync signal, this function returns a matched time pair in the near future and the delta between successive times.

## Parameters

- `outClockStartTime`: Points to a CMTime to receive the clock time of the next preferred start time pair.
- `outHostClockStartTime`: Points to a CMTime to receive the host clock time of the next preferred start time pair.
- `outDeltaBetweenPreferredStartTimes`: Points to a CMTime to receive the delta between successive preferred start times. Integer multiples of this delta may be added to the clock start time and host clock start time to calculate near future preferred start times.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmclockgetpreferredstarttimepattern)*