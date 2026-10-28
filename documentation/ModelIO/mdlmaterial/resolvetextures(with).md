# resolveTextures(with:)

**Framework**: Model I/O  
**Kind**: method  
**Role**: Instance Method

Resolves all texture string paths as NSURLs with resolver.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func resolveTextures(with resolver: any MDLAssetResolver)
```

```objc
- (void) resolveTexturesWithResolver:(id<MDLAssetResolver>) resolver;
```

## Discussion

Iterates all material properties. If there are string values, they’re resolved into valid paths as NSURL values by the resolver.

## Parameters

- `resolver`: If non-nil, the resolver converts stringValues or NSURLs to MDLTextureSampler values.

## See Also

### Working with textures using resolvers
- [func loadTextures(using: any MDLAssetResolver)](./loadtextures%28using%29.md)
  Loads textures using resolver for string paths and NSURLs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlmaterial/resolvetextures(with:))*