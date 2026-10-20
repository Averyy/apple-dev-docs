# recordAccelerometer(forDuration:)

**Framework**: Core Motion  
**Kind**: method

Begins recording accelerometer data for the specified period of time.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- watchOS 2.0+

## Declaration

```swift
func recordAccelerometer(forDuration duration: TimeInterval)
```

#### Discussion

When you call this method, the system begins capturing accelerometer data at a sample rate of 50 Hz. The system records the data for the specified amount of time, even if your app is suspended or terminated. The collected data remains accessible to your app for up to three days.

## Parameters

- `duration`: The amount of time (in seconds) for which to record the data. You may specify a time interval of up to 43,200 seconds (12 hours).


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmsensorrecorder/recordaccelerometer(forduration:))*