# performActivity(options:reason:using:)

**Framework**: Foundation  
**Kind**: method

Synchronously perform an activity defined by a given block using the given options.

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
func performActivity(options: ProcessInfo.ActivityOptions = [], reason: String, using block: @escaping () -> Void)
```

#### Discussion

The activity will be automatically ended after `block` returns.

## Parameters

- `options`: Options for the activity. See   for possible values.
- `reason`: A string used in debugging to indicate the reason the activity began.
- `block`: A block containing the work to be performed by the activity.

## See Also

- [func beginActivity(options: ProcessInfo.ActivityOptions, reason: String) -> any NSObjectProtocol](processinfo/beginactivity(options:reason:).md)
  Begin an activity using the given options and reason.
- [func endActivity(any NSObjectProtocol)](processinfo/endactivity(_:).md)
  Ends the given activity.
- [func performExpiringActivity(withReason: String, using: (Bool) -> Void)](processinfo/performexpiringactivity(withreason:using:).md)
  Performs the specified block asynchronously and notifies you if the process is about to be suspended.
- [ProcessInfo.ActivityOptions](processinfo/activityoptions.md)
  Option flags used with [`beginActivity(options:reason:)`](processinfo/beginactivity(options:reason:).md) and [`performActivity(options:reason:using:)`](processinfo/performactivity(options:reason:using:).md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/processinfo/performactivity(options:reason:using:))*