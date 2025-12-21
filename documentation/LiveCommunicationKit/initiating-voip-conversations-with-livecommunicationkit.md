# Initiating VoIP conversations with LiveCommunicationKit

**Framework**: LiveCommunicationKit

Let people initiate and receive VoIP conversations, and configure your app so it can be the default calling app on a person’s device.

#### Overview

LiveCommunicationKit enables you to add VoIP capabilities to your app. For incoming and outgoing VoIP conversations, your app displays the same interface as the Phone app, responding appropriately to system-level behaviors, such as Do Not Disturb. Additionally, use LiveCommunicationKit to prepare your app to be the default dialer app, the default calling app, or both.

For more information, see [`Preparing your app to be the default dialer app`](preparing-your-app-to-be-the-default-dialer-app.md) and [`Review default calling app functionality`](initiating-voip-conversations-with-livecommunicationkit#Review-default-calling-app-functionality.md).

##### Start a Voip Conversation

With LiveCommunicationKit, handle VoIP conversations with your VoIP services:

1. Use [`ConversationManager`](conversationmanager.md) to perform conversation actions like [`StartConversationAction`](startconversationaction.md), [`EndConversationAction`](endconversationaction.md), and so on.
2. Implement the [`ConversationManagerDelegate`](conversationmanagerdelegate.md) requirements and respond to VoIP conversation updates.
3. Add code to use your VoIP conversation services.

The following example shows how a VoIP app might start a conversation:

```swift
    // ...

    let configuration: ConversationManager.Configuration
    let manager: ConversationManager

    // Code to set up the manager and configuration for the conversation.
    // ...

    // Start the conversation.
    func startOutgoingConversation(handles: [Handle], isVideo: Bool) async throws {
        let uuid = UUID()
        let action = StartConversationAction(
            conversationUUID: uuid,
            handles: handles,
            isVideo: isVideo
        )
        try await manager.perform([action])

        // Code to initiate a VoIP conversation using your VoIP services.
        // ...
        
        Task {
            try await Task.sleep(for: .seconds(1))
            for conversation in manager.conversations {
                if conversation.uuid == uuid {
                    // Report conversation status.
                    manager.reportConversationEvent(.conversationConnected(Date()), for: conversation)
                }
            }
        }
    }
```

In your `ConversationManagerDelegate` implementation, you can handle conversation events. For example, the conversation manager calls [`conversationManager(_:didActivate:)`](conversationmanagerdelegate/conversationmanager(_:didactivate:).md) when an audio session starts, allowing you to update your app’s UI to show information about the ongoing audio session.

##### Include a Fallback Option

If starting a VoIP conversation fails, you may wish to have the conversation fall back to the system to handle it. While optional, providing a fallback gives people another opportunity to have the conversation. When you let the conversation fall back to the system, the system passes it to the configured default calling app. If a person didn’t configure a default calling app or the default calling app hands the conversation back to the system, the system handles the conversation as a cellular network conversation.

If your app supports being the default dialer app, use [`StartCellularConversationAction`](startcellularconversationaction.md) and [`TelephonyConversationManager`](telephonyconversationmanager.md). For more information, see [`Start a cellular network conversation`](preparing-your-app-to-be-the-default-dialer-app#Start-a-cellular-network-conversation.md).

If your app doesn’t support being the default dialer app, use a `telephony://` URL scheme for your fallback. For more information, see [`Preparing your app to be the default calling app`](https://developer.apple.com/documentation/CallKit/Preparing-your-app-to-be-the-default-calling-app#Apply-the-fallback-URL-scheme-in-your-app).

##### Review Default Calling App Functionality

People may select another app — other than the Phone app or FaceTime — as the default calling app. Before someone can set your app as the default calling app on their device, your app needs to offer VoIP conversation functionality.

When your app receives a conversation as the system’s default calling app, it handles VoIP conversations and passes cellular network conversations to the system as a fallback. For example, when someone configures your app as the default calling app, tapping a telephone number or account in a contact card asks the person for permission to start a conversation using your app. Upon confirmation, your app receives the recipient’s number for the conversation and attempts a VoIP conversation. If the VoIP conversation fails, your app requests the system to handle the conversation as a cellular network conversation. For more information, see [`Include a fallback option`](initiating-voip-conversations-with-livecommunicationkit#Include-a-fallback-option.md).

## See Also

- [Preparing your app to be the default dialer app](preparing-your-app-to-be-the-default-dialer-app.md)
  Let people configure their device to set your app as the default dialer app.
- [LiveCommunicationKit updates](../Updates/LiveCommunicationKit.md)
  Learn about important changes to LiveCommunicationKit.


---

*[View on Apple Developer](https://developer.apple.com/documentation/livecommunicationkit/initiating-voip-conversations-with-livecommunicationkit)*