# HKSourceQuery

**Framework**: HealthKit  
**Kind**: class  
**Role**: Class

A query that returns a list of sources, such as apps and devices, that have saved matching queries to the HealthKit store.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- visionOS
- watchOS

## Declaration

```swift
class HKSourceQuery
```

```objc
@interface HKSourceQuery : HKQuery
```

#### Overview

Source queries return a list of sources that have saved samples matching the specified sample types. Sources can be apps or devices (like Apple Watch or Bluetooth heart-rate monitors).

Source queries are immutable: Their properties are set when they are first created, and they can’t change.

## Topics

### Creating Source Queries
- [Executing Source Queries](./executing-source-queries.md)
  Create and run source queries.
- [init(sampleType: HKSampleType, samplePredicate: NSPredicate?, completionHandler: (HKSourceQuery, Set<HKSource>?, (any Error)?) -> Void)](./hksourcequery/init%28sampletype,samplepredicate,completionhandler%29.md)
  Instantiates and returns a source query.

## Relationships

### Inherits From
- [HKQuery](./hkquery.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Sources and devices
- [struct HKSourceQueryDescriptor](./hksourcequerydescriptor.md)
  A query interface that uses Swift concurrency to read the apps and devices that produced the matching samples.
- [class HKSourceRevision](./hksourcerevision.md)
  An object indicating the source of a HealthKit sample.
- [class HKSource](./hksource.md)
  An object indicating the app or device that created a HealthKit sample
- [class HKDevice](./hkdevice.md)
  A device that generates data for HealthKit.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hksourcequery)*