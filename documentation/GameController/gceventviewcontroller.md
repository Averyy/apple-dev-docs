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
@MainActor
class GCEventViewController
```

## Mentions

- [Adding touch controls to games that support game controllers in iOS](adding-touch-controls-to-games-that-support-game-controllers-in-ios.md)

#### Overview

On systems, such as tvOS, where the player uses the game controller to both navigate the system interface and play your game, use a [`GCEventViewController`](gceventviewcontroller.md) object as the root view controller to selectively receive input directly from the game controller. You can’t simultaneously process input through the responder chain and Game Controller input elements.

By default the system delivers input events to your app using the responder chain. To get the input values through the game controller objects, set a [`GCEventViewController`](gceventviewcontroller.md) object as the root view controller. The view controller delivers the input for its views and their subviews to the game controller’s profile. To switch back to the responder chain, set the view controller’s [`controllerUserInteractionEnabled`](gceventviewcontroller/controlleruserinteractionenabled.md) property to [`true`](https://developer.apple.com/documentation/Swift/true).

## Topics

### Delivering game controller inputs
- [var controllerUserInteractionEnabled: Bool](gceventviewcontroller/controlleruserinteractionenabled.md)
  A Boolean value that indicates whether the system delivers game controller input to profile objects or to views using the responder chain.

## Relationships

### Inherits From
- [NSViewController](../AppKit/NSViewController.md)
- [UIViewController](../UIKit/UIViewController.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSEditor](../AppKit/NSEditor.md)
- [NSExtensionRequestHandling](../Foundation/NSExtensionRequestHandling.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSeguePerforming](../AppKit/NSSeguePerforming.md)
- [NSStandardKeyBindingResponding](../AppKit/NSStandardKeyBindingResponding.md)
- [NSTouchBarProvider](../AppKit/NSTouchBarProvider.md)
- [NSUserActivityRestoring](../AppKit/NSUserActivityRestoring.md)
- [NSUserInterfaceItemIdentification](../AppKit/NSUserInterfaceItemIdentification.md)
- [UIActivityItemsConfigurationProviding](../UIKit/UIActivityItemsConfigurationProviding.md)
- [UIAppearanceContainer](../UIKit/UIAppearanceContainer.md)
- [UIContentContainer](../UIKit/UIContentContainer.md)
- [UIFocusEnvironment](../UIKit/UIFocusEnvironment.md)
- [UIPasteConfigurationSupporting](../UIKit/UIPasteConfigurationSupporting.md)
- [UIResponderStandardEditActions](../UIKit/UIResponderStandardEditActions.md)
- [UIStateRestoring](../UIKit/UIStateRestoring.md)
- [UITraitChangeObservable](../UIKit/UITraitChangeObservable-67e94.md)
- [UITraitEnvironment](../UIKit/UITraitEnvironment.md)
- [UIUserActivityRestoring](../UIKit/UIUserActivityRestoring.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gceventviewcontroller)*