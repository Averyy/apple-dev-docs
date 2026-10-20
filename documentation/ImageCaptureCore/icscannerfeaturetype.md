# ICScannerFeatureType

**Framework**: ImageCaptureCore  
**Kind**: enum  
**Role**: Enumeration

The types of scanner features.

**Availability**:
- macOS 10.4+

## Declaration

```swift
enum ICScannerFeatureType
```

```c
enum ICScannerFeatureType : NSUInteger;
```

## Topics

### Constants
- [ICScannerFeatureType.boolean](./icscannerfeaturetype/boolean.md)
  A feature with a value of YES or NO.
- [ICScannerFeatureType.enumeration](./icscannerfeaturetype/enumeration.md)
  A feature that can have one of several discrete values, strings, or numbers.
- [ICScannerFeatureType.range](./icscannerfeaturetype/range.md)
  A feature with a value that lies within a range.
- [ICScannerFeatureType.template](./icscannerfeaturetype/template.md)
  A group of one or more rectangular scan areas that can be used with a scanner functional unit.
### Initializers
- [init?(rawValue: UInt)](./icscannerfeaturetype/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Features
- [class ICScannerFeature](./icscannerfeature.md)
  An abstract class that describes a scanner feature.
- [class ICScannerFeatureBoolean](./icscannerfeatureboolean.md)
  A feature with a value of `YES` or `NO`.
- [class ICScannerFeatureEnumeration](./icscannerfeatureenumeration.md)
  A feature that can have one of several discrete values, strings or numbers.
- [class ICScannerFeatureRange](./icscannerfeaturerange.md)
  A feature with a value that lies within a range.
- [class ICScannerFeatureTemplate](./icscannerfeaturetemplate.md)
  A group of one or more rectangular scan areas that can be used with a scanner functional unit.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imagecapturecore/icscannerfeaturetype)*