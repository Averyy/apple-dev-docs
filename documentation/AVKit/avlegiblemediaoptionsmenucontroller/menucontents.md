# AVLegibleMediaOptionsMenuController.MenuContents

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
struct MenuContents
```

```c
enum AVLegibleMediaOptionsMenuContents : NSInteger;
```

#### Overview

```
		An option set, describing the different contents of legible option menus.
```

```
		Describes the legible contents of a legible options menu
```

```
		Describes the caption appearance contents of a legible options menu.
```

```
		Describes all the contents of a legible options menu.
```

## Topics

### Creating menu contents
- [init(rawValue: Int)](./menucontents/init%28rawvalue%29.md)
### Menu content options
- [static var all: AVLegibleMediaOptionsMenuController.MenuContents](./menucontents/all.md)
- [static var captionAppearance: AVLegibleMediaOptionsMenuController.MenuContents](./menucontents/captionappearance.md)
- [static var legible: AVLegibleMediaOptionsMenuController.MenuContents](./menucontents/legible.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../../Swift/optionset.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)
- [SetAlgebra](../../Swift/setalgebra.md)

## See Also

### Managing the menu
- [func menu(contents: AVLegibleMediaOptionsMenuController.MenuContents) -> UIMenu?](./menu%28contents%29.md)
- [var menuState: AVLegibleMediaOptionsMenuState](./menustate.md)
- [struct AVLegibleMediaOptionsMenuState](../avlegiblemediaoptionsmenustate.md)
- [AVLegibleMediaOptionsMenuController.StateChangeReason](./statechangereason.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avlegiblemediaoptionsmenucontroller/menucontents)*