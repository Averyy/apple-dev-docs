# init(source:version:productType:operatingSystemVersion:)

**Framework**: HealthKit  
**Kind**: init

Initializes a new source revision object with the provided source, version, product type, and operating system.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
init(source: HKSource, version: String?, productType: String?, operatingSystemVersion: OperatingSystemVersion)
```

#### Return Value

A newly initialized source revision object.

#### Discussion

Use this method to create source revisions for use in queries. For more information, see [`HKPredicateKeyPathSourceRevision`](hkpredicatekeypathsourcerevision.md).

## Parameters

- `source`: The source for a sample.
- `version`: A string that uniquely identifies the source’s version.
- `productType`: A string that identifies the device used to save the sample.
- `operatingSystemVersion`: A string that identifies the operating system used to save the sample.

## See Also

- [let HKSourceRevisionAnyVersion: String](hksourcerevisionanyversion.md)
  A constant that matches any version.
- [let HKSourceRevisionAnyProductType: String](hksourcerevisionanyproducttype.md)
  A constant that matches any product type.
- [let HKSourceRevisionAnyOperatingSystem: OperatingSystemVersion](hksourcerevisionanyoperatingsystem.md)
  A constant that matches any operating system.
- [init(source: HKSource, version: String?)](hksourcerevision/init(source:version:).md)
  Initializes a new source revision object with the provided source and version information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hksourcerevision/init(source:version:producttype:operatingsystemversion:))*