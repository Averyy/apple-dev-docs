# NumAudioFileMarkersToNumBytes(_:)

**Framework**: Audio Toolbox  
**Kind**: func  
**Role**: Function

Returns the number of bytes corresponding to a specified number of audio file markers.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
func NumAudioFileMarkersToNumBytes(_ inNumMarkers: Int) -> Int
```

```c
static size_t NumAudioFileMarkersToNumBytes(size_t inNumMarkers);
```

#### Return Value

The number of bytes required to contain the specified number of audio file markers.

#### Discussion

Use this convenience function when you call the [`AudioFileSetProperty(_:_:_:_:)`](./audiofilesetproperty%28_,_,_,_%29.md) function with the [`kAudioFilePropertyMarkerList`](./kaudiofilepropertymarkerlist.md) property to calculate the size of buffer needed to hold a specific number of audio file markers.

## Parameters

- `inNumMarkers`: The number of audio file markers for which you wish to know the equivalent number of bytes.

## See Also

### Related Documentation
- [func AudioFileSetProperty(AudioFileID, AudioFilePropertyID, UInt32, UnsafeRawPointer) -> OSStatus](./audiofilesetproperty%28_,_,_,_%29.md)
  Sets the value of an audio file property
### Parsing Audio File Content
- [func NextAudioFileRegion(UnsafePointer<AudioFileRegion>) -> UnsafeMutablePointer<AudioFileRegion>](./nextaudiofileregion%28_%29.md)
  Finds the next audio file region in a region list.
- [func NumBytesToNumAudioFileMarkers(Int) -> Int](./numbytestonumaudiofilemarkers%28_%29.md)
  A macro that returns the number of audio file markers represented by a specified number of bytes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/numaudiofilemarkerstonumbytes(_:))*