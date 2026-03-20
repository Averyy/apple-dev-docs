# init(player:)

**Framework**: AVKit  
**Kind**: init

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.4+
- macOS 26.4+
- visionOS 26.4+

## Declaration

```swift
init(player: AVPlayer?)
```

#### Discussion

Creates an AVLegibleMediaOptionsMenuController with an optional player

When player is non-nil, both media tracks and caption appearance options will be included, otherwise, only caption appearance options.

## Parameters

- `player`: The AVPlayer to build menus from, or nil for non-track-specific options only


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avlegiblemediaoptionsmenucontroller/init(player:))*