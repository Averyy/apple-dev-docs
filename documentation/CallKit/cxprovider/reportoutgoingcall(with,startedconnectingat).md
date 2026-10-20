# reportOutgoingCall(with:startedConnectingAt:)

**Framework**: CallKit  
**Kind**: method  
**Role**: Instance Method

Reports to the provider that an outgoing call with the specified unique identifier started connecting at a particular time.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 10.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
func reportOutgoingCall(with UUID: UUID, startedConnectingAt dateStartedConnecting: Date?)
```

```objc
- (void) reportOutgoingCallWithUUID:(NSUUID *) UUID startedConnectingAtDate:(NSDate *) dateStartedConnecting;
```

## Parameters

- `UUID`: The unique identifier of the call.
- `dateStartedConnecting`: The time at which the call started connecting.

  If `nil`, the current time is used.

## See Also

### Reporting Calls
- [func reportNewIncomingCall(with: UUID, update: CXCallUpdate, completion: ((any Error)?) -> Void)](./reportnewincomingcall%28with,update,completion%29.md)
  Reports a new incoming call with the specified unique identifier to the provider.
- [class func reportNewIncomingVoIPPushPayload([AnyHashable : Any], completion: (((any Error)?) -> Void)?)](./reportnewincomingvoippushpayload%28_,completion%29.md)
  Reports a new incoming call after your notification service extension decrypts a VoIP call request.
- [com.apple.developer.usernotifications.filtering](../../BundleResources/entitlements/com.apple.developer.usernotifications.filtering.md)
  Enable receiving notifications without displaying the notification to the user.
- [func reportOutgoingCall(with: UUID, connectedAt: Date?)](./reportoutgoingcall%28with,connectedat%29.md)
  Reports to the provider that an outgoing call with the specified unique identifier finished connecting at a particular time.
- [func reportCall(with: UUID, updated: CXCallUpdate)](./reportcall%28with,updated%29.md)
  Reports to the provider that an active call updated its information.
- [func reportCall(with: UUID, endedAt: Date?, reason: CXCallEndedReason)](./reportcall%28with,endedat,reason%29.md)
  Reports to the provider that a call with the specified identifier ended at a given date for a particular reason.


---

*[View on Apple Developer](https://developer.apple.com/documentation/callkit/cxprovider/reportoutgoingcall(with:startedconnectingat:))*