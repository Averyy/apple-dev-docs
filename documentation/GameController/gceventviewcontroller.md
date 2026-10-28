# GCEventViewController

**Framework**: Game Controller  
**Kind**: class  
**Role**: Class

A view controller that delivers input either from the responder chain to views, or from game controllers to profiles.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class GCEventViewController
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS*

```objc
@interface GCEventViewController : UIViewController
```

*macOS*

```objc
@interface GCEventViewController : NSViewController
```

## Mentions

- [Adding virtual controls to games that support game controllers in iOS](./adding-virtual-controls-to-games-that-support-game-controllers-in-ios.md)

## Overview

On systems, such as tvOS, where the player uses the game controller to both navigate the system interface and play your game, use a [`GCEventViewController`](./gceventviewcontroller.md) object as the root view controller to selectively receive input directly from the game controller. You can’t simultaneously process input through the responder chain and Game Controller input elements.

By default the system delivers input events to your app using the responder chain. To get the input values through the game controller objects, set a [`GCEventViewController`](./gceventviewcontroller.md) object as the root view controller. The view controller delivers the input for its views and their subviews to the game controller’s profile. To switch back to the responder chain, set the view controller’s [`controllerUserInteractionEnabled`](./gceventviewcontroller/controlleruserinteractionenabled.md) property to [`true`](../Swift/true.md).

## Topics

### Delivering game controller inputs
- [var controllerUserInteractionEnabled: Bool](./gceventviewcontroller/controlleruserinteractionenabled.md)
  A Boolean value that indicates whether the system delivers game controller input to profile objects or to views using the responder chain.

## Relationships

### Inherits From
- [NSViewController](../AppKit/nsviewcontroller.md)
- [UIViewController](../UIKit/uiviewcontroller.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSEditor](../AppKit/nseditor.md)
- [NSExtensionRequestHandling](../Foundation/nsextensionrequesthandling.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSeguePerforming](../AppKit/nssegueperforming.md)
- [NSStandardKeyBindingResponding](../AppKit/nsstandardkeybindingresponding.md)
- [NSTouchBarProvider](../AppKit/nstouchbarprovider.md)
- [NSUserActivityRestoring](../AppKit/nsuseractivityrestoring.md)
- [NSUserInterfaceItemIdentification](../AppKit/nsuserinterfaceitemidentification.md)
- [UIActivityItemsConfigurationProviding](../UIKit/uiactivityitemsconfigurationproviding.md)
- [UIAppearanceContainer](../UIKit/uiappearancecontainer.md)
- [UIContentContainer](../UIKit/uicontentcontainer.md)
- [UIFocusEnvironment](../UIKit/uifocusenvironment.md)
- [UIPasteConfigurationSupporting](../UIKit/uipasteconfigurationsupporting.md)
- [UIResponderStandardEditActions](../UIKit/uiresponderstandardeditactions.md)
- [UIStateRestoring](../UIKit/uistaterestoring.md)
- [UITraitChangeObservable](../UIKit/uitraitchangeobservable-67e94.md)
- [UITraitEnvironment](../UIKit/uitraitenvironment.md)
- [UIUserActivityRestoring](../UIKit/uiuseractivityrestoring.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gceventviewcontroller)*