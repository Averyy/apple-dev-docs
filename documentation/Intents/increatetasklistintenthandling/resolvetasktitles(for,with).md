# resolveTaskTitles(for:with:)

**Framework**: Intents  
**Kind**: method  
**Role**: Instance Method

Resolves the tasks in a task list.

**Availability**:
- iOS 11.0+ - Deprecated in 15.0
- iPadOS 11.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 4.0+ - Deprecated in 8.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

```swift
optional func resolveTaskTitles(for intent: INCreateTaskListIntent, with completion: @escaping @Sendable ([INSpeakableStringResolutionResult]) -> Void)
```

```swift
optional func resolveTaskTitles(for intent: INCreateTaskListIntent) async -> [INSpeakableStringResolutionResult]
```

```objc
- (void) resolveTaskTitlesForCreateTaskList:(INCreateTaskListIntent *) intent withCompletion:(void (^)(NSArray<INSpeakableStringResolutionResult *> *resolutionResults)) completion;
```

#### Discussion

Implement this method to resolve the tasks for a task list. Use the intent object to obtain the initial titles suggested by the user. If the user doesn’t supply any task titles and you don’t require an initial set of tasks, return a resolution of not required. Alternatively, you can supply a default task title and create a successful resolution.

## Parameters

- `intent`: The intent object containing details about the user’s request. Use this object to get the initial information, if any, provided by the user.
- `completion`: The handler block to execute with the resolution. You must execute this handler at some point during your implementation of this method. This handler has no return value and takes the following parameter:

  - **resolutionResults**: The details of your proposed resolutions. For successful resolutions, create an array of resolution objects with the title strings to use for the tasks.

## See Also

### Resolving the Intent Parameters
- [func resolveTitle(for: INCreateTaskListIntent, with: (INSpeakableStringResolutionResult) -> Void)](./resolvetitle%28for,with%29.md)
  Resolves the title of the task list.
- [func resolveGroupName(for: INCreateTaskListIntent, with: (INSpeakableStringResolutionResult) -> Void)](./resolvegroupname%28for,with%29.md)
  Resolves the intended group for the task list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/increatetasklistintenthandling/resolvetasktitles(for:with:))*