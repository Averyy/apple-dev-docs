# reportNewIncomingVoIPPushPayload(_:completion:)

**Framework**: CallKit  
**Kind**: method

Reports a new incoming call after your notification service extension decrypts a VoIP call request.

**Availability**:
- iOS 14.5+
- iPadOS 14.5+
- Mac Catalyst 14.5+
- visionOS 1.0+

## Declaration

```swift
class func reportNewIncomingVoIPPushPayload(_ dictionaryPayload: [AnyHashable : Any]) async throws
```

## Mentions

- [Sending End-to-End Encrypted VoIP Calls](sending-end-to-end-encrypted-voip-calls.md)

#### Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration: ```swift
class func reportNewIncomingVoIPPushPayload(_ dictionaryPayload: [AnyHashable : Any]) async throws
``` For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

 You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration:

```swift
class func reportNewIncomingVoIPPushPayload(_ dictionaryPayload: [AnyHashable : Any]) async throws
```

For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

Call this method when your notification service extension receives an encrypted VoIP call request. The system then launches your app and calls your [`pushRegistry(_:didReceiveIncomingPushWith:for:completion:)`](https://developer.apple.com/documentation/PushKit/PKPushRegistryDelegate/pushRegistry(_:didReceiveIncomingPushWith:for:completion:)) method. From this point, the app handles the call just like any incoming VoIP call. For more information, see [`Sending End-to-End Encrypted VoIP Calls`](sending-end-to-end-encrypted-voip-calls.md).

To call this method, your notification service extension must have the [`com.apple.developer.usernotifications.filtering`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.usernotifications.filtering) entitlement.

> ❗ **Important**:  Only call this method when your server can’t determine whether an outgoing notification is a request for a VoIP call or some other data (such as a text message) due to metadata encryption. If your server knows that the outgoing content is a VoIP call, send a [`voIP`](https://developer.apple.com/documentation/PushKit/PKPushType/voIP) push notification instead. For more information, see [`PushKit`](https://developer.apple.com/documentation/PushKit).

 Only call this method when your server can’t determine whether an outgoing notification is a request for a VoIP call or some other data (such as a text message) due to metadata encryption. If your server knows that the outgoing content is a VoIP call, send a [`voIP`](https://developer.apple.com/documentation/PushKit/PKPushType/voIP) push notification instead. For more information, see [`PushKit`](https://developer.apple.com/documentation/PushKit).

## Parameters

- `dictionaryPayload`: A dictionary containing additional data about the incoming call. All keys and values in the dictionary must implement the   protocol.
- `completion`: A block that CallKit executes after allowing or disallowing the call. CallKit executes the block on a private serial queue. The completion handler takes the following parameter:

## See Also

- [func reportNewIncomingCall(with: UUID, update: CXCallUpdate, completion: ((any Error)?) -> Void)](cxprovider/reportnewincomingcall(with:update:completion:).md)
  Reports a new incoming call with the specified unique identifier to the provider.
- [com.apple.developer.usernotifications.filtering](../BundleResources/Entitlements/com.apple.developer.usernotifications.filtering.md)
  Enable receiving notifications without displaying the notification to the user.
- [func reportOutgoingCall(with: UUID, startedConnectingAt: Date?)](cxprovider/reportoutgoingcall(with:startedconnectingat:).md)
  Reports to the provider that an outgoing call with the specified unique identifier started connecting at a particular time.
- [func reportOutgoingCall(with: UUID, connectedAt: Date?)](cxprovider/reportoutgoingcall(with:connectedat:).md)
  Reports to the provider that an outgoing call with the specified unique identifier finished connecting at a particular time.
- [func reportCall(with: UUID, updated: CXCallUpdate)](cxprovider/reportcall(with:updated:).md)
  Reports to the provider that an active call updated its information.
- [func reportCall(with: UUID, endedAt: Date?, reason: CXCallEndedReason)](cxprovider/reportcall(with:endedat:reason:).md)
  Reports to the provider that a call with the specified identifier ended at a given date for a particular reason.


---

*[View on Apple Developer](https://developer.apple.com/documentation/callkit/cxprovider/reportnewincomingvoippushpayload(_:completion:))*