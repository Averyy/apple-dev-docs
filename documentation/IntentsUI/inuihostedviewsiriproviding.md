# INUIHostedViewSiriProviding

**Framework**: IntentsUI  
**Kind**: protocol  
**Role**: Protocol

Methods for hiding portions of the default interfaces that Siri provides.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
protocol INUIHostedViewSiriProviding : NSObjectProtocol
```

```objc
@protocol INUIHostedViewSiriProviding <NSObject>
```

## Mentions

- [Configuring the View Controller for Your Custom Interface](../SiriKit/configuring-the-view-controller-for-your-custom-interface.md)

#### Overview

The properties of the [`INUIHostedViewSiriProviding`](./inuihostedviewsiriproviding.md) protocol let you notify Siri that you want to replace some parts of the standard interface with your custom content. You can never remove the entire default interface provided by Siri, but you can remove specific types of information if your view controller already provides the same information.

Implement this protocol in the view controller that you use to present custom content in your Intents UI extension. Siri supports the replacement of its map interface when displaying locations or the replacement of its message interface when showing the recipients and content of a message. Implementation of this protocol and its properties is optional.

## Topics

### Overriding the Default Behavior
- [var displaysMap: Bool](./inuihostedviewsiriproviding/displaysmap.md)
  A Boolean indicating whether your view controller replaces any default map interface.
- [var displaysMessage: Bool](./inuihostedviewsiriproviding/displaysmessage.md)
  A Boolean indicating whether your view controller replaces the default message interface that Siri provides.
- [var displaysPaymentTransaction: Bool](./inuihostedviewsiriproviding/displayspaymenttransaction.md)
  A Boolean indicating whether your view controller replaces the default payment transaction interface that Siri provides.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Custom UI for Siri and Maps
- [Creating an Intents UI Extension](../SiriKit/creating-an-intents-ui-extension.md)
  Create an Intents UI app extension to customize the interfaces displayed by Siri and Maps.
- [protocol INUIHostedViewControlling](./inuihostedviewcontrolling.md)
  Methods for presenting custom content in the Siri and Maps interfaces.
- [class INParameter](https://developer.apple.com/documentation/intents/inparameter)
  A parameter of an interaction object.
- [protocol INIntentSetImageKeyPath](https://developer.apple.com/documentation/intents/inintentsetimagekeypath)


---

*[View on Apple Developer](https://developer.apple.com/documentation/intentsui/inuihostedviewsiriproviding)*