# resolveTargetNote(for:with:)

**Framework**: Intents  
**Kind**: method  
**Role**: Instance Method

Resolves the note that receives the new content.

**Availability**:
- iOS 11.0+ - Deprecated in 15.0
- iPadOS 11.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 4.0+ - Deprecated in 8.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

```swift
optional func resolveTargetNote(for intent: INAppendToNoteIntent, with completion: @escaping @Sendable (INNoteResolutionResult) -> Void)
```

```swift
optional func resolveTargetNote(for intent: INAppendToNoteIntent) async -> INNoteResolutionResult
```

```objc
- (void) resolveTargetNoteForAppendToNote:(INAppendToNoteIntent *) intent withCompletion:(void (^)(INNoteResolutionResult *resolutionResult)) completion;
```

## Discussion

Implement this method to resolve which note receives new content. Use the intent object to identify which note the user wants to modify. If the intent doesn’t identify a specific note, you might want to prompt the user to specify a value or you might indicate success and select a default note.

## Parameters

- `intent`: The intent object containing details about the user’s request. Use this object to get the initial information, if any, provided by the user.
- `completion`: The handler block to execute with the resolution. You must execute this handler at some point during your implementation of this method. This handler has no return value and takes the following parameter:

  - **resolutionResult**: The object containing the details of your proposed resolution. For successful resolutions, create a resolution object with the [`INNote`](../innote.md) object containing the content that you intend to modify.

## See Also

### Resolving the Intent Parameters
- [func resolveContent(for: INAppendToNoteIntent, with: (INNoteContentResolutionResult) -> Void)](./resolvecontent%28for,with%29.md)
  Resolves the content to append to the note.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inappendtonoteintenthandling/resolvetargetnote(for:with:))*