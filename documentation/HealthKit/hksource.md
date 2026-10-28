# HKSource

**Framework**: HealthKit  
**Kind**: class  
**Role**: Class

An object indicating the app or device that created a HealthKit sample

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class HKSource
```

```objc
@interface HKSource : NSObject
```

## Overview

Sources include apps and devices that save data to the HealthKit store. Currently, HealthKit supports only the direct import of data from Bluetooth LE heart rate monitors. All other devices need a companion app to collect and save the data to HealthKit.

## Topics

### Getting the Current Source
- [class func `default`() -> HKSource](./hksource/default%28%29.md)
  Returns a source object for the current app.
### Getting Property Data
- [var bundleIdentifier: String](./hksource/bundleidentifier.md)
  The source’s bundle identifier.
- [var name: String](./hksource/name.md)
  The source’s name.
### Initializers
- [init?(coder: NSCoder)](./hksource/init%28coder%29.md)

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

### Sources and devices
- [struct HKSourceQueryDescriptor](./hksourcequerydescriptor.md)
  A query interface that uses Swift concurrency to read the apps and devices that produced the matching samples.
- [class HKSourceRevision](./hksourcerevision.md)
  An object indicating the source of a HealthKit sample.
- [class HKDevice](./hkdevice.md)
  A device that generates data for HealthKit.
- [class HKSourceQuery](./hksourcequery.md)
  A query that returns a list of sources, such as apps and devices, that have saved matching queries to the HealthKit store.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hksource)*