# getTextureAccessCounters(_:region:mipLevel:slice:resetCounters:countersBuffer:countersBufferOffset:)

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method

Encodes a command that retrieves a sparse texture’s access data for a specific region, mipmap level, and slice.

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
func getTextureAccessCounters(_ texture: any MTLTexture, region: MTLRegion, mipLevel: Int, slice: Int, resetCounters: Bool, countersBuffer: any MTLBuffer, countersBufferOffset: Int)
```

*Mac Catalyst, macOS*

```swift
optional func getTextureAccessCounters(_ texture: any MTLTexture, region: MTLRegion, mipLevel: Int, slice: Int, resetCounters: Bool, countersBuffer: any MTLBuffer, countersBufferOffset: Int)
```

```objc
- (void) getTextureAccessCounters:(id<MTLTexture>) texture region:(MTLRegion) region mipLevel:(NSUInteger) mipLevel slice:(NSUInteger) slice resetCounters:(BOOL) resetCounters countersBuffer:(id<MTLBuffer>) countersBuffer countersBufferOffset:(NSUInteger) countersBufferOffset;
```

#### Discussion

The GPU returns a counter for each sparse tile in the region you specify. Each counter is a [`uint32_t`](../../kernel/uint32_t.md) in row-major order. Provide space in the buffer for each counter you request.

When the GPU samples a texture and fails to find data in its internal caches, the GPU increments the access counter for the sparse tile. The GPU then attempts to fetch a new cache line from device memory that contains those pixels.

The counter doesn’t track memory operations to data that’s already in the GPU’s caches. You can ignore differences in cache line sizes or pixel formats because the GPU driver normalizes the access counts. Each count represents the number of pixels the GPU fetches into memory.

## Parameters

- `texture`: A sparse texture instance.
- `region`: A region within the sparse texture’s `mipLevel`, in sparse tile coordinates.
- `mipLevel`: A mipmap level within the sparse texture.
- `slice`: A slice within the sparse texture.
- `resetCounters`: A Boolean value that indicates whether the command resets the counters after it completes.
- `countersBuffer`: A destination buffer where the command stores the sparse texture’s access counter data.
- `countersBufferOffset`: A starting offset, in bytes, within `countersBuffer` where the command writes the first byte of the sparse texture’s access counter data.

## See Also

### Managing sparse texture access counters
- [func resetTextureAccessCounters(any MTLTexture, region: MTLRegion, mipLevel: Int, slice: Int)](./resettextureaccesscounters%28_,region,miplevel,slice%29.md)
  Encodes a command that resets a sparse texture’s access data for a specific region, mipmap level, and slice.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlblitcommandencoder/gettextureaccesscounters(_:region:miplevel:slice:resetcounters:countersbuffer:countersbufferoffset:))*