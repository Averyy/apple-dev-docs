# MSSticker

**Framework**: Messages  
**Kind**: class  
**Role**: Class

A sticker that can be sent as a new message or attached to an existing balloon in the Messages app’s  transcript.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+

## Declaration

```swift
class MSSticker
```

```objc
@interface MSSticker : NSObject
```

## Mentions

- [Adding Sticker packs and iMessage apps to the system Stickers app, Messages camera, and FaceTime](./adding-sticker-packs-and-imessage-apps-to-the-system-stickers-app-messages-camera-and-facetime.md)

## Topics

### Creating Stickers
- [init(contentsOfFileURL: URL, localizedDescription: String) throws](./mssticker/init%28contentsoffileurl,localizeddescription%29.md)
  Initializes a sticker with the contents of the URL and the localized description.
### Reading Sticker Data
- [var imageFileURL: URL](./mssticker/imagefileurl.md)
  The file URL of the image displayed by the sticker.
- [var localizedDescription: String](./mssticker/localizeddescription.md)
  The sticker’s localized description.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Message content
- [class MSConversation](./msconversation.md)
  An object that represents a conversation in the Messages app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/messages/mssticker)*