# CAFFileHeader

**Framework**: Audio Toolbox  
**Kind**: struct  
**Role**: Structure

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
struct CAFFileHeader
```

```c
struct CAFFileHeader;
```

## Topics

### Initializers
- [init()](./caffileheader/init%28%29.md)
- [init(mFileType: UInt32, mFileVersion: UInt16, mFileFlags: UInt16)](./caffileheader/init%28mfiletype,mfileversion,mfileflags%29.md)
### Instance Properties
- [var mFileFlags: UInt16](./caffileheader/mfileflags.md)
- [var mFileType: UInt32](./caffileheader/mfiletype.md)
- [var mFileVersion: UInt16](./caffileheader/mfileversion.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Sendable](../Swift/sendable.md)

## See Also

### File Structure
- [struct CAFAudioDescription](./cafaudiodescription.md)
- [struct CAFAudioFormatListItem](./cafaudioformatlistitem.md)
- [struct CAFChunkHeader](./cafchunkheader.md)
- [struct CAFDataChunk](./cafdatachunk.md)
- [struct CAFFormatFlags](./cafformatflags.md)
- [struct CAFInfoStrings](./cafinfostrings.md)
- [struct CAFInstrumentChunk](./cafinstrumentchunk.md)
- [struct CAFMarker](./cafmarker.md)
- [struct CAFMarkerChunk](./cafmarkerchunk.md)
- [struct CAFOverviewChunk](./cafoverviewchunk.md)
- [struct CAFOverviewSample](./cafoverviewsample.md)
- [struct CAFPacketTableHeader](./cafpackettableheader.md)
- [struct CAFPeakChunk](./cafpeakchunk.md)
- [struct CAFPositionPeak](./cafpositionpeak.md)
- [struct CAFRegion](./cafregion.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/caffileheader)*