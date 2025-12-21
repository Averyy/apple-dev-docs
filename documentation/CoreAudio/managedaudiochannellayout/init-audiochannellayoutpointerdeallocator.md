# init(audioChannelLayoutPointer:deallocator:)

**Framework**: Core Audio  
**Kind**: init

Creates a new `ManagedAudioChannelLayout` from an existing pointer to an `AudioChannelLayout`.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst ?+
- macOS 10.15+
- tvOS 13.0+
- visionOS ?+
- watchOS 6.0+

## Declaration

```swift
init(audioChannelLayoutPointer: AudioChannelLayout.UnsafePointer, deallocator: @escaping (AudioChannelLayout.UnsafePointer) -> Void)
```

#### Discussion

Any mutation on the new `ManagedAudioChannelLayout` will perform a copy of the `audioChannelLayoutPointer` values.

## Parameters

- `audioChannelLayoutPointer`: A pointer to an existing   .
- `deallocator`: A closure that will be called when    is no longer used.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreaudio/managedaudiochannellayout/init(audiochannellayoutpointer:deallocator:))*