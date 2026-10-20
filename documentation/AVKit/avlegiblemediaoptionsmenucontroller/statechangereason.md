# AVLegibleMediaOptionsMenuController.StateChangeReason

**Framework**: AVKit  
**Kind**: enum  
**Role**: Enumeration

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

```c
enum AVLegibleMediaOptionsMenuStateChangeReason : NSInteger;
```

#### Overview

```
		An enum set, describing the different reasons for changing the menu state.
```

```
		Describes a non specified menu state change reason.
```

```
		Describes a menu state change reason due language mismatch.
```

## Topics

### Creating a reason
- [init?(rawValue: Int)](./statechangereason/init%28rawvalue%29.md)
### Reasons
- [AVLegibleMediaOptionsMenuController.StateChangeReason.none](./statechangereason/none.md)
- [AVLegibleMediaOptionsMenuController.StateChangeReason.languageMismatch](./statechangereason/languagemismatch.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Managing the menu
- [func menu(contents: AVLegibleMediaOptionsMenuController.MenuContents) -> UIMenu?](./menu%28contents%29.md)
- [var menuState: AVLegibleMediaOptionsMenuState](./menustate.md)
- [AVLegibleMediaOptionsMenuController.MenuContents](./menucontents.md)
- [struct AVLegibleMediaOptionsMenuState](../avlegiblemediaoptionsmenustate.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avlegiblemediaoptionsmenucontroller/statechangereason)*