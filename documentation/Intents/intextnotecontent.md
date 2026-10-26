# INTextNoteContent

**Framework**: Intents  
**Kind**: class  
**Role**: Class

The textual content of a note.

**Availability**:
- iOS 11.0+ - Deprecated in 27.0
- iPadOS 11.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0
- watchOS 4.0+ - Deprecated in 27.0

> **Deprecated**: INTextNoteContent is deprecated. Please adopt the Notes or Reminders AppSchema domain instead.

## Declaration

```swift
class INTextNoteContent
```

```objc
@interface INTextNoteContent : INNoteContent
```

## Topics

### Initializing the Text Note
- [init(text: String)](./intextnotecontent/init%28text%29.md)
  Initializes a text-based note with the specified content.
### Getting the Note Text
- [var text: String?](./intextnotecontent/text.md)
  Text from the main content of the note.

## Relationships

### Inherits From
- [INNoteContent](./innotecontent.md)
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
- [class INNote](./innote.md)
  The content and metadata associated with a single note entry in your app.
- [class INNoteContent](./innotecontent.md)
  An abstract class that defines the types of content contained in notes.
- [class INImageNoteContent](./inimagenotecontent.md)
  An image contained in a note.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/intextnotecontent)*