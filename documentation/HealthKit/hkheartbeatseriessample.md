# HKHeartbeatSeriesSample

**Framework**: HealthKit  
**Kind**: class  
**Role**: Class

A sample that represents a series of heartbeats.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
class HKHeartbeatSeriesSample
```

```objc
@interface HKHeartbeatSeriesSample : HKSeriesSample
```

## Overview

Use a [`HKHeartbeatSeriesQuery`](./hkheartbeatseriesquery.md) to access the underlying heartbeat data.

The [`HKHeartbeatSeriesSample`](./hkheartbeatseriessample.md) class is a subclass of the [`HKSeriesSample`](./hkseriessample.md) class. These samples are immutable; you set the sample’s properties when you build them, and they can’t change.

### Extend Heartbeat Samples

Like many HealthKit classes, you shouldn’t subclass the [`HKHeartbeatSeriesSample`](./hkheartbeatseriessample.md) class. You may extend this class by adding metadata with custom keys to save related data used by your app.

For more information, see [`addMetadata(_:completion:)`](./hkheartbeatseriesbuilder/addmetadata%28_,completion%29.md).

## Topics

### Metadata
- [let HKMetadataKeyAlgorithmVersion: String](./hkmetadatakeyalgorithmversion.md)
  A key that indicates the version number of the algorithm used to calculate the sample’s value.

## Relationships

### Inherits From
- [HKSeriesSample](./hkseriessample.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Series data
- [class HKQuantitySeriesSampleBuilder](./hkquantityseriessamplebuilder.md)
  A builder object for incrementally building a sample that contains multiple quantities.
- [class HKHeartbeatSeriesBuilder](./hkheartbeatseriesbuilder.md)
  A builder object for incrementally building a heartbeat series.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkheartbeatseriessample)*