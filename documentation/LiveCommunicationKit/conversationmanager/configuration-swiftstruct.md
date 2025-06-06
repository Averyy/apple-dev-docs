# ConversationManager.Configuration

**Framework**: LiveCommunicationKit  
**Kind**: struct

An encapsulation of the configuration of a `ConversationManager`.

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
  Creates a new `Configuration`.
### Instance Properties
- [var iconTemplateImageData: Data?](conversationmanager/configuration-swift.struct/icontemplateimagedata.md)
  PNG data for the icon image to be displayed for the provider.
- [var includesConversationInRecents: Bool](conversationmanager/configuration-swift.struct/includesconversationinrecents.md)
  A Boolean value that indicates whether the provider includes a call in the system’s Recents list after the call ends.
- [var maximumConversationGroups: Int](conversationmanager/configuration-swift.struct/maximumconversationgroups.md)
  The maximum number of `Conversation`s groups.
- [var maximumConversationsPerConversationGroup: Int](conversationmanager/configuration-swift.struct/maximumconversationsperconversationgroup.md)
  The maximum number of `Conversation`s per `Conversation` group.
- [var ringtoneName: String?](conversationmanager/configuration-swift.struct/ringtonename.md)
  The name of the sound resource in the app bundle to be used for the provider ringtone.
- [var supportedHandleTypes: Set<Handle.Kind>](conversationmanager/configuration-swift.struct/supportedhandletypes.md)
  The supported handle types.
- [var supportsVideo: Bool](conversationmanager/configuration-swift.struct/supportsvideo.md)
  A Boolean value that indicates whether the provider supports video in addition to audio.


---

*[View on Apple Developer](https://developer.apple.com/documentation/livecommunicationkit/conversationmanager/configuration-swift.struct)*