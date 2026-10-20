# CAFPacketTableHeader

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
struct CAFPacketTableHeader
```

```c
struct CAFPacketTableHeader;
```

## Topics

### Initializers
- [init()](./cafpackettableheader/init%28%29.md)
- [init(mNumberPackets: Int64, mNumberValidFrames: Int64, mPrimingFrames: Int32, mRemainderFrames: Int32, mPacketDescriptions: UInt8)](./cafpackettableheader/init%28mnumberpackets,mnumbervalidframes,mprimingframes,mremainderframes,mpacketdescriptions%29.md)
### Instance Properties
- [var mNumberPackets: Int64](./cafpackettableheader/mnumberpackets.md)
- [var mNumberValidFrames: Int64](./cafpackettableheader/mnumbervalidframes.md)
- [var mPacketDescriptions: UInt8](./cafpackettableheader/mpacketdescriptions.md)
- [var mPrimingFrames: Int32](./cafpackettableheader/mprimingframes.md)
- [var mRemainderFrames: Int32](./cafpackettableheader/mremainderframes.md)

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
- [struct CAFFileHeader](./caffileheader.md)
- [struct CAFFormatFlags](./cafformatflags.md)
- [struct CAFInfoStrings](./cafinfostrings.md)
- [struct CAFInstrumentChunk](./cafinstrumentchunk.md)
- [struct CAFMarker](./cafmarker.md)
- [struct CAFMarkerChunk](./cafmarkerchunk.md)
- [struct CAFOverviewChunk](./cafoverviewchunk.md)
- [struct CAFOverviewSample](./cafoverviewsample.md)
- [struct CAFPeakChunk](./cafpeakchunk.md)
- [struct CAFPositionPeak](./cafpositionpeak.md)
- [struct CAFRegion](./cafregion.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/cafpackettableheader)*