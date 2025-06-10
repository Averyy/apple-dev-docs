# resetTextureAccessCounters(_:region:mipLevel:slice:)

**Framework**: Metal  
**Kind**: method

Encodes a command that resets a sparse texture’s access data for a specific region, mipmap level, and slice.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
optional func resetTextureAccessCounters(_ texture: any MTLTexture, region: MTLRegion, mipLevel: Int, slice: Int)
```

## Parameters

- `texture`: A sparse texture instance.
- `region`: A region within the sparse texture’s  , in sparse tile coordinates.
- `mipLevel`: A mipmap level within the sparse texture.
- `slice`: A slice within the sparse texture.

## See Also

- [func getTextureAccessCounters(any MTLTexture, region: MTLRegion, mipLevel: Int, slice: Int, resetCounters: Bool, countersBuffer: any MTLBuffer, countersBufferOffset: Int)](mtlblitcommandencoder/gettextureaccesscounters(_:region:miplevel:slice:resetcounters:countersbuffer:countersbufferoffset:).md)
  Encodes a command that retrieves a sparse texture’s access data for a specific region, mipmap level, and slice.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlblitcommandencoder/resettextureaccesscounters(_:region:miplevel:slice:))*