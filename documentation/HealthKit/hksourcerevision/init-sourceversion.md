# init(source:version:)

**Framework**: HealthKit  
**Kind**: init

Initializes a new source revision object with the provided source and version information.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
init(source: HKSource, version: String?)
```

#### Return Value

A newly initialized source revision object.

#### Discussion

Use this method to create source revisions for use in queries. For more information, see [`HKPredicateKeyPathSourceRevision`](hkpredicatekeypathsourcerevision.md).

On iOS 9.0 or later, the system automatically creates a source revision for any samples saved to the HealthKit store. For earlier versions of iOS, the system only saves [`HKSource`](hksource.md) information. However, when these samples are retrieved on iOS 9.0 or later, the system creates a new source revision object for the sample. HealthKit uses the previously stored source information with a `nil`-valued version string.

## Parameters

- `source`: The source for a sample.
- `version`: A string that uniquely identifies the source’s version.

## See Also

- [let HKSourceRevisionAnyVersion: String](hksourcerevisionanyversion.md)
  A constant that matches any version.
- [init(source: HKSource, version: String?, productType: String?, operatingSystemVersion: OperatingSystemVersion)](hksourcerevision/init(source:version:producttype:operatingsystemversion:).md)
  Initializes a new source revision object with the provided source, version, product type, and operating system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hksourcerevision/init(source:version:))*