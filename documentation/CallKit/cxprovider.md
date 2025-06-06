# CXProvider

**Framework**: CallKit  
**Kind**: class

An object that represents a telephony provider.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 10.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
class CXProvider
```

## Mentions

- [Making and receiving VoIP calls](making-and-receiving-voip-calls.md)

#### Overview

A [`CXProvider`](cxprovider.md) object is responsible for reporting out-of-band notifications that occur to the system. A VoIP app should create only one instance of [`CXProvider`](cxprovider.md) and store it for use globally. A [`CXProvider`](cxprovider.md) object is initialized with a [`CXProviderConfiguration`](cxproviderconfiguration.md) object to specify the behavior and capabilities of calls. Each provider can specify an object conforming to the [`CXProviderDelegate`](cxproviderdelegate.md) protocol to respond to events, such as the call starting, the call being put on hold, or the provider’s audio session being activated.

##### Subclassing Notes

[`CXProvider`](cxprovider.md) is not intended for subclassing.

## Topics

### Creating New Providers
- [init(configuration: CXProviderConfiguration)](cxprovider/init(configuration:).md)
  Initializes a new provider with the specified configuration.
### Setting the Delegate
- [func setDelegate((any CXProviderDelegate)?, queue: dispatch_queue_t?)](cxprovider/setdelegate(_:queue:).md)
  Sets a provider delegate, specifying an optional queue on which to execute delegate methods.
### Accessing Provider Attributes
- [var configuration: CXProviderConfiguration](cxprovider/configuration.md)
  The configuration of the provider.
### Accessing Pending Transaction and Call Actions
- [var pendingTransactions: [CXTransaction]](cxprovider/pendingtransactions.md)
  Incomplete transactions.
- [func pendingCallActions(of: AnyClass, withCall: UUID) -> [CXCallAction]](cxprovider/pendingcallactions(of:withcall:).md)
  Returns all call actions in any pending transactions of the specified class for the specified call identifier that are incomplete.
### Reporting Calls
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
- [func reportCall(with: UUID, endedAt: Date?, reason: CXCallEndedReason)](cxprovider/reportcall(with:endedat:reason:).md)
  Reports to the provider that a call with the specified identifier ended at a given date for a particular reason.
### Invalidating a Provider
- [func invalidate()](cxprovider/invalidate.md)
  Invalidates the provider and completes all active calls with an error.
### Handling Errors
- [enum CXCallEndedReason](cxcallendedreason.md)
  The reason that a call ended.
- [struct CXError](cxerror.md)
  Error codes for the CallKit errors.
- [CXError.Code](cxerror/code.md)
  Error codes for the CallKit errors.
- [struct CXErrorCodeIncomingCallError](cxerrorcodeincomingcallerror-swift.struct.md)
  Codes for errors that occur during incoming calls.
- [CXErrorCodeIncomingCallError.Code](cxerrorcodeincomingcallerror-swift.struct/code.md)
  Codes for errors that occur during incoming calls.
- [struct CXErrorCodeNotificationServiceExtensionError](cxerrorcodenotificationserviceextensionerror-swift.struct.md)
  Errors that can occur when reporting new, incoming VoIP calls.
- [let CXErrorDomain: String](cxerrordomain.md)
  The domain for CallKit errors.
- [let CXErrorDomainIncomingCall: String](cxerrordomainincomingcall.md)
  The domain for errors that occur during incoming calls.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [protocol CXProviderDelegate](cxproviderdelegate.md)
  A collection of methods that a telephony provider object calls.
- [class CXProviderConfiguration](cxproviderconfiguration.md)
  An encapsulation of the configuration of a provider object.
- [Making and receiving VoIP calls](making-and-receiving-voip-calls.md)
  Initiate outgoing calls with VoIP and configure your app to receive incoming calls.
- [VoIP calling with CallKit](voip-calling-with-callkit.md)
  Use the CallKit framework to integrate native VoIP calling.
- [Preparing your app to be the default calling app](preparing-your-app-to-be-the-default-calling-app.md)
  Configure your CallKit or LiveCommunicationKit app so people can set it as the default calling app on their device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/callkit/cxprovider)*