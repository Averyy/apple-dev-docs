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

### Protocols
- [AVLegibleMediaOptionsMenuController.Delegate](avlegiblemediaoptionsmenucontroller/delegate-swift.protocol.md)
### Structures
- [AVLegibleMediaOptionsMenuController.MenuContents](avlegiblemediaoptionsmenucontroller/menucontents.md)
### Initializers
- [init(player: AVPlayer?)](avlegiblemediaoptionsmenucontroller/init(player:).md)
### Instance Properties
- [var delegate: (any AVLegibleMediaOptionsMenuController.Delegate)?](avlegiblemediaoptionsmenucontroller/delegate-swift.property.md)
- [var menuState: AVLegibleMediaOptionsMenuState](avlegiblemediaoptionsmenucontroller/menustate.md)
- [var player: AVPlayer](avlegiblemediaoptionsmenucontroller/player.md)
### Instance Methods
- [func menu(contents: AVLegibleMediaOptionsMenuController.MenuContents) -> UIMenu?](avlegiblemediaoptionsmenucontroller/menu(contents:).md)
### Enumerations
- [AVLegibleMediaOptionsMenuController.StateChangeReason](avlegiblemediaoptionsmenucontroller/statechangereason.md)

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avlegiblemediaoptionsmenucontroller)*