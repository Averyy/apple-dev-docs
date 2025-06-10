# ConversationManager.Configuration

**Framework**: LiveCommunicationKit  
**Kind**: struct

Configuration options for a conversation manager.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- visionOS 1.1+
- watchOS 10.4+

## Declaration

```swift
struct Configuration
```

## Topics

### Initializers
- [init(ringtoneName: String?, iconTemplateImageData: Data?, maximumConversationGroups: Int, maximumConversationsPerConversationGroup: Int, includesConversationInRecents: Bool, supportsVideo: Bool, supportedHandleTypes: Set<Handle.Kind>)](conversationmanager/configuration-swift.struct/init(ringtonename:icontemplateimagedata:maximumconversationgroups:maximumconversationsperconversationgroup:includesconversationinrecents:supportsvideo:supportedhandletypes:).md)
  Creates a new configuration for a conversation manager.
- [init(ringtoneName: String?, iconTemplateImageData: Data?, maximumConversationGroups: Int, maximumConversationsPerConversationGroup: Int, includesConversationInRecents: Bool, supportsVideo: Bool, supportedHandleTypes: Set<Handle.Kind>, supportsAudioTranslation: Bool)](conversationmanager/configuration-swift.struct/init(ringtonename:icontemplateimagedata:maximumconversationgroups:maximumconversationsperconversationgroup:includesconversationinrecents:supportsvideo:supportedhandletypes:supportsaudiotranslation:).md)
  Creates a new configuration for a conversation manager.
### Configuration options
- [var iconTemplateImageData: Data?](conversationmanager/configuration-swift.struct/icontemplateimagedata.md)
  The PNG data for the icon image of the app.
- [var includesConversationInRecents: Bool](conversationmanager/configuration-swift.struct/includesconversationinrecents.md)
  A Boolean value that indicates whether your app includes a conversation in the system’s Recents list after the conversation ends.
- [var maximumConversationGroups: Int](conversationmanager/configuration-swift.struct/maximumconversationgroups.md)
  The maximum number of conversation groups.
- [var maximumConversationsPerConversationGroup: Int](conversationmanager/configuration-swift.struct/maximumconversationsperconversationgroup.md)
  The maximum number of conversations per conversation group.
- [var ringtoneName: String?](conversationmanager/configuration-swift.struct/ringtonename.md)
  The name of the sound resource in the app bundle for the app’s ringtone.
- [var supportedHandleTypes: Set<Handle.Kind>](conversationmanager/configuration-swift.struct/supportedhandletypes.md)
  The supported handle types.
- [var supportsAudioTranslation: Bool](conversationmanager/configuration-swift.struct/supportsaudiotranslation.md)
  A Boolean value that indicates whether the app supports real-time audio translation.
- [var supportsVideo: Bool](conversationmanager/configuration-swift.struct/supportsvideo.md)
  A Boolean value that indicates whether the app supports video in addition to audio.

## See Also

- [convenience init(configuration: ConversationManager.Configuration)](conversationmanager/init(configuration:).md)
  Creates a new conversation manager with a given conversation.
- [let configuration: ConversationManager.Configuration](conversationmanager/configuration-swift.property.md)
  The configuration of a conversation manager.


---

*[View on Apple Developer](https://developer.apple.com/documentation/livecommunicationkit/conversationmanager/configuration-swift.struct)*