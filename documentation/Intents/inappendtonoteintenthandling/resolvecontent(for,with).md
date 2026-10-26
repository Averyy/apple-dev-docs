# resolveContent(for:with:)

**Framework**: Intents  
**Kind**: method  
**Role**: Instance Method

Resolves the content to append to the note.

**Availability**:
- iOS 11.0+ - Deprecated in 15.0
- iPadOS 11.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 4.0+ - Deprecated in 8.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

```swift
optional func resolveContent(for intent: INAppendToNoteIntent, with completion: @escaping @Sendable (INNoteContentResolutionResult) -> Void)
```

```swift
optional func resolveContent(for intent: INAppendToNoteIntent) async -> INNoteContentResolutionResult
```

```objc
- (void) resolveContentForAppendToNote:(INAppendToNoteIntent *) intent withCompletion:(void (^)(INNoteContentResolutionResult *resolutionResult)) completion;
```

#### Discussion

Implement this method to resolve the content to append to a note. Use the intent object to obtain the content specified by the user. If the intent doesn’t contain any content, you might want to prompt the user to specify a value.

## Parameters

- `intent`: The intent object containing details about the user’s request. Use this object to get the initial information, if any, provided by the user.
- `completion`: The handler block to execute with the resolution. You must execute this handler at some point during your implementation of this method. This handler has no return value and takes the following parameter:

  - **resolutionResult**: The object containing the details of your proposed resolution. For successful resolutions, create a resolution object with the text or image that you intend to append to the main content of the note.

## See Also

### Resolving the Intent Parameters
- [func resolveTargetNote(for: INAppendToNoteIntent, with: (INNoteResolutionResult) -> Void)](./resolvetargetnote%28for,with%29.md)
  Resolves the note that receives the new content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inappendtonoteintenthandling/resolvecontent(for:with:))*