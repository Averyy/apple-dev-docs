# setBuffer(_:offset:index:)

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Encodes a reference to a buffer into the argument buffer.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func setBuffer(_ buffer: (any MTLBuffer)?, offset: Int, index: Int)
```

```objc
- (void) setBuffer:(id<MTLBuffer>) buffer offset:(NSUInteger) offset atIndex:(NSUInteger) index;
```

## Parameters

- `buffer`: A buffer the method encodes.
- `offset`: A byte offset for `buffer`.
- `index`: The index of a buffer within the argument buffer. The value corresponds to either the index ID of a declaration in Metal Shading Language (MSL) or the [`index`](../mtlargumentdescriptor/index.md) property of an [`MTLArgumentDescriptor`](../mtlargumentdescriptor.md) instance.

## See Also

### Encoding buffers
- [func setBuffers([(any MTLBuffer)?], offsets: [Int], range: Range<Int>)](./setbuffers%28_,offsets,range%29.md)
  Encodes references to an array of buffers into the argument buffer.
- [- setBuffers:offsets:withRange:](./setbuffers_offsets_withrange_.md)
  Encodes references to an array of buffers into the argument buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlargumentencoder/setbuffer(_:offset:index:))*