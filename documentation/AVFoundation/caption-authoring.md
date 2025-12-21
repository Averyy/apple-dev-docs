# Caption authoring

**Framework**: AVFoundation

Create captions and subtitles in industry-standard formats.

## Topics

### Captions
- [class AVCaption](avcaption.md)
  An object that represents text to present over a time range.
- [class AVMutableCaption](avmutablecaption.md)
  A mutable caption subclass that you use to create new captions.
### Regions
- [class AVCaptionRegion](avcaptionregion.md)
  An object that represents the region in which the system presents a caption.
- [class AVMutableCaptionRegion](avmutablecaptionregion.md)
  A mutable caption region subclass that you use to create new caption regions.
### Groups
- [class AVCaptionGroup](avcaptiongroup.md)
  An object that represents zero or more captions that intersect in time.
- [class AVCaptionGrouper](avcaptiongrouper.md)
  An object that analyzes the temporal overlaps of caption objects to create caption groups for each span of concurrent captions.
### Presentation
- [class AVCaptionRenderer](avcaptionrenderer.md)
  An object that renders captions for display at a particular time.
### Reading and writing
- [class AVAssetReaderOutputCaptionAdaptor](avassetreaderoutputcaptionadaptor.md)
  An object that reads caption group objects from an asset track that contains timed text.
- [class AVAssetWriterInputCaptionAdaptor](avassetwriterinputcaptionadaptor.md)
  An object that appends captions to an asset writer input.
### Conversion and validation
- [struct AVCaptionSettingsKey](avcaptionsettingskey.md)
  A structure that defines dictionary keys to configure the caption converter and validator.
- [class AVCaptionFormatConformer](avcaptionformatconformer.md)
  An object that converts a canonical caption to a specific format.
- [class AVCaptionConversionValidator](avcaptionconversionvalidator.md)
  An object that validates captions for a conversion operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/caption-authoring)*