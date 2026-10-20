# MSStickerSize.large

**Framework**: Messages  
**Kind**: case  
**Role**: Case

Large stickers.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+

## Declaration

```swift
case large
```

```c
MSStickerSizeLarge
```

#### Discussion

Use 206 x 206 point images to create large stickers. Always provide @3x images for these stickers (618 x 618 pixels). The system generates the @2x and @1x versions by downscaling the @3x images at runtime.

## See Also

### Constants
- [MSStickerSize.small](./small.md)
  Small stickers.
- [MSStickerSize.regular](./regular.md)
  Medium-sized stickers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/messages/msstickersize/large)*