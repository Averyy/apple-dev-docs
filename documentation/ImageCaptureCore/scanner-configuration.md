# Scanner Configuration

**Framework**: ImageCaptureCore

Examine a scanner’s functional units and features.

## Topics

### Band Data
- [class ICScannerBandData](icscannerbanddata.md)
  The options for each band of data that the scanner reads.
### Bit Depth
- [enum ICScannerBitDepth](icscannerbitdepth.md)
  The number of bits per channel in the scanned image.
### Color Formats
- [enum ICScannerColorDataFormatType](icscannercolordataformattype.md)
  The color data formats relevant to multichannel data.
### Document Sizes
- [enum ICScannerDocumentType](icscannerdocumenttype.md)
  The supported document size types.
- [enum ICScannerMeasurementUnit](icscannermeasurementunit.md)
  The unit of measurement used by the scanner.
### Features
- [class ICScannerFeature](icscannerfeature.md)
  An abstract class that describes a scanner feature.
- [class ICScannerFeatureBoolean](icscannerfeatureboolean.md)
  A feature with a value of `YES` or `NO`.
- [class ICScannerFeatureEnumeration](icscannerfeatureenumeration.md)
  A feature that can have one of several discrete values, strings or numbers.
- [class ICScannerFeatureRange](icscannerfeaturerange.md)
  A feature with a value that lies within a range.
- [class ICScannerFeatureTemplate](icscannerfeaturetemplate.md)
  A group of one or more rectangular scan areas that can be used with a scanner functional unit.
- [enum ICScannerFeatureType](icscannerfeaturetype.md)
  The types of scanner features.
### Functional Units
- [class ICScannerFunctionalUnit](icscannerfunctionalunit.md)
  An abstract class that represents a scanner functional unit.
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
### Pixel Data Types
- [enum ICScannerPixelDataType](icscannerpixeldatatype.md)
  The pixel data types.
### Scanner States
- [let ICScannerStatusRequestsOverviewScan: String](icscannerstatusrequestsoverviewscan.md)
  A nonlocalized notification string to indicate that the scanner is requesting an overview scan.
- [let ICScannerStatusWarmingUp: String](icscannerstatuswarmingup.md)
  A nonlocalized notification string to indicate that the scanner is warming up.
- [let ICScannerStatusWarmUpDone: String](icscannerstatuswarmupdone.md)
  A nonlocalized notification string to indicate that the scanner has warmed up.
### Buttons
- [let ICButtonTypeCopy: String](icbuttontypecopy.md)
  A nonlocalized notification string to indicate that the Copy button on the device was pressed.
- [let ICButtonTypeMail: String](icbuttontypemail.md)
  A nonlocalized notification string to indicate that the Mail button on the device was pressed.
- [let ICButtonTypePrint: String](icbuttontypeprint.md)
  A nonlocalized notification string to indicate that the Print button on the device was pressed.
- [let ICButtonTypeScan: String](icbuttontypescan.md)
  A nonlocalized notification string to indicate that the Scan button on the device was pressed.
- [let ICButtonTypeTransfer: String](icbuttontypetransfer.md)
  A nonlocalized notification string to indicate that the Transfer button on the device was pressed.
- [let ICButtonTypeWeb: String](icbuttontypeweb.md)
  A nonlocalized notification string to indicate that the Web button on the device was pressed.

## See Also

- [class ICScannerDevice](icscannerdevice.md)
  An object that represents a scanner.
- [protocol ICScannerDeviceDelegate](icscannerdevicedelegate.md)
  Methods for determining availability, selecting a functional unit, and performing scans on connected scanners.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imagecapturecore/scanner-configuration)*