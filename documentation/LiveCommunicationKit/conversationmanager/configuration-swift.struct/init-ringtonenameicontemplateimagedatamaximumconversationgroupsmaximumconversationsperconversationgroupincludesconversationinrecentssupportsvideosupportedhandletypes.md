# init(ringtoneName:iconTemplateImageData:maximumConversationGroups:maximumConversationsPerConversationGroup:includesConversationInRecents:supportsVideo:supportedHandleTypes:)

**Framework**: LiveCommunicationKit  
**Kind**: init

Creates a new `Configuration`.

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

- `ringtoneName`: The name of the sound resource in the app bundle to be used for the provider ringtone.
- `iconTemplateImageData`: PNG data for the icon image to be displayed for the provider.
- `maximumConversationGroups`: The maximum number of  s groups.
- `maximumConversationsPerConversationGroup`: The maximum number of  s per   group.
- `includesConversationInRecents`: A Boolean value that indicates whether the provider includes a call in the system’s Recents list after the call ends.
- `supportsVideo`: A Boolean value that indicates whether the provider supports video in addition to audio.
- `supportedHandleTypes`: The supported handle types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/livecommunicationkit/conversationmanager/configuration-swift.struct/init(ringtonename:icontemplateimagedata:maximumconversationgroups:maximumconversationsperconversationgroup:includesconversationinrecents:supportsvideo:supportedhandletypes:))*