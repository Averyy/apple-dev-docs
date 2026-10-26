# resolveContent(for:with:)

**Framework**: Intents  
**Kind**: method  
**Role**: Instance Method

Resolves the main content of the note.

**Availability**:
- iOS 11.0+ - Deprecated in 27.0
- iPadOS 11.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0
- watchOS 4.0+ - Deprecated in 27.0

> **Deprecated**: INCreateNoteIntentHandling is deprecated. Please adopt the Notes or Reminders AppSchema domain instead.

## Declaration

```swift
optional func resolveContent(for intent: INCreateNoteIntent, with completion: @escaping @Sendable (INNoteContentResolutionResult) -> Void)
```

```swift
optional func resolveContent(for intent: INCreateNoteIntent) async -> INNoteContentResolutionResult
```

```objc
- (void) resolveContentForCreateNote:(INCreateNoteIntent *) intent withCompletion:(void (^)(INNoteContentResolutionResult *resolutionResult)) completion;
```

#### Discussion

Implement this method to resolve the main contnet for a note. Use the intent object to obtain the content specified by the user. If the intent does not contain any content, you might want to prompt the user to specify a value. However, if there is a note title and it is sufficient for creating the note, you can also return a result indicating that a value for the content is not required.

## Parameters

- `intent`: The intent object containing details about the user’s request. Use this object to get the initial information, if any, provided by the user.
- `completion`: The handler block to execute with the resolution. You must execute this handler at some point during your implementation of this method. This handler has no return value and takes the following parameter:

  - **resolutionResult**: The object containing the details of your proposed resolution. For successful resolutions, create a resolution object with the text or image that you intend to use as the main content of the note.

## See Also

### Resolving the Intent Parameters
- [func resolveTitle(for: INCreateNoteIntent, with: (INSpeakableStringResolutionResult) -> Void)](./resolvetitle%28for,with%29.md)
  Resolves the title of the note.
- [func resolveGroupName(for: INCreateNoteIntent, with: (INSpeakableStringResolutionResult) -> Void)](./resolvegroupname%28for,with%29.md)
  Resolves the intended group of the note.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/increatenoteintenthandling/resolvecontent(for:with:))*