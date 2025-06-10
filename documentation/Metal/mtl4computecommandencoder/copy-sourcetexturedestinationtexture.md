# copy(sourceTexture:destinationTexture:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Encodes a command that copies data from a texture to another.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
func copy(sourceTexture: any MTLTexture, destinationTexture: any MTLTexture)
```

## Parameters

- `sourceTexture`: An   instance the command copies data from.
- `destinationTexture`: Another   instance the command copies the data into that has the same    and   as  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4computecommandencoder/copy(sourcetexture:destinationtexture:))*