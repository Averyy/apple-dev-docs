# AVLegibleMediaOptionsMenuState

**Framework**: AVKit  
**Kind**: struct  
**Role**: Structure

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.4+
- macOS 26.4+
- visionOS 26.4+

## Declaration

```swift
struct AVLegibleMediaOptionsMenuState
```

```c
typedef struct AVLegibleMediaOptionsMenuState { ... } AVLegibleMediaOptionsMenuState;
```

## Overview

A struct describing the state of the legible options menu.

## Topics

### Creating a menu state
- [init()](./avlegiblemediaoptionsmenustate/init%28%29.md)
- [init(enabled: ObjCBool, reason: AVLegibleMediaOptionsMenuController.StateChangeReason)](./avlegiblemediaoptionsmenustate/init%28enabled,reason%29.md)
### Inspecting the state
- [var enabled: ObjCBool](./avlegiblemediaoptionsmenustate/enabled.md)
  Whether or not the legible options menu is
- [var reason: AVLegibleMediaOptionsMenuController.StateChangeReason](./avlegiblemediaoptionsmenustate/reason.md)
  The reason for changing the menu state

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Sendable](../Swift/sendable.md)

## See Also

### Media and content selection
- [class AVLegibleMediaOptionsMenuController](./avlegiblemediaoptionsmenucontroller.md)
- [class AVContentSelectionViewController](./avcontentselectionviewcontroller.md)
  A view controller for providing additional UI to the multiview experience.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avlegiblemediaoptionsmenustate)*