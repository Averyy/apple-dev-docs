# IntentsUI

**Framework**: IntentsUI  
**Kind**: module  
**Role**: Framework

Customize content in the interface for Siri and Maps.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.0+
- macOS 12.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 3.2+

## Overview

> **Note**: SiriKit, Intents, and IntentsUI frameworks continue to provide legacy support for Shortcuts actions, widget configuration, and most existing Siri interactions. To implement modern support for these features and integrate your app with Apple Intelligence and Siri AI, use the [App Intents](../AppIntents/AppIntents.md) framework.

IntentsUI is a [SiriKit](../SiriKit/SiriKit.md) framework that enables people to interact with specific intents, and allows you to define actions in your app that respond to user inputs or system events. Use Intents UI to create custom UI that reflect interactions and enhance your app experience. The framework also prioritizes privacy and security by providing access to only the relevant data tied to each intent.

## Topics

### Custom UI for Siri and Maps
- [Creating an Intents UI Extension](../SiriKit/creating-an-intents-ui-extension.md)
  Create an Intents UI app extension to customize the interfaces displayed by Siri and Maps.
- [protocol INUIHostedViewControlling](./inuihostedviewcontrolling.md)
  Methods for presenting custom content in the Siri and Maps interfaces.
- [protocol INUIHostedViewSiriProviding](./inuihostedviewsiriproviding.md)
  Methods for hiding portions of the default interfaces that Siri provides.
- [class INParameter](../Intents/inparameter.md)
  A parameter of an interaction object.
- [protocol INIntentSetImageKeyPath](../Intents/inintentsetimagekeypath.md)
### Custom UI for Shortcuts
- [Shortcut-Related UI](../SiriKit/shortcut-related-ui.md)
  Incorporate standard buttons and interfaces into your user interface to offer easy shortcut creation.
- [Configuring the View Controller for Your Custom Interface](../SiriKit/configuring-the-view-controller-for-your-custom-interface.md)
  Configure your view controller to replace or augment the default interface in Siri or Maps.

## See Also

### Frameworks
- [Intents](../Intents/Intents.md)
  Empower people to customize interactions for your app on their device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intentsui)*