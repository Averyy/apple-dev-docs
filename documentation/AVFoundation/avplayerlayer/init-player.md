# init(player:)

**Framework**: AVFoundation  
**Kind**: init

Creates a layer object to present the visual contents of a player’s current item.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
init(player: AVPlayer?)
```

#### Return Value

A layer that displays the visual output of the associated player.

#### Discussion

You may create an arbitrary number of layers for the same player object.

## Parameters

- `player`: The player whose visual contents the layer presents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayerlayer/init(player:))*