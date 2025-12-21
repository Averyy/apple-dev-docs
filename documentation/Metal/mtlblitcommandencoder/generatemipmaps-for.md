# generateMipmaps(for:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Encodes a command that generates mipmaps for a texture from the base mipmap level up to the highest mipmap level.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
func generateMipmaps(for texture: any MTLTexture)
```

## Mentions

- [Generating mipmap data](generating-mipmap-data.md)

#### Discussion

The command generates with scaled images for all levels up to the highest mipmap level.

> **Note**:  The image filtering that GPU drivers use to generate the mipmaps may vary by the feature families ([`MTLGPUFamily`](mtlgpufamily.md)) it supports.

## Parameters

- `texture`: A texture instance the command generates mipmaps for that has:


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlblitcommandencoder/generatemipmaps(for:))*