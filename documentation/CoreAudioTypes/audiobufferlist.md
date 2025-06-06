# AudioBufferList

**Framework**: Core Audio Types  
**Kind**: struct

A structure that stores a variable-length array of audio buffers.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
struct AudioBufferList
```

## Topics

### Creating a Buffer List
- [init()](audiobufferlist/init.md)
  Creates an empty audio buffer list.
- [init(mNumberBuffers: UInt32, mBuffers: AudioBuffer)](audiobufferlist/init(mnumberbuffers:mbuffers:).md)
  Creates an audio buffer list with audio buffers.
### Accessing the Data
- [var mNumberBuffers: UInt32](audiobufferlist/mnumberbuffers.md)
  The number of audio buffers in the list.
- [var mBuffers: AudioBuffer](audiobufferlist/mbuffers.md)
  A variable-length array of audio buffers.
### Type Methods
- [static func allocate(maximumBuffers: Int) -> UnsafeMutableAudioBufferListPointer](audiobufferlist/allocate(maximumbuffers:).md)
  Allocate an `AudioBufferList` with a capacity for the specified number of `AudioBuffer`s.
- [static func sizeInBytes(maximumBuffers: Int) -> Int](audiobufferlist/sizeinbytes(maximumbuffers:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)

## See Also

- [struct AudioBuffer](audiobuffer.md)
  A structure that holds a buffer of audio data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreaudiotypes/audiobufferlist)*