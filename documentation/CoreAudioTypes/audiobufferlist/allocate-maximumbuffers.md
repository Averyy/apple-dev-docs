# allocate(maximumBuffers:)

**Framework**: Core Audio Types  
**Kind**: method

Allocate an `AudioBufferList` with a capacity for the specified number of `AudioBuffer`s.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
static func allocate(maximumBuffers: Int) -> UnsafeMutableAudioBufferListPointer
```

#### Discussion

The `count` property of the new `AudioBufferList` is initialized to `maximumBuffers`.

The memory should be freed with `free()`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreaudiotypes/audiobufferlist/allocate(maximumbuffers:))*