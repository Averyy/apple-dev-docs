# HKAudiogramSample

**Framework**: HealthKit  
**Kind**: class  
**Role**: Class

A sample that stores an audiogram.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
class HKAudiogramSample
```

```objc
@interface HKAudiogramSample : HKSample
```

## Overview

This sample stores the results from a hearing test. The sample stores the audiogram data as an array of sensitivity points.

## Topics

### Creating Audiogram Samples
- [convenience init(sensitivityPoints: [HKAudiogramSensitivityPoint], start: Date, end: Date, metadata: [String : Any]?)](./hkaudiogramsample/init%28sensitivitypoints,start,end,metadata%29.md)
  Creates a new audiogram sample.
### Accessing Sensitivity Point Data
- [var sensitivityPoints: [HKAudiogramSensitivityPoint]](./hkaudiogramsample/sensitivitypoints.md)
  An array of sensitivity point objects.
### Initializers
- [convenience init(sensitivityPoints: [HKAudiogramSensitivityPoint], start: Date, end: Date, device: HKDevice?, metadata: [String : Any]?)](./hkaudiogramsample/init%28sensitivitypoints,start,end,device,metadata%29.md)
- [convenience init(sensitivityPoints: [HKAudiogramSensitivityPoint], startDate: Date, endDate: Date, device: HKDevice?, metadata: [String : Any]?)](./hkaudiogramsample/init%28sensitivitypoints,startdate,enddate,device,metadata%29.md)
- [convenience init(sensitivityPoints: [HKAudiogramSensitivityPoint], startDate: Date, endDate: Date, metadata: [String : Any]?)](./hkaudiogramsample/init%28sensitivitypoints,startdate,enddate,metadata%29.md)

## Relationships

### Inherits From
- [HKSample](./hksample.md)
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

### Audiograms
- [class HKAudiogramSensitivityPoint](./hkaudiogramsensitivitypoint.md)
  A hearing sensitivity reading associated with a hearing test.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkaudiogramsample)*