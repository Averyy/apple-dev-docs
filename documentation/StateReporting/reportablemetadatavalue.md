# ReportableMetadataValue

**Framework**: StateReporting  
**Kind**: enum  
**Role**: Enumeration

A value in a reportable-metadata dictionary.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
enum ReportableMetadataValue
```

#### Overview

Strings, numbers, and dates all initialize directly. The [`ReportableMetadata()`](./reportablemetadata%28%29.md) macro constructs these automatically when you annotate your metadata type.

```swift
let values: [String: ReportableMetadataValue] = [
    "username": ReportableMetadataValue("alice"),
    "loginCount": ReportableMetadataValue(42),
    "lastLogin": ReportableMetadataValue(Date()),
    "score": ReportableMetadataValue(98.6)
]
```

## Topics

### Enumeration Cases
- [ReportableMetadataValue.date(_:)](./reportablemetadatavalue/date%28_%29.md)
- [ReportableMetadataValue.floatingPoint(_:)](./reportablemetadatavalue/floatingpoint%28_%29.md)
- [ReportableMetadataValue.integer(_:)](./reportablemetadatavalue/integer%28_%29.md)
- [ReportableMetadataValue.string(_:)](./reportablemetadatavalue/string%28_%29.md)
### Initializers
- [init(Int32)](./reportablemetadatavalue/init%28_%29-14guo.md)
- [init(UInt32)](./reportablemetadatavalue/init%28_%29-1ahz9.md)
- [init(UInt16)](./reportablemetadatavalue/init%28_%29-2f79p.md)
- [init(CGFloat)](./reportablemetadatavalue/init%28_%29-2h2re.md)
- [init(Date)](./reportablemetadatavalue/init%28_%29-2llwr.md)
- [init(Int64)](./reportablemetadatavalue/init%28_%29-5y574.md)
- [init(Bool)](./reportablemetadatavalue/init%28_%29-5yq8x.md)
- [init(UInt8)](./reportablemetadatavalue/init%28_%29-6kkn5.md)
- [init(Double)](./reportablemetadatavalue/init%28_%29-6r11y.md)
- [init(UInt)](./reportablemetadatavalue/init%28_%29-6z809.md)
- [init(Float)](./reportablemetadatavalue/init%28_%29-85rvl.md)
- [init(UInt64)](./reportablemetadatavalue/init%28_%29-90tzm.md)
- [init(Int16)](./reportablemetadatavalue/init%28_%29-9dt4i.md)
- [init(Int8)](./reportablemetadatavalue/init%28_%29-pijp.md)
- [init(Int)](./reportablemetadatavalue/init%28_%29-tnel.md)
- [init(String)](./reportablemetadatavalue/init%28_%29-zkel.md)

## Relationships

### Conforms To
- [Decodable](../Swift/decodable.md)
- [Encodable](../Swift/encodable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Defining metadata
- [protocol ReportableMetadata](./reportablemetadata.md)
  A protocol for types that can supply their metadata as a dictionary of reportable values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/statereporting/reportablemetadatavalue)*