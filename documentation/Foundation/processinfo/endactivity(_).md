# endActivity(_:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (void) endActivity:(id<NSObject>) activity;
```

## Parameters

- `activity`: An activity object returned by [`beginActivity(options:reason:)`](./beginactivity%28options,reason%29.md).

## See Also

### Managing activities
- [func beginActivity(options: ProcessInfo.ActivityOptions, reason: String) -> any NSObjectProtocol](./beginactivity%28options,reason%29.md)
  Begin an activity using the given options and reason.
- [func performActivity(options: ProcessInfo.ActivityOptions, reason: String, using: () -> Void)](./performactivity%28options,reason,using%29.md)
  Synchronously perform an activity defined by a given block using the given options.
- [func performExpiringActivity(withReason: String, using: (Bool) -> Void)](./performexpiringactivity%28withreason,using%29.md)
  Performs the specified block asynchronously and notifies you if the process is about to be suspended.
- [ProcessInfo.ActivityOptions](./activityoptions.md)
  Option flags used with [`beginActivity(options:reason:)`](./beginactivity%28options,reason%29.md) and [`performActivity(options:reason:using:)`](./performactivity%28options,reason,using%29.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/processinfo/endactivity(_:))*