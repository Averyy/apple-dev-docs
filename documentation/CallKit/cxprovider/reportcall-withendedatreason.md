# reportCall(with:endedAt:reason:)

**Framework**: CallKit  
**Kind**: method

Reports to the provider that a call with the specified identifier ended at a given date for a particular reason.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 10.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
func reportCall(with UUID: UUID, endedAt dateEnded: Date?, reason endedReason: CXCallEndedReason)
```

## Parameters

- `UUID`: The unique identifier of the call.
- `dateEnded`: If  , the current time is used.
- `endedReason`: The reason that the call ended. For possible values, see  .

## See Also

- [func reportNewIncomingCall(with: UUID, update: CXCallUpdate, completion: ((any Error)?) -> Void)](cxprovider/reportnewincomingcall(with:update:completion:).md)
  Reports a new incoming call with the specified unique identifier to the provider.
- [class func reportNewIncomingVoIPPushPayload([AnyHashable : Any], completion: (((any Error)?) -> Void)?)](cxprovider/reportnewincomingvoippushpayload(_:completion:).md)
  Reports a new incoming call after your notification service extension decrypts a VoIP call request.
- [com.apple.developer.usernotifications.filtering](../BundleResources/Entitlements/com.apple.developer.usernotifications.filtering.md)
  Enable receiving notifications without displaying the notification to the user.
- [func reportOutgoingCall(with: UUID, startedConnectingAt: Date?)](cxprovider/reportoutgoingcall(with:startedconnectingat:).md)
  Reports to the provider that an outgoing call with the specified unique identifier started connecting at a particular time.
- [func reportOutgoingCall(with: UUID, connectedAt: Date?)](cxprovider/reportoutgoingcall(with:connectedat:).md)
  Reports to the provider that an outgoing call with the specified unique identifier finished connecting at a particular time.
- [func reportCall(with: UUID, updated: CXCallUpdate)](cxprovider/reportcall(with:updated:).md)
  Reports to the provider that an active call updated its information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/callkit/cxprovider/reportcall(with:endedat:reason:))*