# menu(contents:)

**Framework**: AVKit  
**Kind**: method

**Availability**:
- iOS 26.4+ (Beta)
- iPadOS 26.4+ (Beta)
- Mac Catalyst 26.4+ (Beta)
- macOS 26.4+ (Beta)
- visionOS 26.4+ (Beta)

## Declaration

```swift
func menu(contents: AVLegibleMediaOptionsMenuController.MenuContents = []) -> NSMenu?
```

#### Return Value

A NSMenu ready to be presented by the client, or nil if the menu cannot be built

#### Discussion

Builds a legible options menu using the specified contents.

Returns nil if the requested menu type cannot be built due to missing content (e.g., requesting track selection without a player).

## Parameters

- `contents`: A set of values from the AVLegibleMediaOptionsMenuContents


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avlegiblemediaoptionsmenucontroller/menu(contents:))*