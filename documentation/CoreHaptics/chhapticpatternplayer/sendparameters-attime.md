# sendParameters(_:atTime:)

**Framework**: Core Haptics  
**Kind**: method  
**Required**: Yes

Sends an array of haptic parameters, starting at the specified time.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
func sendParameters(_ parameters: [CHHapticDynamicParameter], atTime time: TimeInterval) throws
```

#### Discussion

If `time` is `0` or any value less than the haptic engine’s [`currentTime`](chhapticengine/currenttime.md), this method sends parameters immediately.

## Parameters

- `parameters`: An array of dynamic parameters to send together.
- `time`: The time at which to send the dynamic parameters.

## See Also

- [func scheduleParameterCurve(CHHapticParameterCurve, atTime: TimeInterval) throws](chhapticpatternplayer/scheduleparametercurve(_:attime:).md)
  Schedules a parameter curve to begin transitioning a parameter at a certain time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corehaptics/chhapticpatternplayer/sendparameters(_:attime:))*