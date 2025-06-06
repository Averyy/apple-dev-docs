# textureNames

**Framework**: SpriteKit  
**Kind**: property

The names of the texture images stored in the atlas.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
var textureNames: [String] { get }
```

#### Discussion

The property holds an array of [`NSString`](https://developer.apple.com/documentation/Foundation/NSString) objects. Each string is the name of a texture stored in the atlas. The count of the array is the number of textures stored in the atlas.

If the atlas is not currently loaded into memory, this method forces it to be loaded from the app bundle. Your game blocks until the atlas is loaded.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/sktextureatlas/texturenames)*