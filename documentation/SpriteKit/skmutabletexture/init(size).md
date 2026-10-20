# init(size:)

**Framework**: SpriteKit  
**Kind**: init

Initializes an empty texture with a specific size.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
init(size: CGSize)
```

#### Return Value

An empty mutable texture.

#### Discussion

You must call the [`modifyPixelData(_:)`](skmutabletexture/modifypixeldata(_:).md) method at least once before using this texture.

## Parameters

- `size`: The size of the texture, in pixels.

## See Also

- [init(size: CGSize, pixelFormat: Int32)](skmutabletexture/init(size:pixelformat:).md)
  Initializes an empty texture with a specific size and format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skmutabletexture/init(size:))*