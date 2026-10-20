# MSStickerSize.regular

**Framework**: Messages  
**Kind**: case  
**Role**: Case

Medium-sized stickers.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+

## Declaration

```swift
case regular
```

```c
MSStickerSizeRegular
```

#### Discussion

Use 136 x 136 point images to create regular-sized stickers. Always provide @3x images for these stickers (408 x 408 pixels). The system generates the @2x and @1x versions by downscaling the @3x images at runtime.

## See Also

### Constants
- [MSStickerSize.small](./small.md)
  Small stickers.
- [MSStickerSize.large](./large.md)
  Large stickers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/messages/msstickersize/regular)*