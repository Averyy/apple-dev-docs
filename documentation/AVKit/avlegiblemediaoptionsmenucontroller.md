# AVLegibleMediaOptionsMenuController

**Framework**: AVKit  
**Kind**: class

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.4+
- macOS 26.4+
- visionOS 26.4+

## Declaration

```swift
class AVLegibleMediaOptionsMenuController
```

#### Overview

A menu controller for legible media options (subtitles/captions)

Supports both media track selection and caption appearance customization. When initialized without a player, only caption appearance options are available. When initialized with a player, both media tracks and caption appearance are available.

## Topics

### Creating a menu controller
- [init(player: AVPlayer?)](avlegiblemediaoptionsmenucontroller/init(player:).md)
### Managing the menu
- [func menu(contents: AVLegibleMediaOptionsMenuController.MenuContents) -> UIMenu?](avlegiblemediaoptionsmenucontroller/menu(contents:).md)
- [var menuState: AVLegibleMediaOptionsMenuState](avlegiblemediaoptionsmenucontroller/menustate.md)
- [AVLegibleMediaOptionsMenuController.MenuContents](avlegiblemediaoptionsmenucontroller/menucontents.md)
- [struct AVLegibleMediaOptionsMenuState](avlegiblemediaoptionsmenustate.md)
- [AVLegibleMediaOptionsMenuController.StateChangeReason](avlegiblemediaoptionsmenucontroller/statechangereason.md)
### Accessing the player
- [var player: AVPlayer](avlegiblemediaoptionsmenucontroller/player.md)
### Configuring a delegate
- [var delegate: (any AVLegibleMediaOptionsMenuController.Delegate)?](avlegiblemediaoptionsmenucontroller/delegate-swift.property.md)
- [AVLegibleMediaOptionsMenuController.Delegate](avlegiblemediaoptionsmenucontroller/delegate-swift.protocol.md)

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## See Also

- [struct AVLegibleMediaOptionsMenuState](avlegiblemediaoptionsmenustate.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avlegiblemediaoptionsmenucontroller)*