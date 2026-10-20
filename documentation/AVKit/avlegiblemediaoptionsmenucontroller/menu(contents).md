# menu(contents:)

**Framework**: AVKit  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.4+
- macOS 26.4+
- visionOS 26.4+

## Declaration

*iOS, iPadOS, Mac Catalyst, visionOS*

```swift
func menu(contents: AVLegibleMediaOptionsMenuController.MenuContents = []) -> UIMenu?
```

*macOS*

```swift
func menu(contents: AVLegibleMediaOptionsMenuController.MenuContents = []) -> NSMenu?
```

*iOS, iPadOS, Mac Catalyst, visionOS*

```objc
- (UIMenu *) menuWithContents:(AVLegibleMediaOptionsMenuContents) contents;
```

*macOS*

```objc
- (NSMenu *) menuWithContents:(AVLegibleMediaOptionsMenuContents) contents;
```

#### Return Value

A NSMenu ready to be presented by the client, or nil if the menu cannot be built

#### Discussion

Builds a legible options menu using the specified contents.

Returns nil if the requested menu type cannot be built due to missing content (e.g., requesting track selection without a player).

## Parameters

- `contents`: A set of values from the AVLegibleMediaOptionsMenuContents

## See Also

### Managing the menu
- [var menuState: AVLegibleMediaOptionsMenuState](./menustate.md)
- [AVLegibleMediaOptionsMenuController.MenuContents](./menucontents.md)
- [struct AVLegibleMediaOptionsMenuState](../avlegiblemediaoptionsmenustate.md)
- [AVLegibleMediaOptionsMenuController.StateChangeReason](./statechangereason.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avlegiblemediaoptionsmenucontroller/menu(contents:))*