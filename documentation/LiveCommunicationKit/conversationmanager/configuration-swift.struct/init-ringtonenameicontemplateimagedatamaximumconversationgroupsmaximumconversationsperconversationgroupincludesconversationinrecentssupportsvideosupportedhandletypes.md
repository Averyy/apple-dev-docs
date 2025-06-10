# init(ringtoneName:iconTemplateImageData:maximumConversationGroups:maximumConversationsPerConversationGroup:includesConversationInRecents:supportsVideo:supportedHandleTypes:)

**Framework**: LiveCommunicationKit  
**Kind**: init

Creates a new configuration for a conversation manager.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- visionOS 1.1+
- watchOS 10.4+

## Declaration

```swift
init(ringtoneName: String?, iconTemplateImageData: Data?, maximumConversationGroups: Int, maximumConversationsPerConversationGroup: Int, includesConversationInRecents: Bool, supportsVideo: Bool, supportedHandleTypes: Set<Handle.Kind>)
```

## Parameters

- `ringtoneName`: The name of the sound resource in the app bundle for your app’s ringtone.
- `iconTemplateImageData`: The PNG data for the icon image of your app.
- `maximumConversationGroups`: The maximum number of conversation groups.
- `maximumConversationsPerConversationGroup`: The maximum number of conversations per conversation group.
- `includesConversationInRecents`: A Boolean value that indicates whether your app includes a conversation in the system’s Recents list after the conversation ends.
- `supportsVideo`: A Boolean value that indicates whether your app supports video in addition to audio.
- `supportedHandleTypes`: The supported handle types.

## See Also

- [init(ringtoneName: String?, iconTemplateImageData: Data?, maximumConversationGroups: Int, maximumConversationsPerConversationGroup: Int, includesConversationInRecents: Bool, supportsVideo: Bool, supportedHandleTypes: Set<Handle.Kind>, supportsAudioTranslation: Bool)](conversationmanager/configuration-swift.struct/init(ringtonename:icontemplateimagedata:maximumconversationgroups:maximumconversationsperconversationgroup:includesconversationinrecents:supportsvideo:supportedhandletypes:supportsaudiotranslation:).md)
  Creates a new configuration for a conversation manager.


---

*[View on Apple Developer](https://developer.apple.com/documentation/livecommunicationkit/conversationmanager/configuration-swift.struct/init(ringtonename:icontemplateimagedata:maximumconversationgroups:maximumconversationsperconversationgroup:includesconversationinrecents:supportsvideo:supportedhandletypes:))*