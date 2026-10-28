# resolveTasks(for:with:)

**Framework**: Intents  
**Kind**: method  
**Role**: Instance Method

Resolves the tasks to snooze.

**Availability**:
- iOS 13.0+ - Deprecated in 27.0
- iPadOS 13.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0
- watchOS 6.0+ - Deprecated in 27.0

> **Deprecated**: INSnoozeTasksIntentHandling is deprecated. Please adopt the Notes or Reminders AppSchema domain instead.

## Declaration

```swift
optional func resolveTasks(for intent: INSnoozeTasksIntent, with completion: @escaping @Sendable ([INSnoozeTasksTaskResolutionResult]) -> Void)
```

```swift
optional func resolveTasks(for intent: INSnoozeTasksIntent) async -> [INSnoozeTasksTaskResolutionResult]
```

```objc
- (void) resolveTasksForSnoozeTasks:(INSnoozeTasksIntent *) intent withCompletion:(void (^)(NSArray<INSnoozeTasksTaskResolutionResult *> *resolutionResults)) completion;
```

## Discussion

Implement this method to resolve the tasks to snooze. Use the intent object to obtain information about the tasks to snooze. Use the information in the [`INTask`](../intask.md) object to look up the corresponding task information in your app’s data structures. Return a resolution that includes as much information as you have available about the task.

## Parameters

- `intent`: The intent object that contains details about the user’s request. Use this object to get the initial information, if any, provided by the user.
- `completion`: The handler block to execute with the resolution. You must execute this handler while implementing this method. This handler has no return value and takes the following parameter:

  - **resolutionResult**: The object that contains the details of your proposed resolution. For a successful resolution, create a resolution object with the [`INTask`](../intask.md) object representing the task list that you intend to use.

## See Also

### Resolving Details of the Intent
- [func resolveNextTriggerTime(for: INSnoozeTasksIntent, with: (INDateComponentsRangeResolutionResult) -> Void)](./resolvenexttriggertime%28for,with%29.md)
  Resolves the trigger of when to snooze tasks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insnoozetasksintenthandling/resolvetasks(for:with:))*