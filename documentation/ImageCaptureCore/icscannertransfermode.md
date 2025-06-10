# ICScannerTransferMode

**Framework**: ImageCaptureCore  
**Kind**: enum

The modes for transferring scan data from the scanner functional unit.

**Availability**:
- macOS 10.7+

## Declaration

```swift
enum ICScannerTransferMode
```

## Topics

### Constants
- [ICScannerTransferMode.fileBased](icscannertransfermode/filebased.md)
  The mode for transferring the scan as a file.
- [ICScannerTransferMode.memoryBased](icscannertransfermode/memorybased.md)
  The mode for transferring the scan as data.
### Initializers
- [init?(rawValue: UInt)](icscannertransfermode/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/imagecapturecore/icscannertransfermode)*