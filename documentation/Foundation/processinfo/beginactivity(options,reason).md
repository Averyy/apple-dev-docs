# beginActivity(options:reason:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (id<NSObject>) beginActivityWithOptions:(NSActivityOptions) options reason:(NSString *) reason;
```

## Return Value

An object token representing the activity.

## Discussion

Indicate completion of the activity by calling [`endActivity(_:)`](./endactivity%28_%29.md) passing the returned object as the argument.

## Parameters

- `options`: Options for the activity. See [`ProcessInfo.ActivityOptions`](./activityoptions.md) for possible values.
- `reason`: A string used in debugging to indicate the reason the activity began.

## See Also

### Managing activities
- [func endActivity(any NSObjectProtocol)](./endactivity%28_%29.md)
  Ends the given activity.
- [func performActivity(options: ProcessInfo.ActivityOptions, reason: String, using: () -> Void)](./performactivity%28options,reason,using%29.md)
  Synchronously perform an activity defined by a given block using the given options.
- [func performExpiringActivity(withReason: String, using: (Bool) -> Void)](./performexpiringactivity%28withreason,using%29.md)
  Performs the specified block asynchronously and notifies you if the process is about to be suspended.
- [ProcessInfo.ActivityOptions](./activityoptions.md)
  Option flags used with [`beginActivity(options:reason:)`](./beginactivity%28options,reason%29.md) and [`performActivity(options:reason:using:)`](./performactivity%28options,reason,using%29.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/processinfo/beginactivity(options:reason:))*