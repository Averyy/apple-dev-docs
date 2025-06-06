# entities

**Framework**: GameplayKit  
**Kind**: property

The list of GameplayKit entities managed by the scene.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var entities: [GKEntity] { get }
```

#### Discussion

When you add entities (and their components) to a scene in the Xcode SpriteKit scene editor, Xcode automatically adds them to this array.

## See Also

- [func addEntity(GKEntity)](gkscene/addentity(_:).md)
  Adds a GameplayKit entity to the list of entities managed by the scene.
- [func removeEntity(GKEntity)](gkscene/removeentity(_:).md)
  Removes a GameplayKit entity from the list of entities managed by the scene.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkscene/entities)*