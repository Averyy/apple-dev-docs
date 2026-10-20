# moveTextureMappings(sourceTexture:sourceSlice:sourceLevel:sourceOrigin:sourceSize:destinationTexture:destinationSlice:destinationLevel:destinationOrigin:)

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS*

```swift
func moveTextureMappings(sourceTexture: any MTLTexture, sourceSlice: Int, sourceLevel: Int, sourceOrigin: MTLOrigin, sourceSize: MTLSize, destinationTexture: any MTLTexture, destinationSlice: Int, destinationLevel: Int, destinationOrigin: MTLOrigin)
```

*Mac Catalyst, macOS*

```swift
optional func moveTextureMappings(sourceTexture: any MTLTexture, sourceSlice: Int, sourceLevel: Int, sourceOrigin: MTLOrigin, sourceSize: MTLSize, destinationTexture: any MTLTexture, destinationSlice: Int, destinationLevel: Int, destinationOrigin: MTLOrigin)
```

```objc
- (void) moveTextureMappingsFromTexture:(id<MTLTexture>) sourceTexture sourceSlice:(NSUInteger) sourceSlice sourceLevel:(NSUInteger) sourceLevel sourceOrigin:(MTLOrigin) sourceOrigin sourceSize:(MTLSize) sourceSize toTexture:(id<MTLTexture>) destinationTexture destinationSlice:(NSUInteger) destinationSlice destinationLevel:(NSUInteger) destinationLevel destinationOrigin:(MTLOrigin) destinationOrigin;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlresourcestatecommandencoder/movetexturemappings(sourcetexture:sourceslice:sourcelevel:sourceorigin:sourcesize:destinationtexture:destinationslice:destinationlevel:destinationorigin:))*