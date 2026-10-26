# resolveGroupName(for:with:)

**Framework**: Intents  
**Kind**: method  
**Role**: Instance Method

Resolves the intended group of the note.

**Availability**:
- iOS 11.0+ - Deprecated in 27.0
- iPadOS 11.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0
- watchOS 4.0+ - Deprecated in 27.0

> **Deprecated**: INCreateNoteIntentHandling is deprecated. Please adopt the Notes or Reminders AppSchema domain instead.

## Declaration

```swift
optional func resolveGroupName(for intent: INCreateNoteIntent, with completion: @escaping @Sendable (INSpeakableStringResolutionResult) -> Void)
```

```swift
optional func resolveGroupName(for intent: INCreateNoteIntent) async -> INSpeakableStringResolutionResult
```

```objc
- (void) resolveGroupNameForCreateNote:(INCreateNoteIntent *) intent withCompletion:(void (^)(INSpeakableStringResolutionResult *resolutionResult)) completion;
```

#### Discussion

Implement this method to resolve the intended group for the note. Use the intent object to obtain the group information, if any, specified by the user. Groups are a way for you to organize the notes of your app. For example, the Notes app provides a group for the services, such as iCloud, that manage notes.

If the intent does not contain a group name, choose a resolution that is most appropriate for your app. If your app does not support organizing notes into groups, you might return a result indicating that the group name is not required. If you are able to select a default group for the note, create a successful resolution that includes the name of the group you selected.

## Parameters

- `intent`: The intent object containing details about the user’s request. Use this object to get the initial information, if any, provided by the user.
- `completion`: The handler block to execute with the resolution. You must execute this handler at some point during your implementation of this method. This handler has no return value and takes the following parameter:

  - **resolutionResult**: The object containing the details of your proposed resolution. For successful resolutions, create a resolution object with the name of the group in which you intend to place the note.

## See Also

### Resolving the Intent Parameters
- [func resolveTitle(for: INCreateNoteIntent, with: (INSpeakableStringResolutionResult) -> Void)](./resolvetitle%28for,with%29.md)
  Resolves the title of the note.
- [func resolveContent(for: INCreateNoteIntent, with: (INNoteContentResolutionResult) -> Void)](./resolvecontent%28for,with%29.md)
  Resolves the main content of the note.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/increatenoteintenthandling/resolvegroupname(for:with:))*