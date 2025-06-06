# ICScannerFunctionalUnit

**Framework**: ImageCaptureCore  
**Kind**: class

An abstract class that represents a scanner functional unit.

**Availability**:
- macOS 10.4+

## Declaration

```swift
class ICScannerFunctionalUnit
```

#### Overview

The ImageCaptureCore framework defines four concrete subclasses of functional units:

- [`ICScannerFunctionalUnitDocumentFeeder`](icscannerfunctionalunitdocumentfeeder.md)
- [`ICScannerFunctionalUnitFlatbed`](icscannerfunctionalunitflatbed.md)
- [`ICScannerFunctionalUnitPositiveTransparency`](icscannerfunctionalunitpositivetransparency.md)
- [`ICScannerFunctionalUnitNegativeTransparency`](icscannerfunctionalunitnegativetransparency.md)

[`ICScannerDevice`](icscannerdevice.md) creates instances of these subclasses.

## Topics

### Instance Properties
- [var acceptsThresholdForBlackAndWhiteScanning: Bool](icscannerfunctionalunit/acceptsthresholdforblackandwhitescanning.md)
- [var bitDepth: ICScannerBitDepth](icscannerfunctionalunit/bitdepth.md)
- [var canPerformOverviewScan: Bool](icscannerfunctionalunit/canperformoverviewscan.md)
- [var defaultThresholdForBlackAndWhiteScanning: UInt8](icscannerfunctionalunit/defaultthresholdforblackandwhitescanning.md)
- [var measurementUnit: ICScannerMeasurementUnit](icscannerfunctionalunit/measurementunit.md)
- [var nativeXResolution: Int](icscannerfunctionalunit/nativexresolution.md)
- [var nativeYResolution: Int](icscannerfunctionalunit/nativeyresolution.md)
- [var overviewImage: CGImage?](icscannerfunctionalunit/overviewimage.md)
- [var overviewResolution: Int](icscannerfunctionalunit/overviewresolution.md)
- [var overviewScanInProgress: Bool](icscannerfunctionalunit/overviewscaninprogress.md)
- [var physicalSize: NSSize](icscannerfunctionalunit/physicalsize.md)
- [var pixelDataType: ICScannerPixelDataType](icscannerfunctionalunit/pixeldatatype.md)
- [var preferredResolutions: IndexSet](icscannerfunctionalunit/preferredresolutions.md)
- [var preferredScaleFactors: IndexSet](icscannerfunctionalunit/preferredscalefactors.md)
- [var resolution: Int](icscannerfunctionalunit/resolution.md)
- [var scaleFactor: Int](icscannerfunctionalunit/scalefactor.md)
- [var scanArea: NSRect](icscannerfunctionalunit/scanarea.md)
- [var scanAreaOrientation: ICEXIFOrientationType](icscannerfunctionalunit/scanareaorientation.md)
- [var scanInProgress: Bool](icscannerfunctionalunit/scaninprogress.md)
- [var scanProgressPercentDone: CGFloat](icscannerfunctionalunit/scanprogresspercentdone.md)
- [var state: ICScannerFunctionalUnitState](icscannerfunctionalunit/state.md)
- [var supportedBitDepths: IndexSet](icscannerfunctionalunit/supportedbitdepths.md)
- [var supportedMeasurementUnits: IndexSet](icscannerfunctionalunit/supportedmeasurementunits.md)
- [var supportedResolutions: IndexSet](icscannerfunctionalunit/supportedresolutions.md)
- [var supportedScaleFactors: IndexSet](icscannerfunctionalunit/supportedscalefactors.md)
- [var templates: [ICScannerFeatureTemplate]](icscannerfunctionalunit/templates.md)
- [var thresholdForBlackAndWhiteScanning: UInt8](icscannerfunctionalunit/thresholdforblackandwhitescanning.md)
- [var type: ICScannerFunctionalUnitType](icscannerfunctionalunit/type.md)
- [var usesThresholdForBlackAndWhiteScanning: Bool](icscannerfunctionalunit/usesthresholdforblackandwhitescanning.md)
- [var vendorFeatures: [ICScannerFeature]?](icscannerfunctionalunit/vendorfeatures.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [ICScannerFunctionalUnitDocumentFeeder](icscannerfunctionalunitdocumentfeeder.md)
- [ICScannerFunctionalUnitFlatbed](icscannerfunctionalunitflatbed.md)
- [ICScannerFunctionalUnitNegativeTransparency](icscannerfunctionalunitnegativetransparency.md)
- [ICScannerFunctionalUnitPositiveTransparency](icscannerfunctionalunitpositivetransparency.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class ICScannerFunctionalUnitDocumentFeeder](icscannerfunctionalunitdocumentfeeder.md)
  An object that represents the document feeder unit on a scanner.
- [class ICScannerFunctionalUnitFlatbed](icscannerfunctionalunitflatbed.md)
  An object that represents the flatbed unit on a scanner.
- [class ICScannerFunctionalUnitNegativeTransparency](icscannerfunctionalunitnegativetransparency.md)
  An object that represents the transparency unit for scanning negatives on the scanner.
- [class ICScannerFunctionalUnitPositiveTransparency](icscannerfunctionalunitpositivetransparency.md)
  An object that represents the transparency unit for scanning positives on the scanner.
- [enum ICScannerTransferMode](icscannertransfermode.md)
  The modes for transferring scan data from the scanner functional unit.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imagecapturecore/icscannerfunctionalunit)*