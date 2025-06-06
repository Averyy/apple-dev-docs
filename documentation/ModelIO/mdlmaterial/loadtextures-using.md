# loadTextures(using:)

**Framework**: Model I/O  
**Kind**: method

Loads textures using resolver for string paths and NSURLs.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func loadTextures(using resolver: any MDLAssetResolver)
```

#### Discussion

Iterates all material properties. If there are string values or NSURL values, and you can resolve the values as textures, then [`MDLTextureSampler`](mdltexturesampler.md) values replaces the string and NSURL values.

## Parameters

- `resolver`: If non-nil, the resolver converts stringValues or NSURLs to MDLTextureSampler values.

## See Also

- [func resolveTextures(with: any MDLAssetResolver)](mdlmaterial/resolvetextures(with:).md)
  Resolves all texture string paths as NSURLs with resolver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlmaterial/loadtextures(using:))*