# init(targetNote:content:)

**Framework**: Intents  
**Kind**: init  
**Role**: Initializer

Initializes the intent object with the specified note and content.

**Availability**:
- iOS 11.0+ - Deprecated in 15.0
- iPadOS 11.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 4.0+ - Deprecated in 8.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

```swift
init(targetNote: INNote?, content: INNoteContent?)
```

```objc
- (instancetype) initWithTargetNote:(INNote *) targetNote content:(INNoteContent *) content;
```

#### Return Value

An initialized intent object or `nil` if the object could not be created.

#### Discussion

Normally, you don’t create instances of this class yourself. Instead, SiriKit creates instances when the user asks to append content to a note. However, you can use this method during testing to create intent objects in order to validate your intent handling code paths.

## Parameters

- `targetNote`: The note to receive the additional content.
- `content`: The content to add to the note. You may specify text or image content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inappendtonoteintent/init(targetnote:content:))*