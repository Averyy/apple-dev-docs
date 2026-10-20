# reportNewIncomingVoIPPushPayload(_:completion:)

**Framework**: CallKit  
**Kind**: method  
**Role**: Type Method

Reports a new incoming call after your notification service extension decrypts a VoIP call request.

**Availability**:
- iOS 14.5+
- iPadOS 14.5+
- Mac Catalyst 14.5+
- visionOS 1.0+

## Declaration

```swift
class func reportNewIncomingVoIPPushPayload(_ dictionaryPayload: [AnyHashable : Any], completion: (@Sendable ((any Error)?) -> Void)? = nil)
```

```swift
class func reportNewIncomingVoIPPushPayload(_ dictionaryPayload: [AnyHashable : Any]) async throws
```

```objc
+ (void) reportNewIncomingVoIPPushPayload:(NSDictionary *) dictionaryPayload completion:(void (^)(NSError *)) completion;
```

## Mentions

- [Sending End-to-End Encrypted VoIP Calls](../sending-end-to-end-encrypted-voip-calls.md)

#### Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration:
>
> ```swift
> class func reportNewIncomingVoIPPushPayload(_ dictionaryPayload: [AnyHashable : Any]) async throws
> ```
>
> For information about concurrency and asynchronous code in Swift, see [Calling Objective-C APIs Asynchronously](../../Swift/calling-objective-c-apis-asynchronously.md).

Call this method when your notification service extension receives an encrypted VoIP call request. The system then launches your app and calls your [`pushRegistry(_:didReceiveIncomingPushWith:for:completion:)`](../../PushKit/pkpushregistrydelegate/pushregistry%28_,didreceiveincomingpushwith,for,completion%29.md) method. From this point, the app handles the call just like any incoming VoIP call. For more information, see [Sending End-to-End Encrypted VoIP Calls](../sending-end-to-end-encrypted-voip-calls.md).

To call this method, your notification service extension must have the [`com.apple.developer.usernotifications.filtering`](../../BundleResources/entitlements/com.apple.developer.usernotifications.filtering.md) entitlement.

> ❗ **Important**:  Only call this method when your server can’t determine whether an outgoing notification is a request for a VoIP call or some other data (such as a text message) due to metadata encryption. If your server knows that the outgoing content is a VoIP call, send a [`voIP`](../../PushKit/pkpushtype/voip.md) push notification instead. For more information, see [PushKit](../../PushKit/PushKit.md).

## Parameters

- `dictionaryPayload`: A dictionary containing additional data about the incoming call. All keys and values in the dictionary must implement the [`NSSecureCoding`](../../Foundation/nssecurecoding.md) protocol.
- `completion`: A block that CallKit executes after allowing or disallowing the call. CallKit executes the block on a private serial queue. The completion handler takes the following parameter:

  - **`error`**: When the system disallows a call, it sets this parameter to an error object that contains information about why it disallowed the call; otherwise it’s `nil`.

## See Also

### Reporting Calls
- [func reportNewIncomingCall(with: UUID, update: CXCallUpdate, completion: ((any Error)?) -> Void)](./reportnewincomingcall%28with,update,completion%29.md)
  Reports a new incoming call with the specified unique identifier to the provider.
- [com.apple.developer.usernotifications.filtering](../../BundleResources/entitlements/com.apple.developer.usernotifications.filtering.md)
  Enable receiving notifications without displaying the notification to the user.
- [func reportOutgoingCall(with: UUID, startedConnectingAt: Date?)](./reportoutgoingcall%28with,startedconnectingat%29.md)
  Reports to the provider that an outgoing call with the specified unique identifier started connecting at a particular time.
- [func reportOutgoingCall(with: UUID, connectedAt: Date?)](./reportoutgoingcall%28with,connectedat%29.md)
  Reports to the provider that an outgoing call with the specified unique identifier finished connecting at a particular time.
- [func reportCall(with: UUID, updated: CXCallUpdate)](./reportcall%28with,updated%29.md)
  Reports to the provider that an active call updated its information.
- [func reportCall(with: UUID, endedAt: Date?, reason: CXCallEndedReason)](./reportcall%28with,endedat,reason%29.md)
  Reports to the provider that a call with the specified identifier ended at a given date for a particular reason.


---

*[View on Apple Developer](https://developer.apple.com/documentation/callkit/cxprovider/reportnewincomingvoippushpayload(_:completion:))*