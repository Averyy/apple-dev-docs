# AVLegibleMediaOptionsMenuController

**Framework**: AVKit  
**Kind**: class  
**Role**: Class

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

```objc
@interface AVLegibleMediaOptionsMenuController : NSObject
```

#### Overview

A menu controller for legible media options (subtitles/captions)

Supports both media track selection and caption appearance customization. When initialized without a player, only caption appearance options are available. When initialized with a player, both media tracks and caption appearance are available.

## Topics

### Creating a menu controller
- [init(player: AVPlayer?)](./avlegiblemediaoptionsmenucontroller/init%28player%29.md)
### Managing the menu
- [func menu(contents: AVLegibleMediaOptionsMenuController.MenuContents) -> UIMenu?](./avlegiblemediaoptionsmenucontroller/menu%28contents%29.md)
- [var menuState: AVLegibleMediaOptionsMenuState](./avlegiblemediaoptionsmenucontroller/menustate.md)
- [AVLegibleMediaOptionsMenuController.MenuContents](./avlegiblemediaoptionsmenucontroller/menucontents.md)
- [struct AVLegibleMediaOptionsMenuState](./avlegiblemediaoptionsmenustate.md)
- [AVLegibleMediaOptionsMenuController.StateChangeReason](./avlegiblemediaoptionsmenucontroller/statechangereason.md)
### Accessing the player
- [var player: AVPlayer](./avlegiblemediaoptionsmenucontroller/player.md)
### Configuring a delegate
- [var delegate: (any AVLegibleMediaOptionsMenuController.Delegate)?](./avlegiblemediaoptionsmenucontroller/delegate-swift.property.md)
- [AVLegibleMediaOptionsMenuController.Delegate](./avlegiblemediaoptionsmenucontroller/delegate-swift.protocol.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Media and content selection
- [struct AVLegibleMediaOptionsMenuState](./avlegiblemediaoptionsmenustate.md)
- [class AVContentSelectionViewController](./avcontentselectionviewcontroller.md)
  A view controller for providing additional UI to the multiview experience.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avlegiblemediaoptionsmenucontroller)*