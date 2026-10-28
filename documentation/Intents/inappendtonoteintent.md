# INAppendToNoteIntent

**Framework**: Intents  
**Kind**: class  
**Role**: Class

A request to append content to a note.

**Availability**:
- iOS 11.0+ - Deprecated in 15.0
- iPadOS 11.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 4.0+ - Deprecated in 8.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

```swift
class INAppendToNoteIntent
```

```objc
@interface INAppendToNoteIntent : INIntent
```

## Overview

Siri creates an [`INAppendToNoteIntent`](./inappendtonoteintent.md) object when the user asks to append content to an existing note. The intent object contains the note to modify and the content to add to the note.

To handle this intent, the handler object in your Intents extension must adopt the [`INAppendToNoteIntentHandling`](./inappendtonoteintenthandling.md) protocol. Your handler should confirm the request and create an [`INAppendToNoteIntentResponse`](./inappendtonoteintentresponse.md) object with the updated note.

### Additional Intent Attributes

The following table lists additional attributes of this intent object:

| Attribute | Description |
| --- | --- |
| Supported by | Siri Intents |
| Always requires unlocked device | No |

If the resolution for any parameter requires disambiguation or confirmation, the user must unlock the device before you handle the intent. If resolution of the parameters doesn’t require user interaction, you can handle the intent without the user unlocking the device.

## Topics

### Initializing the Intent Object
- [init(targetNote: INNote?, content: INNoteContent?)](./inappendtonoteintent/init%28targetnote,content%29.md)
  Initializes the intent object with the specified note and content.
### Getting the Note Content
- [var content: INNoteContent?](./inappendtonoteintent/content.md)
  The content to append to the note.
- [var targetNote: INNote?](./inappendtonoteintent/targetnote.md)
  The note to receive the additional content.

## Relationships

### Inherits From
- [INIntent](./inintent.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [INIntentSetImageKeyPath](./inintentsetimagekeypath.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### Note Additions
- [protocol INAppendToNoteIntentHandling](./inappendtonoteintenthandling.md)
  The handler interface for appending content to a note.
- [class INAppendToNoteIntentResponse](./inappendtonoteintentresponse.md)
  Your app’s response to a request to append content to a note.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inappendtonoteintent)*