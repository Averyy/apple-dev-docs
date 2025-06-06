# init(size:pixelFormat:)

**Framework**: SpriteKit  
**Kind**: init

Initializes an empty texture with a specific size and format.

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
init(size: CGSize, pixelFormat format: Int32)
```

#### Return Value

An empty mutable texture.

#### Discussion

You must call the [`modifyPixelData(_:)`](skmutabletexture/modifypixeldata(_:).md) method at least once before using this texture.

## Parameters

- `size`: The size of the texture, in pixels.
- `format`: A Core Video format code. Three codes are supported:  ,  , and   for byte, half-float, and float components respectively.

## See Also

- [init(size: CGSize)](skmutabletexture/init(size:).md)
  Initializes an empty texture with a specific size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skmutabletexture/init(size:pixelformat:))*