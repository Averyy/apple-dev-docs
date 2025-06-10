# CXProviderDelegate

**Framework**: CallKit  
**Kind**: protocol

A collection of methods that a telephony provider object calls.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 10.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
protocol CXProviderDelegate : NSObjectProtocol
```

#### Overview

The [`CXProviderDelegate`](cxproviderdelegate.md) protocol defines a set of methods that are called by an object that represents a telephony provider it begins or resets, requests a transaction, performs an action, or an audio session changes its activation state.

## Topics

### Handling Provider Events
- [func providerDidBegin(CXProvider)](cxproviderdelegate/providerdidbegin(_:).md)
  Called when the provider begins.
- [func providerDidReset(CXProvider)](cxproviderdelegate/providerdidreset(_:).md)
  Called when the provider is reset.
### Determining the Execution of Transactions
- [func provider(CXProvider, execute: CXTransaction) -> Bool](cxproviderdelegate/provider(_:execute:).md)
  Called when a transaction is executed by a call controller.
### Handling Call Actions
- [func provider(CXProvider, perform: CXStartCallAction)](cxproviderdelegate/provider(_:perform:)-2lem5.md)
  Called when the provider performs the specified start call action.
- [func provider(CXProvider, perform: CXAnswerCallAction)](cxproviderdelegate/provider(_:perform:)-h4in.md)
  Called when the provider performs the specified answer call action.
- [func provider(CXProvider, perform: CXEndCallAction)](cxproviderdelegate/provider(_:perform:)-9a0m.md)
  Called when the provider performs the specified end call action.
- [func provider(CXProvider, perform: CXSetHeldCallAction)](cxproviderdelegate/provider(_:perform:)-947b1.md)
  Called when the provider performs the specified set held call action.
- [func provider(CXProvider, perform: CXSetMutedCallAction)](cxproviderdelegate/provider(_:perform:)-4u3yu.md)
  Called when the provider performs the specified set muted call action.
- [func provider(CXProvider, perform: CXSetGroupCallAction)](cxproviderdelegate/provider(_:perform:)-9masw.md)
  Called when the provider performs the specified set group call action.
- [func provider(CXProvider, perform: CXPlayDTMFCallAction)](cxproviderdelegate/provider(_:perform:)-4htxt.md)
  Called when the provider performs the specified play DTMF (dual tone multifrequency) call action.
- [func provider(CXProvider, perform: CXSetTranslatingCallAction)](cxproviderdelegate/provider(_:perform:)-43atg.md)
  Called when the provider performs the specified set translation action.
- [func provider(CXProvider, timedOutPerforming: CXAction)](cxproviderdelegate/provider(_:timedoutperforming:).md)
  Called when the provider performs the specified action times out.
### Handling Changes to Audio Session Activation State
- [func provider(CXProvider, didActivate: AVAudioSession)](cxproviderdelegate/provider(_:didactivate:).md)
  Called when the provider’s audio session is activated.
- [func provider(CXProvider, didDeactivate: AVAudioSession)](cxproviderdelegate/provider(_:diddeactivate:).md)
  Called when the provider’s audio session is deactivated.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class CXProvider](cxprovider.md)
  An object that represents a telephony provider.
- [class CXProviderConfiguration](cxproviderconfiguration.md)
  An encapsulation of the configuration of a provider object.
- [Making and receiving VoIP calls](making-and-receiving-voip-calls.md)
  Initiate outgoing calls with VoIP and configure your app to receive incoming calls.
- [VoIP calling with CallKit](voip-calling-with-callkit.md)
  Use the CallKit framework to integrate native VoIP calling.
- [Preparing your app to be the default calling app](preparing-your-app-to-be-the-default-calling-app.md)
  Configure your CallKit or LiveCommunicationKit app so people can set it as the default calling app on their device.
- [CallKit updates](../Updates/CallKit.md)
  Learn about important changes to CallKit.


---

*[View on Apple Developer](https://developer.apple.com/documentation/callkit/cxproviderdelegate)*