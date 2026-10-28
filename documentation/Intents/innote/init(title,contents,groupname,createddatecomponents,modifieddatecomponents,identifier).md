# init(title:contents:groupName:createdDateComponents:modifiedDateComponents:identifier:)

**Framework**: Intents  
**Kind**: init  
**Role**: Initializer

Initializes a note object with the specified contents and attributes.

**Availability**:
- iOS 11.0+ - Deprecated in 27.0
- iPadOS 11.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0
- watchOS 4.0+ - Deprecated in 27.0

> **Deprecated**: INNote is deprecated. Please adopt the Notes or Reminders AppSchema domain instead.

## Declaration

```swift
init(title: INSpeakableString, contents: [INNoteContent], groupName: INSpeakableString?, createdDateComponents: DateComponents?, modifiedDateComponents: DateComponents?, identifier: String?)
```

```objc
- (instancetype) initWithTitle:(INSpeakableString *) title contents:(NSArray<INNoteContent *> *) contents groupName:(INSpeakableString *) groupName createdDateComponents:(NSDateComponents *) createdDateComponents modifiedDateComponents:(NSDateComponents *) modifiedDateComponents identifier:(NSString *) identifier;
```

## Return Value

An initialized note object or `nil` if the object could not be created.

## Parameters

- `title`: The title text for the note. This string represents the initial text that users see for the note in your interface.
- `contents`: The main content of the note. Use this parameter to specify the text and images that the note contains.
- `groupName`: The container in which the note resides. For example, if your app organizes notes into named folders, use this property to specify the name of the folder.
- `createdDateComponents`: The date on which the note was created.
- `modifiedDateComponents`: The date on which the note was last modified.
- `identifier`: A unique identifier that you associate with the note internally.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/innote/init(title:contents:groupname:createddatecomponents:modifieddatecomponents:identifier:))*