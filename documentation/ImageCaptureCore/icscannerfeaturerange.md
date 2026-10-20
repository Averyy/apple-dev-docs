# ICScannerFeatureRange

**Framework**: ImageCaptureCore  
**Kind**: class  
**Role**: Class

A feature with a value that lies within a range.

**Availability**:
- macOS 10.4+

## Declaration

```swift
class ICScannerFeatureRange
```

```objc
@interface ICScannerFeatureRange : ICScannerFeature
```

## Topics

### Instance Properties
- [var currentValue: CGFloat](./icscannerfeaturerange/currentvalue.md)
- [var defaultValue: CGFloat](./icscannerfeaturerange/defaultvalue.md)
- [var maxValue: CGFloat](./icscannerfeaturerange/maxvalue.md)
- [var minValue: CGFloat](./icscannerfeaturerange/minvalue.md)
- [var stepSize: CGFloat](./icscannerfeaturerange/stepsize.md)

## Relationships

### Inherits From
- [ICScannerFeature](./icscannerfeature.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Features
- [class ICScannerFeature](./icscannerfeature.md)
  An abstract class that describes a scanner feature.
- [class ICScannerFeatureBoolean](./icscannerfeatureboolean.md)
  A feature with a value of `YES` or `NO`.
- [class ICScannerFeatureEnumeration](./icscannerfeatureenumeration.md)
  A feature that can have one of several discrete values, strings or numbers.
- [class ICScannerFeatureTemplate](./icscannerfeaturetemplate.md)
  A group of one or more rectangular scan areas that can be used with a scanner functional unit.
- [enum ICScannerFeatureType](./icscannerfeaturetype.md)
  The types of scanner features.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imagecapturecore/icscannerfeaturerange)*