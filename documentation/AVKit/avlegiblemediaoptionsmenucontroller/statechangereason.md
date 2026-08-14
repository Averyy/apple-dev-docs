# AVLegibleMediaOptionsMenuController.StateChangeReason

**Framework**: AVKit  
**Kind**: enum

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.4+
- macOS 26.4+
- visionOS 26.4+

## Declaration

```swift
enum StateChangeReason
```

#### Overview

```None
		An enum set, describing the different reasons for changing the menu state.
```

```None
		Describes a non specified menu state change reason.
```

```None
		Describes a menu state change reason due language mismatch.
```

## Topics

### Creating a reason
- [init?(rawValue: Int)](avlegiblemediaoptionsmenucontroller/statechangereason/init(rawvalue:).md)
### Reasons
- [AVLegibleMediaOptionsMenuController.StateChangeReason.none](avlegiblemediaoptionsmenucontroller/statechangereason/none.md)
- [AVLegibleMediaOptionsMenuController.StateChangeReason.languageMismatch](avlegiblemediaoptionsmenucontroller/statechangereason/languagemismatch.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../swift/bitwisecopyable.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [func menu(contents: AVLegibleMediaOptionsMenuController.MenuContents) -> UIMenu?](avlegiblemediaoptionsmenucontroller/menu(contents:).md)
- [var menuState: AVLegibleMediaOptionsMenuState](avlegiblemediaoptionsmenucontroller/menustate.md)
- [AVLegibleMediaOptionsMenuController.MenuContents](avlegiblemediaoptionsmenucontroller/menucontents.md)
- [struct AVLegibleMediaOptionsMenuState](avlegiblemediaoptionsmenustate.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avlegiblemediaoptionsmenucontroller/statechangereason)*