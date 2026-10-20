# MDLAssetResolver

**Framework**: Model I/O  
**Kind**: protocol  
**Role**: Protocol

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
protocol MDLAssetResolver : NSObjectProtocol
```

```objc
@protocol MDLAssetResolver <NSObject>
```

## Topics

### Instance Methods
- [func canResolveAssetNamed(String) -> Bool](./mdlassetresolver/canresolveassetnamed%28_%29.md)
- [func resolveAssetNamed(String) -> URL](./mdlassetresolver/resolveassetnamed%28_%29.md)

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
### Conforming Types
- [MDLBundleAssetResolver](./mdlbundleassetresolver.md)
- [MDLPathAssetResolver](./mdlpathassetresolver.md)
- [MDLRelativeAssetResolver](./mdlrelativeassetresolver.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlassetresolver)*