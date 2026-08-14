# MSSticker

**Framework**: Messages  
**Kind**: class

A sticker that can be sent as a new message or attached to an existing balloon in the Messages app’s  transcript.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+

## Declaration

```swift
class MSSticker
```

## Mentions

- [Adding Sticker packs and iMessage apps to the system Stickers app, Messages camera, and FaceTime](adding-sticker-packs-and-imessage-apps-to-the-system-stickers-app-messages-camera-and-facetime.md)

## Topics

### Creating Stickers
- [init(contentsOfFileURL: URL, localizedDescription: String) throws](mssticker/init(contentsoffileurl:localizeddescription:).md)
  Initializes a sticker with the contents of the URL and the localized description.
### Reading Sticker Data
- [var imageFileURL: URL](mssticker/imagefileurl.md)
  The file URL of the image displayed by the sticker.
- [var localizedDescription: String](mssticker/localizeddescription.md)
  The sticker’s localized description.

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## See Also

- [class MSConversation](msconversation.md)
  An object that represents a conversation in the Messages app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/messages/mssticker)*