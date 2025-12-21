# beginActivity(options:reason:)

**Framework**: Foundation  
**Kind**: method

Begin an activity using the given options and reason.

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
func beginActivity(options: ProcessInfo.ActivityOptions = [], reason: String) -> any NSObjectProtocol
```

#### Return Value

An object token representing the activity.

#### Discussion

Indicate completion of the activity by calling [`endActivity(_:)`](processinfo/endactivity(_:).md) passing the returned object as the argument.

## Parameters

- `options`: Options for the activity. See   for possible values.
- `reason`: A string used in debugging to indicate the reason the activity began.

## See Also

- [func endActivity(any NSObjectProtocol)](processinfo/endactivity(_:).md)
  Ends the given activity.
- [func performActivity(options: ProcessInfo.ActivityOptions, reason: String, using: () -> Void)](processinfo/performactivity(options:reason:using:).md)
  Synchronously perform an activity defined by a given block using the given options.
- [func performExpiringActivity(withReason: String, using: (Bool) -> Void)](processinfo/performexpiringactivity(withreason:using:).md)
  Performs the specified block asynchronously and notifies you if the process is about to be suspended.
- [ProcessInfo.ActivityOptions](processinfo/activityoptions.md)
  Option flags used with [`beginActivity(options:reason:)`](processinfo/beginactivity(options:reason:).md) and [`performActivity(options:reason:using:)`](processinfo/performactivity(options:reason:using:).md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/processinfo/beginactivity(options:reason:))*