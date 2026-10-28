# reportNewIncomingCall(with:update:completion:)

**Framework**: CallKit  
**Kind**: method  
**Role**: Instance Method

Reports a new incoming call with the specified unique identifier to the provider.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 10.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
func reportNewIncomingCall(with UUID: UUID, update: CXCallUpdate, completion: @escaping @Sendable ((any Error)?) -> Void)
```

```swift
func reportNewIncomingCall(with UUID: UUID, update: CXCallUpdate) async throws
```

```objc
- (void) reportNewIncomingCallWithUUID:(NSUUID *) UUID update:(CXCallUpdate *) update completion:(void (^)(NSError *error)) completion;
```

## Mentions

- [Making and receiving VoIP calls](../making-and-receiving-voip-calls.md)
- [Sending End-to-End Encrypted VoIP Calls](../sending-end-to-end-encrypted-voip-calls.md)

## Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration:
>
> ```swift
> func reportNewIncomingCall(with UUID: UUID, update: CXCallUpdate) async throws
> ```
>
> For information about concurrency and asynchronous code in Swift, see [Calling Objective-C APIs Asynchronously](../../Swift/calling-objective-c-apis-asynchronously.md).

An incoming call may be disallowed by the system if, for example, the caller handle is blocked, or the user has Do Not Disturb enabled.

## Parameters

- `UUID`: The unique identifier of the call.
- `update`: The information for the call.
- `completion`: A block to be executed once the call is allowed or disallowed by the system. The block is executed on the delegate queue set by the [`setDelegate(_:queue:)`](./setdelegate%28_,queue%29.md) method, or on a private serial queue if none is specified.

  - **error**: If an error occurred, an error object indicating that the call was disallowed by the system, otherwise `nil`.

## See Also

### Reporting Calls
- [class func reportNewIncomingVoIPPushPayload([AnyHashable : Any], completion: (((any Error)?) -> Void)?)](./reportnewincomingvoippushpayload%28_,completion%29.md)
  Reports a new incoming call after your notification service extension decrypts a VoIP call request.
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

*[View on Apple Developer](https://developer.apple.com/documentation/callkit/cxprovider/reportnewincomingcall(with:update:completion:))*