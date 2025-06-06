# NumBytesToNumAudioFileMarkers(_:)

**Framework**: Audio Toolbox  
**Kind**: func

A macro that returns the number of audio file markers represented by a specified number of bytes.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
func NumBytesToNumAudioFileMarkers(_ inNumBytes: Int) -> Int
```

#### Return Value

The number of audio file markers that can be contained in the specified number of bytes.

#### Discussion

Use this convenience macro when you call the [`AudioFileGetProperty(_:_:_:_:)`](audiofilegetproperty(_:_:_:_:).md) function with the [`kAudioFilePropertyMarkerList`](kaudiofilepropertymarkerlist.md) property to calculate the number of markers that will be returned.

## Parameters

- `inNumBytes`: The number of bytes for which you wish to know the equivalent number of audio file markers.

## See Also

- [func AudioFileGetProperty(AudioFileID, AudioFilePropertyID, UnsafeMutablePointer<UInt32>, UnsafeMutableRawPointer) -> OSStatus](audiofilegetproperty(_:_:_:_:).md)
  Gets the value of an audio file property.
- [func NextAudioFileRegion(UnsafePointer<AudioFileRegion>) -> UnsafeMutablePointer<AudioFileRegion>](nextaudiofileregion(_:).md)
  Finds the next audio file region in a region list.
- [func NumAudioFileMarkersToNumBytes(Int) -> Int](numaudiofilemarkerstonumbytes(_:).md)
  Returns the number of bytes corresponding to a specified number of audio file markers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/numbytestonumaudiofilemarkers(_:))*