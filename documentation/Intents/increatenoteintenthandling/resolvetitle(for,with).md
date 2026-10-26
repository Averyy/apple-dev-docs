# resolveTitle(for:with:)

**Framework**: Intents  
**Kind**: method  
**Role**: Instance Method

Resolves the title of the note.

**Availability**:
- iOS 11.0+ - Deprecated in 27.0
- iPadOS 11.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0
- watchOS 4.0+ - Deprecated in 27.0

> **Deprecated**: INCreateNoteIntentHandling is deprecated. Please adopt the Notes or Reminders AppSchema domain instead.

## Declaration

```swift
optional func resolveTitle(for intent: INCreateNoteIntent, with completion: @escaping @Sendable (INSpeakableStringResolutionResult) -> Void)
```

```swift
optional func resolveTitle(for intent: INCreateNoteIntent) async -> INSpeakableStringResolutionResult
```

```objc
- (void) resolveTitleForCreateNote:(INCreateNoteIntent *) intent withCompletion:(void (^)(INSpeakableStringResolutionResult *resolutionResult)) completion;
```

#### Discussion

Implement this method to resolve the title for a note. Use the intent object to obtain the title, if any, suggested by the user. The title represents the initial text that users see for the note.

If the intent does not contain title information, choose a resolution that is most appropriate for your app. If you can extract the title information from the note’s content, return a result of success with the title string you extracted. Otherwise, you can return a result of not required if you do not require a title.

## Parameters

- `intent`: The intent object containing details about the user’s request. Use this object to get the initial information, if any, provided by the user.
- `completion`: The handler block to execute with the resolution. You must execute this handler at some point during your implementation of this method. This handler has no return value and takes the following parameter:

  - **resolutionResult**: The object containing the details of your proposed resolution. For successful resolutions, create a resolution object with the title text that you intend to use for the note.

## See Also

### Resolving the Intent Parameters
- [func resolveContent(for: INCreateNoteIntent, with: (INNoteContentResolutionResult) -> Void)](./resolvecontent%28for,with%29.md)
  Resolves the main content of the note.
- [func resolveGroupName(for: INCreateNoteIntent, with: (INSpeakableStringResolutionResult) -> Void)](./resolvegroupname%28for,with%29.md)
  Resolves the intended group of the note.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/increatenoteintenthandling/resolvetitle(for:with:))*