# ICScannerFunctionalUnitDocumentFeeder

**Framework**: ImageCaptureCore  
**Kind**: class  
**Role**: Class

An object that represents the document feeder unit on a scanner.

**Availability**:
- macOS 10.4+

## Declaration

```swift
class ICScannerFunctionalUnitDocumentFeeder
```

```objc
@interface ICScannerFunctionalUnitDocumentFeeder : ICScannerFunctionalUnit
```

## Topics

### Instance Properties
- [var documentLoaded: Bool](./icscannerfunctionalunitdocumentfeeder/documentloaded.md)
- [var documentSize: NSSize](./icscannerfunctionalunitdocumentfeeder/documentsize.md)
- [var documentType: ICScannerDocumentType](./icscannerfunctionalunitdocumentfeeder/documenttype.md)
- [var duplexScanningEnabled: Bool](./icscannerfunctionalunitdocumentfeeder/duplexscanningenabled.md)
- [var evenPageOrientation: ICEXIFOrientationType](./icscannerfunctionalunitdocumentfeeder/evenpageorientation.md)
- [var oddPageOrientation: ICEXIFOrientationType](./icscannerfunctionalunitdocumentfeeder/oddpageorientation.md)
- [var reverseFeederPageOrder: Bool](./icscannerfunctionalunitdocumentfeeder/reversefeederpageorder.md)
- [var supportedDocumentTypes: IndexSet](./icscannerfunctionalunitdocumentfeeder/supporteddocumenttypes.md)
- [var supportsDuplexScanning: Bool](./icscannerfunctionalunitdocumentfeeder/supportsduplexscanning.md)

## Relationships

### Inherits From
- [ICScannerFunctionalUnit](./icscannerfunctionalunit.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Functional Units
- [class ICScannerFunctionalUnit](./icscannerfunctionalunit.md)
  An abstract class that represents a scanner functional unit.
- [class ICScannerFunctionalUnitFlatbed](./icscannerfunctionalunitflatbed.md)
  An object that represents the flatbed unit on a scanner.
- [class ICScannerFunctionalUnitNegativeTransparency](./icscannerfunctionalunitnegativetransparency.md)
  An object that represents the transparency unit for scanning negatives on the scanner.
- [class ICScannerFunctionalUnitPositiveTransparency](./icscannerfunctionalunitpositivetransparency.md)
  An object that represents the transparency unit for scanning positives on the scanner.
- [enum ICScannerTransferMode](./icscannertransfermode.md)
  The modes for transferring scan data from the scanner functional unit.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imagecapturecore/icscannerfunctionalunitdocumentfeeder)*