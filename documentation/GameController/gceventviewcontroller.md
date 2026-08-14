# GCEventViewController

**Framework**: Game Controller  
**Kind**: class

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

## Mentions

- [Adding virtual controls to games that support game controllers in iOS](adding-virtual-controls-to-games-that-support-game-controllers-in-ios.md)

#### Overview

On systems, such as tvOS, where the player uses the game controller to both navigate the system interface and play your game, use a [`GCEventViewController`](gceventviewcontroller.md) object as the root view controller to selectively receive input directly from the game controller. You can’t simultaneously process input through the responder chain and Game Controller input elements.

By default the system delivers input events to your app using the responder chain. To get the input values through the game controller objects, set a [`GCEventViewController`](gceventviewcontroller.md) object as the root view controller. The view controller delivers the input for its views and their subviews to the game controller’s profile. To switch back to the responder chain, set the view controller’s [`controllerUserInteractionEnabled`](gceventviewcontroller/controlleruserinteractionenabled.md) property to [`true`](https://developer.apple.com/documentation/swift/true).

## Topics

### Delivering game controller inputs
- [var controllerUserInteractionEnabled: Bool](gceventviewcontroller/controlleruserinteractionenabled.md)
  A Boolean value that indicates whether the system delivers game controller input to profile objects or to views using the responder chain.

## Relationships

### Inherits From
- [NSViewController](../appkit/nsviewcontroller.md)
- [UIViewController](../uikit/uiviewcontroller.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCoding](../foundation/nscoding.md)
- [NSEditor](../appkit/nseditor.md)
- [NSExtensionRequestHandling](../foundation/nsextensionrequesthandling.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [NSSeguePerforming](../appkit/nssegueperforming.md)
- [NSStandardKeyBindingResponding](../appkit/nsstandardkeybindingresponding.md)
- [NSTouchBarProvider](../appkit/nstouchbarprovider.md)
- [NSUserActivityRestoring](../appkit/nsuseractivityrestoring.md)
- [NSUserInterfaceItemIdentification](../appkit/nsuserinterfaceitemidentification.md)
- [UIActivityItemsConfigurationProviding](../uikit/uiactivityitemsconfigurationproviding.md)
- [UIAppearanceContainer](../uikit/uiappearancecontainer.md)
- [UIContentContainer](../uikit/uicontentcontainer.md)
- [UIFocusEnvironment](../uikit/uifocusenvironment.md)
- [UIPasteConfigurationSupporting](../uikit/uipasteconfigurationsupporting.md)
- [UIResponderStandardEditActions](../uikit/uiresponderstandardeditactions.md)
- [UIStateRestoring](../uikit/uistaterestoring.md)
- [UITraitChangeObservable](../uikit/uitraitchangeobservable-67e94.md)
- [UITraitEnvironment](../uikit/uitraitenvironment.md)
- [UIUserActivityRestoring](../uikit/uiuseractivityrestoring.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gceventviewcontroller)*