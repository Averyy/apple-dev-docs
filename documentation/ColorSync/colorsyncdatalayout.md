# ColorSyncDataLayout

**Framework**: ColorSync  
**Kind**: typealias  
**Role**: Type Alias

A bit field describing the alpha information and byte order of a pixel layout.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
typealias ColorSyncDataLayout = UInt32
```

```c
typedef uint32_t ColorSyncDataLayout;
```

#### Discussion

Combine a [`ColorSyncAlphaInfo`](./colorsyncalphainfo.md) value (within [`kColorSyncAlphaInfoMask`](./kcolorsyncalphainfomask.md)) with a byte-order value (within [`kColorSyncByteOrderMask`](./kcolorsyncbyteordermask.md)) to describe how color components are packed.

## See Also

### Describing data layout
- [struct ColorSyncAlphaInfo](./colorsyncalphainfo.md)
  The location of the alpha component in a pixel, and whether it’s premultiplied.
- [struct ColorSyncDataDepth](./colorsyncdatadepth.md)
  The bit depth and numeric type of a color component in a pixel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/colorsync/colorsyncdatalayout)*