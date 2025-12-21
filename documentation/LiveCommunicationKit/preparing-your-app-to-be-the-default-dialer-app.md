# Preparing your app to be the default dialer app

**Framework**: LiveCommunicationKit

Let people configure their device to set your app as the default dialer app.

#### Overview

In addition to adding VoIP calling to your app and preparing it to be the default calling app, LiveCommunicationKit allows you to prepare your app as the default dialer app that can start cellular network conversations:

- A default  app handles incoming and outgoing VoIP conversations, requiring VoIP conversation functionality, and uses LiveCommunicationKit or [`CallKit`](https://developer.apple.com/documentation/CallKit).
- A default  app uses LiveCommunicationKit and focuses on presenting a dialer interface as the default way for initiating cellular network conversations.

> ❗ **Important**: To use the [`StartCellularConversationAction`](startcellularconversationaction.md) and [`TelephonyConversationManager`](telephonyconversationmanager.md) API in LiveCommunicationKit, you must add the [`Default Dialer App`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.dialing-app) entitlement to your app. To test your app’s behavior as a default dialer app, your Apple Developer account needs to be registered in the European Union (EU), and the test device must be located within the EU.

As the default dialer app, people use your app to initiate a cellular network conversation immediately without a system prompt that asks them to confirm their intent. This behavior is different from apps that use [`CallKit`](https://developer.apple.com/documentation/CallKit), or an app that forwards a conversation to the system using a `telephony:` URL scheme. Additionally, your app can access the device’s conversation history, from the moment your app became the default dialer app, to allow people to quickly start a follow-up conversation from a previous inbound or outgoing conversation.

> **Note**: If your app includes the [`Default Dialer App`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.dialing-app) entitlement, your app can initiate a cellular network conversation with LiveCommunicationKit even if a person doesn’t also configure it as the default dialer app. However, the person has to confirm their intention to start the conversation with a confirmation dialog. If someone configures your app as the default dialer app, they don’t have to confirm their intent with a confirmation dialog.

When someone enters recipient information in the default dialer app to initiate a conversation, the app can handle cellular network conversations directly and either handle VoIP conversations itself or pass them to the system. For example:

- A cartoon app might add support for being the default dialer app to let people initiate conversations from a custom dialer UI with a cartoon theme. If someone enters a phone number, the app starts the cellular network conversation without a confirmation if it’s the configured default dialer app. The app’s dialer UI remains visible during the conversation. To allow people to initiate a VoIP conversation using an email address or other account information, the app forwards the conversation to the system.
- A VoIP conversation app might add support to be the default dialer app for a conversation experience that’s more integrated in the system. When someone enters a phone number, the app starts a cellular network conversation using LiveCommunicationKit. If the app is the configured default dialer app, the system doesn’t show a confirmation dialog. When a person initiates a VoIP conversation, the app handles the VoIP conversation as well. If the VoIP conversation fails, it attempts a cellular conversation using LiveCommunicationKit.

When an app forwards a conversation to the system using LiveCommunicationKit, the framework routes the conversation to the configured default calling app which attempts a VoIP conversation. If the VoIP conversation fails, the default calling app can fall back to the system, and the system attempts to handle the conversation as a cellular network conversation.

##### Add the Default Dialer App Entitlement

To prepare your app to be the default dialer app, add the `com.apple.developer.dialing-app` entitlement to the `.entitlements` file in your app’s Xcode project. For details on adding this entitlement, see [`Default Dialer App`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.dialing-app).

##### Start a Cellular Network Conversation

After adding the default dialer app entitlement, use LiveCommunicationKit to initiate a conversation. If your app doesn’t include VoIP conversation functionality, ask the system to start a conversation using the default calling app:

1. Create a [`Handle`](handle.md) for the conversation’s recipient.
2. Create a [`StartCellularConversationAction`](startcellularconversationaction.md) using the `Handle` and the [`CellularService`](cellularservice.md) to initiate the cellular network conversation.
3. Use the [`TelephonyConversationManager`](telephonyconversationmanager.md) and its [`startCellularConversation(_:)`](telephonyconversationmanager/startcellularconversation(_:).md) method to initiate a conversation.

By creating a `DialRequest` and initiating a conversation using the `TelephonyConversationManager`, you let the system route it to the right app. If a person configures their device to use a default calling app, the system launches that app to either handle a VoIP conversation or pass a cellular network conversation back to the system. If a person hasn’t configured a default calling app, the system handles the conversation as a cellular network conversation.

The following example shows a method for initiating a conversation with a `StartCellularConversationAction`:

```swift
// ...

let manager = TelephonyConversationManager.sharedInstance
let cellularServices = manager.cellularServices

// Code to choose a cellular service.
// ...

// Start a cellular network conversation.
func startCellularConversation(_ phoneNumber: String, using cellularService: CellularService? = nil) async throws {
    let handle = Handle(type: .phoneNumber, value: phoneNumber)
    do {
        let action = StartCellularConversationAction(handle, cellularService: cellularService)
        try await manager.startCellularConversation(action)
    } catch {
        print("error dialing \(error)")
        // ...
        // Additional error handling.

        throw error
    }
}
```

If your app includes VoIP conversation functionality, handle the VoIP conversation in your app. If the VoIP conversation fails, use `DialRequest` and `TelephonyConversationManager` as shown above to let the system pass the conversation to the configured default calling app. If a person didn’t configure a default calling app, the system handles the conversation as a cellular network conversation.

##### Access Recent Cellular Conversation History

If your app includes the [`Default Dialer App`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.dialing-app) entitlement and a person configures it as the default dialer app, your app can access recent conversation history. Displaying recent conversations in your app makes it easy for people to return missed conversations or follow up after a recent conversation. To access the conversation history, use [`ConversationHistoryManager`](conversationhistorymanager.md) to fetch recent conversations. To update your app’s interface to show recent changes to the conversation history, observe the [`ConversationHistoryManager.ConversationHistoryDidUpdate`](conversationhistorymanager/conversationhistorydidupdate.md) message as shown in the following example:

```swift
import Foundation
import LiveCommunicationKit

import Foundation
import LiveCommunicationKit

@Observable
class RecentConversationsViewModel {
    @MainActor var history: [ConversationHistoryManager.RecentConversation] = []
    let dataProvider = ConversationHistoryManager.sharedInstance
    var token: NotificationCenter.ObservationToken? = nil

    init() {
        fetchAndUpdateHistory()
        self.token = NotificationCenter.default.addObserver(of: ConversationHistoryManager.self, for: .conversationHistoryDidUpdateMessage) { _ in
            self.fetchAndUpdateHistory()
        }
    }

    private func fetchAndUpdateHistory() {
        Task {
            let predicate = #Predicate<ConversationHistoryManager.RecentConversation> { _ in true }
            do {
                let results = try await dataProvider.recentConversations(matching: predicate)
                await MainActor.run {
                    history = results
                }
            } catch {
                // Handle any errors.
                // ...
            }
        }
    }
}
```

## See Also

- [Initiating VoIP conversations with LiveCommunicationKit](initiating-voip-conversations-with-livecommunicationkit.md)
  Let people initiate and receive VoIP conversations, and configure your app so it can be the default calling app on a person’s device.
- [LiveCommunicationKit updates](../Updates/LiveCommunicationKit.md)
  Learn about important changes to LiveCommunicationKit.


---

*[View on Apple Developer](https://developer.apple.com/documentation/livecommunicationkit/preparing-your-app-to-be-the-default-dialer-app)*