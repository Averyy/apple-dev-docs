# setTextureView(buffer:descriptor:offset:bytesPerRow:index:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Creates a new lightweight texture view of a buffer.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
func setTextureView(buffer: any MTLBuffer, descriptor: MTLTextureDescriptor, offset: Int, bytesPerRow: Int, index: Int) -> MTLResourceID
```

#### Return Value

The [`MTLResourceID`](mtlresourceid.md) of a new buffer view in this pool.

#### Discussion

This method creates a lightweight texture view over a buffer, according to a descriptor you provide. It then associates the texture view with a slot in this texture view pool at the index you specify.

## Parameters

- `buffer`: An   instance for which to create a new texture view.
- `descriptor`: A descriptor specifying properties of the texture view to create.
- `offset`: A byte offset, within the   parameter, at which the data for the texture view starts.
- `bytesPerRow`: The number of bytes between adjacent rows of pixels in the source buffer’s memory.
- `index`: An index of a slot in the table into which this method writes the new texture view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtltextureviewpool/settextureview(buffer:descriptor:offset:bytesperrow:index:))*