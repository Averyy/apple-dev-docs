# init(named:)

**Framework**: SpriteKit  
**Kind**: init

Creates a texture atlas from data stored in the app bundle.

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
convenience init(named name: String)
```

#### Return Value

A new texture atlas object.

#### Discussion

If the texture atlas cannot be found, an exception is thrown.

## Parameters

- `name`: The name of the texture atlas, without the   extension.

## See Also

- [convenience init(dictionary: [String : Any])](sktextureatlas/init(dictionary:).md)
  Creates a texture atlas from a set of image files.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/sktextureatlas/init(named:))*