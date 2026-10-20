# NumBytesToNumAudioFileMarkers(_:)

**Framework**: Audio Toolbox  
**Kind**: func  
**Role**: Function

A macro that returns the number of audio file markers represented by a specified number of bytes.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
func NumBytesToNumAudioFileMarkers(_ inNumBytes: Int) -> Int
```

```c
static size_t NumBytesToNumAudioFileMarkers(size_t inNumBytes);
```

#### Return Value

The number of audio file markers that can be contained in the specified number of bytes.

#### Discussion

Use this convenience macro when you call the [`AudioFileGetProperty(_:_:_:_:)`](./audiofilegetproperty%28_,_,_,_%29.md) function with the [`kAudioFilePropertyMarkerList`](./kaudiofilepropertymarkerlist.md) property to calculate the number of markers that will be returned.

## Parameters

- `inNumBytes`: The number of bytes for which you wish to know the equivalent number of audio file markers.

## See Also

### Related Documentation
- [func AudioFileGetProperty(AudioFileID, AudioFilePropertyID, UnsafeMutablePointer<UInt32>, UnsafeMutableRawPointer) -> OSStatus](./audiofilegetproperty%28_,_,_,_%29.md)
  Gets the value of an audio file property.
### Parsing Audio File Content
- [func NextAudioFileRegion(UnsafePointer<AudioFileRegion>) -> UnsafeMutablePointer<AudioFileRegion>](./nextaudiofileregion%28_%29.md)
  Finds the next audio file region in a region list.
- [func NumAudioFileMarkersToNumBytes(Int) -> Int](./numaudiofilemarkerstonumbytes%28_%29.md)
  Returns the number of bytes corresponding to a specified number of audio file markers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/numbytestonumaudiofilemarkers(_:))*