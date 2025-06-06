# MESampleCursor

**Framework**: MediaExtension  
**Kind**: protocol

A protocol that defines the information to provide about samples within a track of a media asset, and enables stepping through samples in the track in decode or presentation order.

**Availability**:
- macOS 14.0+

## Declaration

```swift
protocol MESampleCursor : NSCopying, NSObjectProtocol
```

#### Overview

This object delivers sample data either by providing sample location and sample chunk information, or by directly generating a sample buffer.

##### Delivering Sample Data

An [`MESampleCursor`](mesamplecursor.md) object can return sample data to [`Core Media`](https://developer.apple.com/documentation/CoreMedia) in two ways:

- Return information about the sample data location in the media and let Core Media read the data.
- Read the data and return sample buffers directly.

Review the following information that explains these approaches and which one to use for typical scenarios.

###### Allowing Core Media to Read the Sample Data

This is the preferred method to deliver sample data. It allows Core Media to optimize data I/O read operations, and potentially combine multiple smaller reads into a single larger read for better performance. There are four methods available to deliver the required sample location information:

1. [`sampleLocation()`](mesamplecursor/samplelocation().md)

This is the baseline method to return sample location information. For formats with individually-stored samples such as video, Core Media calls this method to find each sample location.

1. [`chunkDetails()`](mesamplecursor/chunkdetails().md)

For formats with samples stored in groups, blocks, or chunks such as audio, use this method to indicate details about the number of samples stored in each group. After determining the chunk information, Core Media calls [`sampleLocation()`](mesamplecursor/samplelocation().md) to locate individual samples within the chunk. [`MESampleCursor`](mesamplecursor.md) objects for these formats need to implement both [`sampleLocation()`](mesamplecursor/samplelocation().md) and [`chunkDetails()`](mesamplecursor/chunkdetails().md).

1. [`estimatedSampleLocation()`](mesamplecursor/estimatedsamplelocation().md)

In some cases it’s not possible to directly determine the sample location and return it through [`sampleLocation()`](mesamplecursor/samplelocation().md). Instead, there’s a two-step process to determine the sample location: call [`estimatedSampleLocation()`](mesamplecursor/estimatedsamplelocation().md) to obtain a coarse estimation, and then call [`refineSampleLocation(_:refinementData:refinementDataLength:refinedLocation:)`](mesamplecursor/refinesamplelocation(_:refinementdata:refinementdatalength:refinedlocation:).md) to find the exact location. Implement both methods to support this approach.

1. [`refineSampleLocation(_:refinementData:refinementDataLength:refinedLocation:)`](mesamplecursor/refinesamplelocation(_:refinementdata:refinementdatalength:refinedlocation:).md)

This method returns the exact sample location information as a second step after it receives the coarse estimate from [`estimatedSampleLocation()`](mesamplecursor/estimatedsamplelocation().md). Implement both methods to support this approach.

###### Reading the Sample Buffers Directly

When it’s not possible to let Core Media read the sample data using location information, the [`MESampleCursor`](mesamplecursor.md) object needs to read the sample data itself using the [`MEByteSource`](mebytesource.md) to deliver the sample data buffers. This is less efficient for data I/O because there’s no way for Core Media to optimize read operations.

The method [`loadSampleBufferContainingSamples(to:completionHandler:)`](mesamplecursor/loadsamplebuffercontainingsamples(to:completionhandler:).md) delivers sample data buffers directly, so it allows the [`MESampleCursor`](mesamplecursor.md) object flexibility to read and unpack the samples from the media. The sample cursor needs to use the [`MEByteSource`](mebytesource.md) directly to seek and read in the sample data. This method can deliver sample buffers either with one sample, such as for video tracks, or with blocks of samples, such as for audio tracks. It’s also suitable for use with synthesized samples that use metadata from the media, such as for timecode tracks.

###### Choosing the Best Approach

Choose the best approach in these typical scenarios:

1. The media stores the samples in groups interleaved among other samples.

The `MESampleCursor` object implements [`sampleLocation()`](mesamplecursor/samplelocation().md) and [`chunkDetails()`](mesamplecursor/chunkdetails().md) to allow Core Media to locate the chunks and find samples inside the chunks.

1. The media stores the samples in blocks interleaved among other samples, but some blocks are non-contiguous.

The `MESampleCursor` object implements [`sampleLocation()`](mesamplecursor/samplelocation().md), [`chunkDetails()`](mesamplecursor/chunkdetails().md), and [`loadSampleBufferContainingSamples(to:completionHandler:)`](mesamplecursor/loadsamplebuffercontainingsamples(to:completionhandler:).md). For contiguous samples, [`sampleLocation()`](mesamplecursor/samplelocation().md) returns the samples to read. For non-contiguous samples, [`sampleLocation()`](mesamplecursor/samplelocation().md) fails with the error [`MEError.Code.locationNotAvailable`](meerror-swift.struct/code/locationnotavailable.md) and Core Media then uses [`loadSampleBufferContainingSamples(to:completionHandler:)`](mesamplecursor/loadsamplebuffercontainingsamples(to:completionhandler:).md) to read the samples.

1. It’s not possible to determine sample location in one step.

The `MESampleCursor` object implements [`estimatedSampleLocation()`](mesamplecursor/estimatedsamplelocation().md) and [`refineSampleLocation(_:refinementData:refinementDataLength:refinedLocation:)`](mesamplecursor/refinesamplelocation(_:refinementdata:refinementdatalength:refinedlocation:).md) (instead of [`sampleLocation()`](mesamplecursor/samplelocation().md)). If it’s not possible to determine the sample location using either the one-step or two-step approach, the `MESampleCursor` object implements [`loadSampleBufferContainingSamples(to:completionHandler:)`](mesamplecursor/loadsamplebuffercontainingsamples(to:completionhandler:).md) to directly deliver sample buffers.

1. It’s necessary to unpack or prepare sample data before delivering it.

If Core Media can’t directly read the sample data, then the `MESampleCursor` object implements [`loadSampleBufferContainingSamples(to:completionHandler:)`](mesamplecursor/loadsamplebuffercontainingsamples(to:completionhandler:).md) to read the data itself, unpack or prepare it, and deliver it in sample buffers.

## Topics

### Inspecting a sample cursor
- [var presentationTimeStamp: CMTime](mesamplecursor/presentationtimestamp.md)
  The presentation timestamp (PTS) of the sample at the current position of the cursor.
- [var decodeTimeStamp: CMTime](mesamplecursor/decodetimestamp.md)
  The decode timestamp (DTS) of the sample at the current position of the cursor.
- [var currentSampleDuration: CMTime](mesamplecursor/currentsampleduration.md)
  The decode duration of the sample at the current position.
- [var currentSampleFormatDescription: CMFormatDescription?](mesamplecursor/currentsampleformatdescription.md)
  The format description for the sample at the current position of the cursor.
- [var syncInfo: AVSampleCursorSyncInfo](mesamplecursor/syncinfo.md)
  Decoder synchronization information about the sample the cursor points to.
- [var dependencyInfo: AVSampleCursorDependencyInfo](mesamplecursor/dependencyinfo.md)
  Dependency information about the sample the cursor points to.
- [var hevcDependencyInfo: MEHEVCDependencyInfo](mesamplecursor/hevcdependencyinfo.md)
  Additional information that’s necessary to recover complete sample dependency information.
- [var decodeTimeOfLastSampleReachableByForwardSteppingThatIsAlreadyLoadedByByteSource: CMTime](mesamplecursor/decodetimeoflastsamplereachablebyforwardsteppingthatisalreadyloadedbybytesource.md)
  The duration of the playable content starting from the cursor position.
### Stepping through samples
- [func samplesWithEarlierDTSsMayHaveLaterPTSs(than: any MESampleCursor) -> Bool](mesamplecursor/sampleswithearlierdtssmayhavelaterptss(than:).md)
  Tests for an earlier boundary in sample reordering.
- [func samplesWithLaterDTSsMayHaveEarlierPTSs(than: any MESampleCursor) -> Bool](mesamplecursor/sampleswithlaterdtssmayhaveearlierptss(than:).md)
  Tests for a later boundary in sample reordering.
- [func estimatedSampleLocation() throws -> MEEstimatedSampleLocation](mesamplecursor/estimatedsamplelocation.md)
  Returns an estimate of the sample location indicated by the cursor.
- [func refineSampleLocation(AVSampleCursorStorageRange, refinementData: UnsafePointer<UInt8>, refinementDataLength: Int, refinedLocation: UnsafeMutablePointer<AVSampleCursorStorageRange>) throws](mesamplecursor/refinesamplelocation(_:refinementdata:refinementdatalength:refinedlocation:).md)
  Produces an exact sample location based on the estimated sample location and refinement data that you specify.
- [func stepByDecodeTime(CMTime, completionHandler: (CMTime, Bool, (any Error)?) -> Void)](mesamplecursor/stepbydecodetime(_:completionhandler:).md)
  Moves the cursor on the decode timeline by the delta decode time that you specify.
- [func stepByPresentationTime(CMTime, completionHandler: (CMTime, Bool, (any Error)?) -> Void)](mesamplecursor/stepbypresentationtime(_:completionhandler:).md)
  Moves the cursor on the presentation timeline by the delta presentation time that you specify.
- [func stepInDecodeOrder(by: Int64, completionHandler: (Int64, (any Error)?) -> Void)](mesamplecursor/stepindecodeorder(by:completionhandler:).md)
  Moves the cursor a given number of samples in decode order.
- [func stepInPresentationOrder(by: Int64, completionHandler: (Int64, (any Error)?) -> Void)](mesamplecursor/stepinpresentationorder(by:completionhandler:).md)
  Moves the cursor a given number of samples in presentation order.
### Sending samples to a pipeline
- [func chunkDetails() throws -> MESampleCursorChunk](mesamplecursor/chunkdetails.md)
  Returns information about the chunk that holds the sample indicated by the cursor.
- [func sampleLocation() throws -> MESampleLocation](mesamplecursor/samplelocation.md)
  Returns the location and byte source of the sample indicated by the cursor.
- [func loadSampleBufferContainingSamples(to: (any MESampleCursor)?, completionHandler: (CMSampleBuffer?, (any Error)?) -> Void)](mesamplecursor/loadsamplebuffercontainingsamples(to:completionhandler:).md)
  Builds a sample buffer that contains the samples at the cursor that you specify.
### RAW processing metadata
- [func loadPostDecodeProcessingMetadata(completionHandler: ([String : any Sendable]?, (any Error)?) -> Void)](mesamplecursor/loadpostdecodeprocessingmetadata(completionhandler:).md)
  Asynchronously loads a dictionary that represents frame level metadata for post decode processing.

## Relationships

### Inherits From
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class MESampleLocation](mesamplelocation.md)
  An object that provides information about the sample location with the media.
- [class MESampleCursorChunk](mesamplecursorchunk.md)
  An object that provides information about the chunk of media at the location of a sample.
- [class MEEstimatedSampleLocation](meestimatedsamplelocation.md)
  An object that provides information about the estimated sample location with the media.
- [class MEHEVCDependencyInfo](mehevcdependencyinfo.md)
  An object that provides information about the HEVC dependency attributes of a sample.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaextension/mesamplecursor)*