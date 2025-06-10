# Preparing your app to be the default dialer app

**Framework**: LiveCommunicationKit

Let people configure their device to set your app as the default dialer app.

#### Overview

In addition to adding VoIP calling to your app and preparing it to be the default calling app, LiveCommunicationKit allows you to prepare your app as the default dialer app.

- Default  apps handle incoming and outgoing VoIP conversations, requiring VoIP conversation functionality.
- Default  apps focus on presenting a dialer interface as the default way for initiating VoIP and cellular network conversations.

> ❗ **Important**: To use the [`DialRequest`](dialrequest.md) and [`TelephonyManager`](telephonymanager.md) API in LiveCommunicationKit, you must add the [`Default Dialer App`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.dialing-app) entitlement to your app. To test your app’s behavior as a default dialer app, your Apple Developer account needs to be registered in the European Union (EU), and the test device must be located within the EU.

As the default dialer app, your app can initiate a conversation immediately without a system prompt that asks them to confirm their intent. This behavior is different from apps that use [`CallKit`](https://developer.apple.com/documentation/CallKit), or an app that forwards a conversation to the system using a `telephony:` URL scheme. Additionally, your app can access the device’s conversation history, from the moment your app became the default dialer app, and allow people to quickly start a follow-up conversation from a past conversation.

When someone enters recipient information in the default dialer app to initiate a conversation, the app can either handle the VoIP conversation itself or pass it to the system. For example:

- A cartoon app might add support for being the default dialer app to let people initiate conversations from a custom dialer UI with a cartoon theme. The app becomes their primary way to initiate any conversation. However, the app doesn’t offer VoIP functionality itself. Instead, it uses LiveCommunicationKit to forward the conversation to the system.
- A VoIP conversation app might add support to be the default dialer app for a conversation experience that’s more integrated in the system by allowing people to dial any recipient without a confirmation prompt and showing conversation history. If a person initiates a VoIP conversation, the app itself handles the conversation. If the VoIP conversation fails or is not possible, it forwards the conversation to the system using LiveCommunicationKit.

When an app forwards a conversation to the system using LiveCommunicationKit, the framework routes the conversation to the configured default calling app. If the person configured a default calling app, that default calling app might attempt a VoIP conversation. If the VoIP conversation fails, the default calling app can fall back to the system, and the system handles the conversation as a cellular network conversation.

##### Add the Default Dialer App Entitlement

To prepare your app to be the default dialer app, add the `com.apple.developer.dialing-app` entitlement to the `.entitlements` file in your app’s Xcode project. For details on adding this entitlement, see [`Default Dialer App`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.dialing-app).

##### Request the System to Start a Conversation

After adding the default dialer app entitlement, use LiveCommunicationKit to initiate a conversation. If your app doesn’t include VoIP conversation functionality, ask the system to start a conversation using the default calling app:

1. Create a [`Handle`](handle.md) for the conversation’s recipient.
2. Create a [`DialRequest`](dialrequest.md) using the `Handle` and the [`Account`](account.md) to initiate the conversation.
3. Use the [`TelephonyManager`](telephonymanager.md) and its [`dial(request:)`](telephonymanager/dial(request:).md) method to initiate a conversation.

By creating a `DialRequest` and initiating a conversation using the `TelephonyManager`, you let the system route it to the right app. If a person configures their device to use a default calling app, the system launches that app to either handle a VoIP conversation or pass a cellular network conversation back to the system. If a person hasn’t configured a default calling app, the system handles the conversation as a cellular network conversation.

The following example shows a method for initiating a conversation with `DialRequest`:

```swift
    public func dial(_ phoneNumber: String, using account: Account? = nil) {
        Task {
            let handle = Handle(type: .phoneNumber, value: phoneNumber, displayName: nil)
            do {
                let request = DialRequest(handle: handle, account: account)
                let dialer = TelephonyManager()
                try await dialer.dial(request: request)
            } catch {
                print("error dialing \(error)")
                // Additional error handling.
            }
        }
    }
```

If your app includes VoIP conversation functionality, handle the VoIP conversation. If the VoIP conversation fails, use `DialRequest` and `TelephonyManager` as shown above to let the system pass the conversation to the configured default calling app. If a person didn’t configure a default calling app, the system handles the conversation as a cellular network conversation.

##### Access Recent Conversation History

If your app includes the [`Default Dialer App`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.dialing-app) entitlement and a person configures it as the default dialer app, your app can access recent conversation history. Displaying recent conversations in your app makes it easy for people to return missed conversations or follow up after a recent conversation. To access the conversation history, use [`ConversationHistoryManager`](conversationhistorymanager.md) to fetch recent conversations and receive updates about recent conversations, such as missed conversations.

The following example shows a class that implements the [`ConversationHistoryManagerDelegate`](conversationhistorymanagerdelegate.md) protocol to receive updates about recent conversations:

```swift
import Foundation
import LiveCommunicationKit

@Observable
class HistoryViewModel: ConversationHistoryManagerDelegate {
    func conversationHistoryManagerDidUpdate(_ manager: LiveCommunicationKit.ConversationHistoryManager) {
        fetchAndUpdateHistory()
    }

    let dataProvider = ConversationHistoryManager()

    @MainActor var history: [ConversationHistoryManager.RecentConversation] = []

    public init() {
        dataProvider.addDelegate(delegate: self)
        fetchAndUpdateHistory()
    }

    private func fetchAndUpdateHistory() {
        Task {
            let predicate = #Predicate<ConversationHistoryManager.RecentConversation> { _ in true }
            do {
                let results = try await dataProvider.fetch(request: predicate)
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