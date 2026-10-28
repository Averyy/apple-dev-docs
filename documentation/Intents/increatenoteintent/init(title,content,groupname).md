# init(title:content:groupName:)

**Framework**: Intents  
**Kind**: init  
**Role**: Initializer

Initializes the intent object with the specified note content.

**Availability**:
- iOS 11.0+ - Deprecated in 27.0
- iPadOS 11.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0
- watchOS 4.0+ - Deprecated in 27.0

> **Deprecated**: INCreateNoteIntent is deprecated. Please adopt the Notes or Reminders AppSchema domain instead.

## Declaration

```swift
init(title: INSpeakableString?, content: INNoteContent?, groupName: INSpeakableString?)
```

```objc
- (instancetype) initWithTitle:(INSpeakableString *) title content:(INNoteContent *) content groupName:(INSpeakableString *) groupName;
```

## Return Value

An initialized intent object or `nil` if the object could not be created.

## Discussion

Normally, you don’t create instances of this class yourself. Instead, SiriKit creates instances when the user asks to create a note. However, you can use this method during testing to create intent objects in order to validate your intent handling code paths.

## Parameters

- `title`: The title text to apply to the note.
- `content`: The content of the note.
- `groupName`: The name of the group in which to store the note. Group names correspond to folders or other means of organizing notes within your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/increatenoteintent/init(title:content:groupname:))*