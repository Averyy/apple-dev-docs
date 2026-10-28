# CXProviderDelegate

**Framework**: CallKit  
**Kind**: protocol  
**Role**: Protocol

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

```objc
@protocol CXProviderDelegate <NSObject>
```

## Overview

The [`CXProviderDelegate`](./cxproviderdelegate.md) protocol defines a set of methods that are called by an object that represents a telephony provider it begins or resets, requests a transaction, performs an action, or an audio session changes its activation state.

## Topics

### Handling Provider Events
- [func providerDidBegin(CXProvider)](./cxproviderdelegate/providerdidbegin%28_%29.md)
  Called when the provider begins.
- [func providerDidReset(CXProvider)](./cxproviderdelegate/providerdidreset%28_%29.md)
  Called when the provider is reset.
### Determining the Execution of Transactions
- [func provider(CXProvider, execute: CXTransaction) -> Bool](./cxproviderdelegate/provider%28_,execute%29.md)
  Called when a transaction is executed by a call controller.
### Handling Call Actions
- [func provider(CXProvider, perform: CXStartCallAction)](./cxproviderdelegate/provider%28_,perform%29-2lem5.md)
  Called when the provider performs the specified start call action.
- [func provider(CXProvider, perform: CXAnswerCallAction)](./cxproviderdelegate/provider%28_,perform%29-h4in.md)
  Called when the provider performs the specified answer call action.
- [func provider(CXProvider, perform: CXEndCallAction)](./cxproviderdelegate/provider%28_,perform%29-9a0m.md)
  Called when the provider performs the specified end call action.
- [func provider(CXProvider, perform: CXSetHeldCallAction)](./cxproviderdelegate/provider%28_,perform%29-947b1.md)
  Called when the provider performs the specified set held call action.
- [func provider(CXProvider, perform: CXSetMutedCallAction)](./cxproviderdelegate/provider%28_,perform%29-4u3yu.md)
  Called when the provider performs the specified set muted call action.
- [func provider(CXProvider, perform: CXSetGroupCallAction)](./cxproviderdelegate/provider%28_,perform%29-9masw.md)
  Called when the provider performs the specified set group call action.
- [func provider(CXProvider, perform: CXPlayDTMFCallAction)](./cxproviderdelegate/provider%28_,perform%29-4htxt.md)
  Called when the provider performs the specified play DTMF (dual tone multifrequency) call action.
- [func provider(CXProvider, perform: CXSetTranslatingCallAction)](./cxproviderdelegate/provider%28_,perform%29-43atg.md)
  Called when the provider performs the specified set translation action.
- [func provider(CXProvider, timedOutPerforming: CXAction)](./cxproviderdelegate/provider%28_,timedoutperforming%29.md)
  Called when the provider performs the specified action times out.
### Handling Changes to Audio Session Activation State
- [func provider(CXProvider, didActivate: AVAudioSession)](./cxproviderdelegate/provider%28_,didactivate%29.md)
  Called when the provider’s audio session is activated.
- [func provider(CXProvider, didDeactivate: AVAudioSession)](./cxproviderdelegate/provider%28_,diddeactivate%29.md)
  Called when the provider’s audio session is deactivated.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Essentials
- [class CXProvider](./cxprovider.md)
  An object that represents a telephony provider.
- [class CXProviderConfiguration](./cxproviderconfiguration.md)
  An encapsulation of the configuration of a provider object.
- [Making and receiving VoIP calls](./making-and-receiving-voip-calls.md)
  Initiate outgoing calls with VoIP and configure your app to receive incoming calls.
- [VoIP calling with CallKit](./voip-calling-with-callkit.md)
  Use the CallKit framework to integrate native VoIP calling.
- [Preparing your app to be the default calling app](./preparing-your-app-to-be-the-default-calling-app.md)
  Configure your CallKit or LiveCommunicationKit app so people can set it as the default calling app on their device.
- [CallKit updates](../Updates/callkit.md)
  Learn about important changes to CallKit.


---

*[View on Apple Developer](https://developer.apple.com/documentation/callkit/cxproviderdelegate)*