# INNote

**Framework**: Intents  
**Kind**: class  
**Role**: Class

The content and metadata associated with a single note entry in your app.

**Availability**:
- iOS 11.0+ - Deprecated in 27.0
- iPadOS 11.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0
- watchOS 4.0+ - Deprecated in 27.0

> **Deprecated**: INNote is deprecated. Please adopt the Notes or Reminders AppSchema domain instead.

## Declaration

```swift
class INNote
```

```objc
@interface INNote : NSObject
```

## Overview

When SiriKit asks you to create a note, use an instance of this class to specify the contents of the note.

## Topics

### Initializing a Note Object
- [init(title: INSpeakableString, contents: [INNoteContent], groupName: INSpeakableString?, createdDateComponents: DateComponents?, modifiedDateComponents: DateComponents?, identifier: String?)](./innote/init%28title,contents,groupname,createddatecomponents,modifieddatecomponents,identifier%29.md)
  Initializes a note object with the specified contents and attributes.
### Getting the Note Content
- [var title: INSpeakableString](./innote/title.md)
  The title text for the note.
- [var contents: [INNoteContent]](./innote/contents.md)
  The main content of the note.
### Getting the Group Name
- [var groupName: INSpeakableString?](./innote/groupname.md)
  The user-visible name of the group that contains the note.
### Getting the Modification Dates
- [var createdDateComponents: DateComponents?](./innote/createddatecomponents.md)
  The creation date of the note.
- [var modifiedDateComponents: DateComponents?](./innote/modifieddatecomponents.md)
  The date on which the intent most recently modified the note.
### Identifying the Note
- [var identifier: String?](./innote/identifier.md)
  The unique identifier that you use to identify the note internally.
### Initializers
- [init?(coder: NSCoder)](./innote/init%28coder%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### Note Objects
- [class INNoteContent](./innotecontent.md)
  An abstract class that defines the types of content contained in notes.
- [class INTextNoteContent](./intextnotecontent.md)
  The textual content of a note.
- [class INImageNoteContent](./inimagenotecontent.md)
  An image contained in a note.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/innote)*