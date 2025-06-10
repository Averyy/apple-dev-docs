# SpatialAudioExperiences.AnchoringStrategy.scene(identifier:)

**Framework**: Audio Toolbox  
**Kind**: case

Anchor to the visual center of a particular UIScene.

**Availability**:
- visionOS 26.0+ (Beta)

## Declaration

```swift
case scene(identifier: String)
```

#### Discussion

The sound tracks the center of the UIScene’s volume or window even as the user moves it around their space.

Use the [`persistentIdentifier`](https://developer.apple.com/documentation/UIKit/UISceneSession/persistentIdentifier) for a [`UIScene`](https://developer.apple.com/documentation/UIKit/UIScene) as the identifier.

Configuring your sound with an unknown scene identifier causes the sound to receive a front anchoring strategy.

If a sound starts with a known scene identifer but the scene becomes unknown later on, the sound remains aligned with the scene’s last-known location until the user executes a recenter gesture at which point it reverts to a front anchoring strategy.

Using the UIScene identifier from an [`ImmersiveSpace`](https://developer.apple.com/documentation/SwiftUI/ImmersiveSpace) results in the same behavior as a front anchoring strategy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/spatialaudioexperiences/anchoringstrategy/scene(identifier:))*