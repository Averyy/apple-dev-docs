# SRFetchResult

**Framework**: SensorKit  
**Kind**: class

Recorded data that a sensor reader fetches.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
class SRFetchResult<SampleType> where SampleType : AnyObject
```

#### Overview

A sensor reader’s [`delegate`](srsensorreader/delegate.md) receives instances of this class from the [`sensorReader(_:didCompleteFetch:)`](srsensorreaderdelegate/sensorreader(_:didcompletefetch:).md) when a fetch request finishes successfully.

Results are in the form of samples, which are of varying types depending on the reader’s sensor. For a list of sample types per sensor, see [`Sample types`](srfetchresult/sample#Sample-types.md).

## Topics

### Sampling Data
- [var sample: SampleType](srfetchresult/sample.md)
  A recording that the sensor reader fetches.
- [var timestamp: SRAbsoluteTime](srfetchresult/timestamp.md)
  The time when the framework records the sample.
### Instance Properties
- [var sourceDevice: SRSourceDevice?](srfetchresult/sourcedevice.md)

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCopying](../foundation/nscopying.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## See Also

- [class SRFetchRequest](srfetchrequest.md)
  An object that defines the criteria for a sample query.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/srfetchresult)*