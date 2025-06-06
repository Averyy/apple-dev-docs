# ICScannerFeature

**Framework**: ImageCaptureCore  
**Kind**: class

An abstract class that describes a scanner feature.

**Availability**:
- macOS 10.4+

## Declaration

```swift
class ICScannerFeature
```

#### Overview

The ImageCaptureCore framework defines three concrete subclasses of scanner features: [`ICScannerFeatureEnumeration`](icscannerfeatureenumeration.md), [`ICScannerFeatureRange`](icscannerfeaturerange.md), and [`ICScannerFeatureBoolean`](icscannerfeatureboolean.md). Scanner functional units may have one or more instances of these classes to allow users to choose scanner-specific settings or operations before performing a scan.

## Topics

### Instance Properties
- [var humanReadableName: String?](icscannerfeature/humanreadablename.md)
- [var internalName: String?](icscannerfeature/internalname.md)
- [var tooltip: String?](icscannerfeature/tooltip.md)
- [var type: ICScannerFeatureType](icscannerfeature/type.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [ICScannerFeatureBoolean](icscannerfeatureboolean.md)
- [ICScannerFeatureEnumeration](icscannerfeatureenumeration.md)
- [ICScannerFeatureRange](icscannerfeaturerange.md)
- [ICScannerFeatureTemplate](icscannerfeaturetemplate.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/imagecapturecore/icscannerfeature)*