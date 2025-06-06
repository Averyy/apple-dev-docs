# NumAudioFileMarkersToNumBytes(_:)

**Framework**: Audio Toolbox  
**Kind**: func

Returns the number of bytes corresponding to a specified number of audio file markers.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
func NumAudioFileMarkersToNumBytes(_ inNumMarkers: Int) -> Int
```

#### Return Value

The number of bytes required to contain the specified number of audio file markers.

#### Discussion

Use this convenience function when you call the [`AudioFileSetProperty(_:_:_:_:)`](audiofilesetproperty(_:_:_:_:).md) function with the [`kAudioFilePropertyMarkerList`](kaudiofilepropertymarkerlist.md) property to calculate the size of buffer needed to hold a specific number of audio file markers.

## Parameters

- `inNumMarkers`: The number of audio file markers for which you wish to know the equivalent number of bytes.

## See Also

- [func AudioFileSetProperty(AudioFileID, AudioFilePropertyID, UInt32, UnsafeRawPointer) -> OSStatus](audiofilesetproperty(_:_:_:_:).md)
  Sets the value of an audio file property
- [func NextAudioFileRegion(UnsafePointer<AudioFileRegion>) -> UnsafeMutablePointer<AudioFileRegion>](nextaudiofileregion(_:).md)
  Finds the next audio file region in a region list.
- [func NumBytesToNumAudioFileMarkers(Int) -> Int](numbytestonumaudiofilemarkers(_:).md)
  A macro that returns the number of audio file markers represented by a specified number of bytes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/numaudiofilemarkerstonumbytes(_:))*