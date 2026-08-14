# ReportableMetadataValue

**Framework**: StateReporting  
**Kind**: enum

A value in a reportable-metadata dictionary.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
enum ReportableMetadataValue
```

#### Overview

Strings, numbers, and dates all initialize directly. The [`ReportableMetadata()`](reportablemetadata().md) macro constructs these automatically when you annotate your metadata type.

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
- [ReportableMetadataValue.date(_:)](reportablemetadatavalue/date(_:).md)
- [ReportableMetadataValue.floatingPoint(_:)](reportablemetadatavalue/floatingpoint(_:).md)
- [ReportableMetadataValue.integer(_:)](reportablemetadatavalue/integer(_:).md)
- [ReportableMetadataValue.string(_:)](reportablemetadatavalue/string(_:).md)
### Initializers
- [init(Int32)](reportablemetadatavalue/init(_:)-14guo.md)
- [init(UInt32)](reportablemetadatavalue/init(_:)-1ahz9.md)
- [init(UInt16)](reportablemetadatavalue/init(_:)-2f79p.md)
- [init(CGFloat)](reportablemetadatavalue/init(_:)-2h2re.md)
- [init(Date)](reportablemetadatavalue/init(_:)-2llwr.md)
- [init(Int64)](reportablemetadatavalue/init(_:)-5y574.md)
- [init(Bool)](reportablemetadatavalue/init(_:)-5yq8x.md)
- [init(UInt8)](reportablemetadatavalue/init(_:)-6kkn5.md)
- [init(Double)](reportablemetadatavalue/init(_:)-6r11y.md)
- [init(UInt)](reportablemetadatavalue/init(_:)-6z809.md)
- [init(Float)](reportablemetadatavalue/init(_:)-85rvl.md)
- [init(UInt64)](reportablemetadatavalue/init(_:)-90tzm.md)
- [init(Int16)](reportablemetadatavalue/init(_:)-9dt4i.md)
- [init(Int8)](reportablemetadatavalue/init(_:)-pijp.md)
- [init(Int)](reportablemetadatavalue/init(_:)-tnel.md)
- [init(String)](reportablemetadatavalue/init(_:)-zkel.md)

## Relationships

### Conforms To
- [Decodable](../swift/decodable.md)
- [Encodable](../swift/encodable.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [protocol ReportableMetadata](reportablemetadata.md)
  A protocol for types that can supply their metadata as a dictionary of reportable values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/statereporting/reportablemetadatavalue)*