# NextAudioFileRegion(_:)

**Framework**: Audio Toolbox  
**Kind**: func

Finds the next audio file region in a region list.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
func NextAudioFileRegion(_ inAFRegionPtr: UnsafePointer<AudioFileRegion>) -> UnsafeMutablePointer<AudioFileRegion>
```

#### Return Value

A pointer to the next region after the region pointed to by the `inAFRegionPtr` parameter. This value can be beyond the end of the list, so pay attention to the total number of regions in the list.

#### Discussion

Because audio file regions are of variable length, you cannot easily walk the list. Use this convenience function when you call the [`AudioFileGetProperty(_:_:_:_:)`](audiofilegetproperty(_:_:_:_:).md) function with the [`kAudioFilePropertyRegionList`](kaudiofilepropertyregionlist.md) property to walk through the list of regions returned.

## Parameters

- `inAFRegionPtr`: A pointer to an audio file region in the region list.

## See Also

- [func AudioFileSetProperty(AudioFileID, AudioFilePropertyID, UInt32, UnsafeRawPointer) -> OSStatus](audiofilesetproperty(_:_:_:_:).md)
  Sets the value of an audio file property
- [func NumAudioFileMarkersToNumBytes(Int) -> Int](numaudiofilemarkerstonumbytes(_:).md)
  Returns the number of bytes corresponding to a specified number of audio file markers.
- [func NumBytesToNumAudioFileMarkers(Int) -> Int](numbytestonumaudiofilemarkers(_:).md)
  A macro that returns the number of audio file markers represented by a specified number of bytes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/nextaudiofileregion(_:))*