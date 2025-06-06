# init(fileNamed:)

**Framework**: GameplayKit  
**Kind**: init

Loads the specified SpriteKit scene file, creating a [`GKScene`](gkscene.md) object containing the SpriteKit scene and associated GameplayKit objects.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
convenience init?(fileNamed filename: String)
```

#### Return Value

A new GameplayKit scene.

#### Discussion

Use this initializer to load SpriteKit scenes (`.sks` files) created in the Xcode SpriteKit scene editor that contain associated GameplayKit entities, components, and pathfinding graphs.

For more information, see [`GameplayKit Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Conceptual/GameplayKit_Guide/index.html#//apple_ref/doc/uid/TP40015172).

## Parameters

- `filename`: The name of a scene file in your app’s main bundle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkscene/init(filenamed:))*