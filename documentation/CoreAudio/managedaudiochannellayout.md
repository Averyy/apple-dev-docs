# ManagedAudioChannelLayout

**Framework**: Core Audio  
**Kind**: struct  
**Role**: Structure

This structure is used to specify channel layouts in files and hardware.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS
- watchOS 6.0+

## Declaration

```swift
struct ManagedAudioChannelLayout
```

## Topics

### Structures
- [ManagedAudioChannelLayout.ChannelDescriptions](./managedaudiochannellayout/channeldescriptions-swift.struct.md)
  A collection of `AudioChannelDescription`s.
### Initializers
- [init(audioChannelLayoutPointer: AudioChannelLayout.UnsafePointer, deallocator: (AudioChannelLayout.UnsafePointer) -> Void)](./managedaudiochannellayout/init%28audiochannellayoutpointer,deallocator%29.md)
  Creates a new `ManagedAudioChannelLayout` from an existing pointer to an `AudioChannelLayout`.
- [init(channelDescriptions: [AudioChannelDescription])](./managedaudiochannellayout/init%28channeldescriptions%29.md)
  Creates a new `ManagedAudioChannelLayout` from an array of `AudioChannelDescription`.
- [init(maximumDescriptions: Int)](./managedaudiochannellayout/init%28maximumdescriptions%29.md)
  Creates a new `ManagedAudioChannelLayout` that can hold up to `maximumDescriptions`.
- [init(tag: AudioChannelLayoutTag)](./managedaudiochannellayout/init%28tag%29.md)
  Creates a new `ManagedAudioChannelLayout` with a given tag.
### Instance Properties
- [var bitmap: AudioChannelBitmap](./managedaudiochannellayout/bitmap.md)
  If `tag` is set to `kAudioChannelLayoutTag_UseChannelBitmap`, this is the channel usage bitmap.
- [var channelDescriptions: ManagedAudioChannelLayout.ChannelDescriptions](./managedaudiochannellayout/channeldescriptions-swift.property.md)
  The `AudioChannelDescription`s that describe the layout.
- [var numberOfChannels: Int](./managedaudiochannellayout/numberofchannels.md)
  The number of channels described by this `ManagedAudioChannelLayout`.
- [var sizeInBytes: Int](./managedaudiochannellayout/sizeinbytes.md)
  The size, in bytes, of the backing `AudioChannelLayout`.
- [var tag: AudioChannelLayoutTag](./managedaudiochannellayout/tag.md)
  The `AudioChannelLayoutTag` that indicates the layout.
### Instance Methods
- [func setAllToUnknown()](./managedaudiochannellayout/setalltounknown%28%29.md)
  Sets all `AudioChannelDescriptions` to `kAudioChannelLabel_Unknown`.
- [func withUnsafeMutablePointer<Result>((UnsafeMutablePointer<AudioChannelLayout>) throws -> Result) rethrows -> Result](./managedaudiochannellayout/withunsafemutablepointer%28_%29.md)
  Calls a closure with a mutable pointer to the backing `AudioChannelLayout`.
- [func withUnsafePointer<Result>((UnsafePointer<AudioChannelLayout>) throws -> Result) rethrows -> Result](./managedaudiochannellayout/withunsafepointer%28_%29.md)
  Calls a closure with a pointer to the backing `AudioChannelLayout`.

## Relationships

### Conforms To
- [Equatable](../Swift/equatable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreaudio/managedaudiochannellayout)*