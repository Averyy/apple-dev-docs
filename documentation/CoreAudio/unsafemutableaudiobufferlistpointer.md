# UnsafeMutableAudioBufferListPointer

**Framework**: Core Audio  
**Kind**: struct

A wrapper for a pointer to an `AudioBufferList`.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
struct UnsafeMutableAudioBufferListPointer
```

#### Overview

Like `UnsafeMutablePointer`, this type provides no automated memory management and the user must therefore take care to allocate and free memory appropriately.

## Topics

### Initializers
- [init(UnsafeMutablePointer<AudioBufferList>)](unsafemutableaudiobufferlistpointer/init(_:)-4a7c5.md)
  Construct from an `AudioBufferList` pointer.
- [init?(UnsafeMutablePointer<AudioBufferList>?)](unsafemutableaudiobufferlistpointer/init(_:)-6qwfh.md)
  Construct from an `AudioBufferList` pointer.
### Instance Properties
- [var count: Int](unsafemutableaudiobufferlistpointer/count.md)
  The number of `AudioBuffer`s in the `AudioBufferList` (`mNumberBuffers`).
- [var unsafeMutablePointer: UnsafeMutablePointer<AudioBufferList>](unsafemutableaudiobufferlistpointer/unsafemutablepointer.md)
  The pointer to the wrapped `AudioBufferList`.
- [var unsafePointer: UnsafePointer<AudioBufferList>](unsafemutableaudiobufferlistpointer/unsafepointer.md)
  The pointer to the wrapped `AudioBufferList`.
### Default Implementations
- [MutableCollection Implementations](unsafemutableaudiobufferlistpointer/mutablecollection-implementations.md)
- [RandomAccessCollection Implementations](unsafemutableaudiobufferlistpointer/randomaccesscollection-implementations.md)

## Relationships

### Conforms To
- [BidirectionalCollection](../Swift/BidirectionalCollection.md)
- [Collection](../Swift/Collection.md)
- [Copyable](../Swift/Copyable.md)
- [MutableCollection](../Swift/MutableCollection.md)
- [RandomAccessCollection](../Swift/RandomAccessCollection.md)
- [Sequence](../Swift/Sequence.md)

## See Also

- [struct AudioHardwareIOProcStreamUsage](audiohardwareioprocstreamusage.md)
  This structure describes which streams a given AudioDeviceIOProc will use. It is used in conjunction with kAudioDevicePropertyIOProcStreamUsage.
- [struct AudioObjectPropertyAddress](audioobjectpropertyaddress.md)
  An AudioObjectPropertyAddress collects the three parts that identify a specific property together in a struct for easy transmission.
- [struct AudioStreamRangedDescription](audiostreamrangeddescription.md)
  This structure allows a specific sample rate range to be associated with an AudioStreamBasicDescription that specifies its sample rate as kAudioStreamAnyRate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreaudio/unsafemutableaudiobufferlistpointer)*