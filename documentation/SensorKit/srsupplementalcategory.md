# SRSupplementalCategory

**Framework**: SensorKit  
**Kind**: class  
**Role**: Class

A more detailed category that provides additional context to the app category.

**Availability**:
- iOS 16.4+
- iPadOS 16.4+
- Mac Catalyst 16.4+

## Declaration

```swift
class SRSupplementalCategory
```

```objc
@interface SRSupplementalCategory : NSObject
```

#### Overview

Use a supplemental category to interpret the detailed relationships of app usage data within a [`SRDeviceUsageReport`](./srdeviceusagereport.md). The device usage report contains high level primary categories defined by the [`SRDeviceUsageReport.CategoryKey`](./srdeviceusagereport/categorykey.md), which are then broken down into more specific descriptions with the supplemental category. Each category maps to a unique [`identifier`](./srsupplementalcategory/identifier.md), which you can access with the [`supplementalCategories`](./srdeviceusagereport/applicationusage/supplementalcategories.md) property and group the app usage relationships.

Use this [table](https://developer.apple.com/download/files/SRSupplementalCategoryTable.zip) to access this supplemental category. It’s organized with the identifier that maps to a set of related words called *representative words*. For example, if you’re tracking usage within apps in the Games category, use the cluster UUID with representative words like *puzzle*, *gameplay*, *addictive*, and so on to track the specific types of apps and common descriptions within Games.

> **Note**: These representative words are subject to change in future releases, that’s why each table is associated with a version number that helps you keep track of the categories you use.

## Topics

### Identifying the category
- [var identifier: String](./srsupplementalcategory/identifier.md)
  A unique identifier for the supplemental category.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Identifying the App
- [var bundleIdentifier: String?](./srdeviceusagereport/applicationusage/bundleidentifier.md)
  The bundle identifier of the app in use.
- [var reportApplicationIdentifier: String](./srdeviceusagereport/applicationusage/reportapplicationidentifier.md)
  A pseudonymn for a real application identifier.
- [var supplementalCategories: [SRSupplementalCategory]](./srdeviceusagereport/applicationusage/supplementalcategories.md)
  Categories that provide more information about an app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/srsupplementalcategory)*