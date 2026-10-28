# sendParameters(_:atTime:)

**Framework**: Core Haptics  
**Kind**: method  
**Role**: Instance Method  
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

```objc
- (BOOL) sendParameters:(NSArray<CHHapticDynamicParameter *> *) parameters atTime:(NSTimeInterval) time error:(NSError **) outError;
```

## Discussion

If `time` is `0` or any value less than the haptic engine’s [`currentTime`](../chhapticengine/currenttime.md), this method sends parameters immediately.

## Parameters

- `parameters`: An array of dynamic parameters to send together.
- `time`: The time at which to send the dynamic parameters.

## See Also

### Sending Parameters to a Haptic
- [func scheduleParameterCurve(CHHapticParameterCurve, atTime: TimeInterval) throws](./scheduleparametercurve%28_,attime%29.md)
  Schedules a parameter curve to begin transitioning a parameter at a certain time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corehaptics/chhapticpatternplayer/sendparameters(_:attime:))*