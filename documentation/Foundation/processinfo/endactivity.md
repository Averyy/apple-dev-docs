# endActivity(_:)

**Framework**: Foundation  
**Kind**: method

Ends the given activity.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func endActivity(_ activity: any NSObjectProtocol)
```

## Parameters

- `activity`: An activity object returned by  .

## See Also

- [func beginActivity(options: ProcessInfo.ActivityOptions, reason: String) -> any NSObjectProtocol](processinfo/beginactivity(options:reason:).md)
  Begin an activity using the given options and reason.
- [func performActivity(options: ProcessInfo.ActivityOptions, reason: String, using: () -> Void)](processinfo/performactivity(options:reason:using:).md)
  Synchronously perform an activity defined by a given block using the given options.
- [func performExpiringActivity(withReason: String, using: (Bool) -> Void)](processinfo/performexpiringactivity(withreason:using:).md)
  Performs the specified block asynchronously and notifies you if the process is about to be suspended.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/processinfo/endactivity(_:))*