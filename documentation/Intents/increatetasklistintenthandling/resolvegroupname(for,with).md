# resolveGroupName(for:with:)

**Framework**: Intents  
**Kind**: method  
**Role**: Instance Method

Resolves the intended group for the task list.

**Availability**:
- iOS 11.0+ - Deprecated in 15.0
- iPadOS 11.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 4.0+ - Deprecated in 8.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

```swift
optional func resolveGroupName(for intent: INCreateTaskListIntent, with completion: @escaping @Sendable (INSpeakableStringResolutionResult) -> Void)
```

```swift
optional func resolveGroupName(for intent: INCreateTaskListIntent) async -> INSpeakableStringResolutionResult
```

```objc
- (void) resolveGroupNameForCreateTaskList:(INCreateTaskListIntent *) intent withCompletion:(void (^)(INSpeakableStringResolutionResult *resolutionResult)) completion;
```

#### Discussion

Implement this method to resolve the intended group for a task list. Use the intent object to obtain the group information, if any, specified by the user. Groups are a way for you to organize the task lists of your app. For example, the Reminders app automatically provides a group for each unique service, such as iCloud, that manages task lists and tasks.

If the intent doesn’t contain a group name, choose a resolution that’s most appropriate for your app. If your app doesn’t support organizing notes into groups, you might return a result indicating that the group name isn’t required. If you’re able to select a default group for the note, create a successful resolution that includes the name of the group you selected.

## Parameters

- `intent`: The intent object containing details about the user’s request. Use this object to get the initial information, if any, provided by the user.
- `completion`: The handler block to execute with the resolution. You must execute this handler at some point during your implementation of this method. This handler has no return value and takes the following parameter:

  - **resolutionResult**: The object containing the details of your proposed resolution. For successful resolutions, create a resolution object with the name of the group in which you intend to place the task list.

## See Also

### Resolving the Intent Parameters
- [func resolveTitle(for: INCreateTaskListIntent, with: (INSpeakableStringResolutionResult) -> Void)](./resolvetitle%28for,with%29.md)
  Resolves the title of the task list.
- [func resolveTaskTitles(for: INCreateTaskListIntent, with: ([INSpeakableStringResolutionResult]) -> Void)](./resolvetasktitles%28for,with%29.md)
  Resolves the tasks in a task list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/increatetasklistintenthandling/resolvegroupname(for:with:))*