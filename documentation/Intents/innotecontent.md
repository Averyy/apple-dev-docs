# INNoteContent

**Framework**: Intents  
**Kind**: class  
**Role**: Class

An abstract class that defines the types of content contained in notes.

**Availability**:
- iOS 11.0+ - Deprecated in 27.0
- iPadOS 11.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0
- watchOS 4.0+ - Deprecated in 27.0

> **Deprecated**: INNoteContent is deprecated. Please adopt the Notes or Reminders AppSchema domain instead.

## Declaration

```swift
class INNoteContent
```

```objc
@interface INNoteContent : NSObject
```

## Overview

You don’t create instances of this class directly. Instead, you create instances of the [`INTextNoteContent`](./intextnotecontent.md) or [`INImageNoteContent`](./inimagenotecontent.md) subclasses.

## Topics

### Initializers
- [init?(coder: NSCoder)](./innotecontent/init%28coder%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Inherited By
- [INImageNoteContent](./inimagenotecontent.md)
- [INTextNoteContent](./intextnotecontent.md)
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
- [class INTextNoteContent](./intextnotecontent.md)
  The textual content of a note.
- [class INImageNoteContent](./inimagenotecontent.md)
  An image contained in a note.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/innotecontent)*