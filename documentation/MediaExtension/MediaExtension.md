# MediaExtension

**Framework**: MediaExtension  
**Kind**: module

This framework provides a means for developers to create format readers, video decoders, and RAW processors for media that the system doesn’t natively support.

**Availability**:
- Mac Catalyst 18.0+
- macOS 15.0+

#### Overview

MediaExtension format readers encapsulate media assets that the system doesn’t natively support so that the system can recognize them. MediaExtension video decoders decode video formats that the system doesn’t natively support. MediaExtension RAW processors work together with video decoders to allow direct control over the RAW decoding process. Developers need to build format readers, video decoders, and RAW processors as [`ExtensionKit`](https://developer.apple.com/documentation/ExtensionKit) bundles and embed them in a host app. Once a user installs and runs the host app, the embedded extensions become available to any app on the user’s system that opts in to using them.

## Topics

### Format readers
- [protocol MEFormatReader](meformatreader.md)
  A protocol that defines the requirements for a format reader, which represents a single media asset.
- [protocol MEFormatReaderExtension](meformatreaderextension.md)
  A protocol that defines a factory to create a new format reader with a byte source.
- [class MEFormatReaderInstantiationOptions](meformatreaderinstantiationoptions.md)
  An object that contains options to pass to a format reader extension.
- [class MEFileInfo](mefileinfo.md)
  An object that contains file properties from the media asset.
- [Format reader property list dictionaries](format-reader-property-list-dictionaries.md)
  Include property list dictionaries to describe a format reader and register the formats it supports.
- [Format reader entitlement](format-reader-entitlement.md)
  Include an entitlement to indicate your extension is a MediaExtension format reader.
### Track readers
- [protocol METrackReader](metrackreader.md)
  A protocol that defines the information to provide about a track within a media asset.
- [class METrackInfo](metrackinfo.md)
  An object that includes track properties parsed from the media asset.
### Sample cursors
- [protocol MESampleCursor](mesamplecursor.md)
  A protocol that defines the information to provide about samples within a track of a media asset, and enables stepping through samples in the track in decode or presentation order.
- [class MESampleLocation](mesamplelocation.md)
  An object that provides information about the sample location with the media.
- [class MESampleCursorChunk](mesamplecursorchunk.md)
  An object that provides information about the chunk of media at the location of a sample.
- [class MEEstimatedSampleLocation](meestimatedsamplelocation.md)
  An object that provides information about the estimated sample location with the media.
- [class MEHEVCDependencyInfo](mehevcdependencyinfo.md)
  An object that provides information about the HEVC dependency attributes of a sample.
### Byte sources
- [class MEByteSource](mebytesource.md)
  Provides read access to the data in a media asset file.
### Video decoders
- [protocol MEVideoDecoder](mevideodecoder.md)
  A protocol that defines the requirements for a video decoder.
- [protocol MEVideoDecoderExtension](mevideodecoderextension.md)
  A protocol that defines a factory to create new video decoders for a codec type that the extension implements.
- [class MEDecodeFrameOptions](medecodeframeoptions.md)
  An object that guides the video decoder operation on a per-frame basis.
- [class MEVideoDecoderPixelBufferManager](mevideodecoderpixelbuffermanager.md)
  Describes pixel buffer requirements and creates new pixel buffers.
- [Video decoder property list dictionary](video-decoder-property-list-dictionary.md)
  Include a property list dictionary to describe a video decoder.
- [Video decoder entitlement](video-decoder-entitlement.md)
  Include an entitlement to indicate your extension is a MediaExtension video decoder.
### RAW processors
- [protocol MERAWProcessor](merawprocessor.md)
  A protocol that defines the requirements for a RAW processor.
- [protocol MERAWProcessorExtension](merawprocessorextension.md)
  A protocol that defines a factory to create RAW processors for a codec type that the extension implements.
- [class MERAWProcessorPixelBufferManager](merawprocessorpixelbuffermanager.md)
  Describes pixel buffer requirements and creates new pixel buffers.
- [class MERAWProcessingParameter](merawprocessingparameter.md)
  An object for the RAW processor to describe each processing parameter the processor exposes.
- [enum MERAWProcessorNotification](merawprocessornotification.md)
  Notifications that indicate a RAW processor state change.
- [RAW processor property list dictionary](raw-processor-property-list-dictionary.md)
  Include a property list dictionary to describe a RAW processor.
- [RAW processor entitlement](raw-processor-entitlement.md)
  Include an entitlement to indicate your extension is a MediaExtension RAW processor.
### Errors
- [let MediaExtensionErrorDomain: String](mediaextensionerrordomain.md)
  The domain of the error.
- [struct MEError](meerror-swift.struct.md)
  A MediaExtension framework error.
- [MEError.Code](meerror-swift.struct/code.md)
  An enumeration that models media extension error codes.
### Variables
- [var kMERAWProcessorClassImplementationIDKey: String](kmerawprocessorclassimplementationidkey.md)
- [var kMERAWProcessorCodecNameKey: String](kmerawprocessorcodecnamekey.md)
- [var kMERAWProcessorCodecTypeKey: String](kmerawprocessorcodectypekey.md)
- [var kMERAWProcessorObjectNameKey: String](kmerawprocessorobjectnamekey.md)
- [var kMERAWProcessorProcessorInfoKey: String](kmerawprocessorprocessorinfokey.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/MediaExtension)*