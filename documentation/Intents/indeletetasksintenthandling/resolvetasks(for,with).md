# resolveTasks(for:with:)

**Framework**: Intents  
**Kind**: method  
**Role**: Instance Method

Resolves the tasks to delete.

**Availability**:
- iOS 13.0+ - Deprecated in 15.0
- iPadOS 13.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 6.0+ - Deprecated in 8.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

```swift
optional func resolveTasks(for intent: INDeleteTasksIntent, with completion: @escaping @Sendable ([INDeleteTasksTaskResolutionResult]) -> Void)
```

```swift
optional func resolveTasks(for intent: INDeleteTasksIntent) async -> [INDeleteTasksTaskResolutionResult]
```

```objc
- (void) resolveTasksForDeleteTasks:(INDeleteTasksIntent *) intent withCompletion:(void (^)(NSArray<INDeleteTasksTaskResolutionResult *> *resolutionResults)) completion;
```

#### Discussion

This method resolves the tasks to delete. Use the intent object to obtain information about the task to delete. Use the information in the [`INTask`](../intask.md) object to look up the corresponding task information in your app’s data structures.

## Parameters

- `intent`: The intent object that contains details about the user’s request. Use this object to get the initial information, if any, provided by the user.
- `completion`: The handler block to execute with the resolution. You must execute this block while implementing this method. This handler has no return value and takes the following parameter:

  - **resolutionResult**: The object that contains the details of your proposed resolution. For a successful resolution, create a resolution object with the [`INTask`](../intask.md) object that represents the task list you intend to use.

## See Also

### Resolving Details of the Intent
- [func resolveTaskList(for: INDeleteTasksIntent, with: (INDeleteTasksTaskListResolutionResult) -> Void)](./resolvetasklist%28for,with%29.md)
  Resolves the task list from which to delete tasks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/indeletetasksintenthandling/resolvetasks(for:with:))*