# HKSourceRevision

**Framework**: HealthKit  
**Kind**: class

An object indicating the source of a HealthKit sample.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class HKSourceRevision
```

## Mentions

- [About the HealthKit framework](about-the-healthkit-framework.md)

#### Overview

The [`HKSourceRevision`](hksourcerevision.md) class acts as a wrapper for the [`HKSource`](hksource.md) class, adding information about the source’s version, operating system, and product type.

Source revision objects are immutable: you set the source revision’s properties when you create the object, and they cannot change.

When an [`HKObject`](hkobject.md) instance is created, its [`sourceRevision`](hkobject/sourcerevision.md) property is set to `nil`. When the object is saved to the HealthKit store, HealthKit assigns a new source revision to the object’s [`sourceRevision`](hkobject/sourcerevision.md) property. The source revision can be accessed only on objects retrieved from the HealthKit store.

##### Subclassing Source Revisions

As with many HealthKit classes, don’t subclass the [`HKSourceRevision`](hksourcerevision.md) class.

## Topics

### Creating Source Revision Objects
- [init(source: HKSource, version: String?)](hksourcerevision/init(source:version:).md)
  Initializes a new source revision object with the provided source and version information.
- [init(source: HKSource, version: String?, productType: String?, operatingSystemVersion: OperatingSystemVersion)](hksourcerevision/init(source:version:producttype:operatingsystemversion:).md)
  Initializes a new source revision object with the provided source, version, product type, and operating system.
### Accessing Source and Version Information
- [var source: HKSource](hksourcerevision/source.md)
  The source for a sample.
- [var version: String?](hksourcerevision/version.md)
  A string that identifies a particular version of the source.
- [var operatingSystemVersion: OperatingSystemVersion](hksourcerevision/operatingsystemversion.md)
  A string that identifies the operating system used to save a sample.
- [var productType: String?](hksourcerevision/producttype.md)
  A string that identifies the device used to save a sample.
### Initializers
- [init?(coder: NSCoder)](hksourcerevision/init(coder:).md)

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCoding](../foundation/nscoding.md)
- [NSCopying](../foundation/nscopying.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [NSSecureCoding](../foundation/nssecurecoding.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [struct HKSourceQueryDescriptor](hksourcequerydescriptor.md)
  A query interface that uses Swift concurrency to read the apps and devices that produced the matching samples.
- [class HKSource](hksource.md)
  An object indicating the app or device that created a HealthKit sample
- [class HKDevice](hkdevice.md)
  A device that generates data for HealthKit.
- [class HKSourceQuery](hksourcequery.md)
  A query that returns a list of sources, such as apps and devices, that have saved matching queries to the HealthKit store.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hksourcerevision)*