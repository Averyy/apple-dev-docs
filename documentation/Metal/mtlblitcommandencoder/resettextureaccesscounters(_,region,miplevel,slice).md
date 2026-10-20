# resetTextureAccessCounters(_:region:mipLevel:slice:)

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method

Encodes a command that resets a sparse texture’s access data for a specific region, mipmap level, and slice.

**Availability**:
- iOS 13.0+ - Deprecated in 26.4
- iPadOS 13.0+ - Deprecated in 26.4
- Mac Catalyst 14.0+ - Deprecated in 26.4
- macOS 11.0+ - Deprecated in 26.4
- tvOS 16.0+ - Deprecated in 26.4
- visionOS 1.0+ - Deprecated in 26.4

> **Deprecated**: Access counters are no longer supported in Metal

## Declaration

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS*

```swift
func resetTextureAccessCounters(_ texture: any MTLTexture, region: MTLRegion, mipLevel: Int, slice: Int)
```

*Mac Catalyst, macOS*

```swift
optional func resetTextureAccessCounters(_ texture: any MTLTexture, region: MTLRegion, mipLevel: Int, slice: Int)
```

```objc
- (void) resetTextureAccessCounters:(id<MTLTexture>) texture region:(MTLRegion) region mipLevel:(NSUInteger) mipLevel slice:(NSUInteger) slice;
```

## Parameters

- `texture`: A sparse texture instance.
- `region`: A region within the sparse texture’s `mipLevel`, in sparse tile coordinates.
- `mipLevel`: A mipmap level within the sparse texture.
- `slice`: A slice within the sparse texture.

## See Also

### Managing sparse texture access counters
- [func getTextureAccessCounters(any MTLTexture, region: MTLRegion, mipLevel: Int, slice: Int, resetCounters: Bool, countersBuffer: any MTLBuffer, countersBufferOffset: Int)](./gettextureaccesscounters%28_,region,miplevel,slice,resetcounters,countersbuffer,countersbufferoffset%29.md)
  Encodes a command that retrieves a sparse texture’s access data for a specific region, mipmap level, and slice.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlblitcommandencoder/resettextureaccesscounters(_:region:miplevel:slice:))*