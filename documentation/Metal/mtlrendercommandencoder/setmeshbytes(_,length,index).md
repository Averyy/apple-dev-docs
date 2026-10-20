# setMeshBytes(_:length:index:)

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Creates a buffer from bytes and assigns it to an entry in the mesh shader argument table.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func setMeshBytes(_ bytes: UnsafeRawPointer, length: Int, index: Int)
```

```objc
- (void) setMeshBytes:(const void *) bytes length:(NSUInteger) length atIndex:(NSUInteger) index;
```

#### Discussion

The method is equivalent to creating an [`MTLBuffer`](../mtlbuffer.md) instance that contains the same data as `bytes` and calling the [`setMeshBuffer(_:offset:index:)`](./setmeshbuffer%28_,offset,index%29.md) method. However, this method avoids the overhead of creating a buffer to store your data; instead, Metal manages the data.

> ❗ **Important**:  Only call this method for single-use data that’s smaller than 4 KB.

For data that’s more than 4 KB, create an [`MTLBuffer`](../mtlbuffer.md) instance and pass it to [`setMeshBufferOffset(_:index:)`](./setmeshbufferoffset%28_,index%29.md).

## Parameters

- `bytes`: A pointer to argument data the method copies to an [`MTLBuffer`](../mtlbuffer.md) and assigns to an entry in the mesh shader argument table for buffers.
- `length`: The number of bytes the method copies from the `bytes` pointer.
- `index`: An integer that represents the entry in the mesh shader argument table for buffers that stores a record of the [`MTLBuffer`](../mtlbuffer.md) the method creates from `bytes`.

## See Also

### Assigning buffers for mesh shaders
- [func setMeshBuffer((any MTLBuffer)?, offset: Int, index: Int)](./setmeshbuffer%28_,offset,index%29.md)
  Assigns a buffer to an entry in the mesh shader argument table.
- [func setMeshBuffers([(any MTLBuffer)?], offsets: [Int], range: Range<Int>)](./setmeshbuffers%28_,offsets,range%29.md)
  Assigns multiple buffers to a range of entries in the mesh shader argument table.
- [func setMeshBufferOffset(Int, index: Int)](./setmeshbufferoffset%28_,index%29.md)
  Updates an entry in the mesh shader argument table with a new location within the entry’s current buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/setmeshbytes(_:length:index:))*