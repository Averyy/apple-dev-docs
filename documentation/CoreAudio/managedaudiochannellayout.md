# ManagedAudioChannelLayout

**Framework**: Core Audio  
**Kind**: struct

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
struct ManagedAudioChannelLayout
```

## Topics

### Structures
- [ManagedAudioChannelLayout.ChannelDescriptions](managedaudiochannellayout/channeldescriptions-swift.struct.md)
### Initializers
- [init(audioChannelLayoutPointer: AudioChannelLayout.UnsafePointer, deallocator: (AudioChannelLayout.UnsafePointer) -> Void)](managedaudiochannellayout/init(audiochannellayoutpointer:deallocator:).md)
- [init(channelDescriptions: [AudioChannelDescription])](managedaudiochannellayout/init(channeldescriptions:).md)
- [init(maximumDescriptions: Int)](managedaudiochannellayout/init(maximumdescriptions:).md)
- [init(tag: AudioChannelLayoutTag)](managedaudiochannellayout/init(tag:).md)
### Instance Properties
- [var bitmap: AudioChannelBitmap](managedaudiochannellayout/bitmap.md)
- [var channelDescriptions: ManagedAudioChannelLayout.ChannelDescriptions](managedaudiochannellayout/channeldescriptions-swift.property.md)
- [var numberOfChannels: Int](managedaudiochannellayout/numberofchannels.md)
- [var sizeInBytes: Int](managedaudiochannellayout/sizeinbytes.md)
- [var tag: AudioChannelLayoutTag](managedaudiochannellayout/tag.md)
### Instance Methods
- [func setAllToUnknown()](managedaudiochannellayout/setalltounknown.md)
- [func withUnsafeMutablePointer<Result>((UnsafeMutablePointer<AudioChannelLayout>) throws -> Result) rethrows -> Result](managedaudiochannellayout/withunsafemutablepointer(_:).md)
- [func withUnsafePointer<Result>((UnsafePointer<AudioChannelLayout>) throws -> Result) rethrows -> Result](managedaudiochannellayout/withunsafepointer(_:).md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreaudio/managedaudiochannellayout)*