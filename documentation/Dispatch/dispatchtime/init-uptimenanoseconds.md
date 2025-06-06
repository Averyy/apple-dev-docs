# init(uptimeNanoseconds:)

**Framework**: Dispatch  
**Kind**: init

Creates a time relative to the amount of time the system has been running.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
init(uptimeNanoseconds: UInt64)
```

#### Discussion

On Apple platforms, this clock is the same as the value returned by [`mach_absolute_time`](https://developer.apple.com/documentation/kernel/1462446-mach_absolute_time) when converted into nanoseconds.

## Parameters

- `uptimeNanoseconds`: The number of nanoseconds since boot, excluding any time the system spent asleep.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatchtime/init(uptimenanoseconds:))*