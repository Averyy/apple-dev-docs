# init(conversationID:isTranslating:localLanguage:remoteLanguage:)

**Framework**: LiveCommunicationKit  
**Kind**: init

Creates an action that starts or stops translation.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Declaration

```swift
init(conversationID: UUID, isTranslating: Bool, localLanguage: Locale.Language, remoteLanguage: Locale.Language)
```

## Parameters

- `conversationID`: The unique identifier for a conversation.
- `isTranslating`: A value that indicates whether translation is active or paused.
- `localLanguage`: The local participant’s language.
- `remoteLanguage`: The remote participant’s language.


---

*[View on Apple Developer](https://developer.apple.com/documentation/livecommunicationkit/settranslatingaction/init(conversationid:istranslating:locallanguage:remotelanguage:))*