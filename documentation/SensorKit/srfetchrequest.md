# SRFetchRequest

**Framework**: SensorKit  
**Kind**: class  
**Role**: Class

An object that defines the criteria for a sample query.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
class SRFetchRequest
```

```objc
@interface SRFetchRequest : NSObject
```

#### Overview

An app configures an instance of this class to select the device from which to query sensor data. The time range ([`from`](./srfetchrequest/from.md), [`to`](./srfetchrequest/to.md)) specifies when the framework records the data. A fetch query can retrieve only sensor data that the app records by first calling [`startRecording()`](./srsensorreader/startrecording%28%29.md).

To execute a fetch request, an app passes the instance of this class to its sensor reader’s [`fetch(_:)`](./srsensorreader/fetch%28_%29.md) function.

The framework notifies the sensor reader’s [`delegate`](./srsensorreader/delegate.md) upon fetch-request completion with [`sensorReader(_:didCompleteFetch:)`](./srsensorreaderdelegate/sensorreader%28_,didcompletefetch%29.md). If the fetch fails, the framework calls the delegate’s [`sensorReader(_:fetching:failedWithError:)`](./srsensorreaderdelegate/sensorreader%28_,fetching,failedwitherror%29.md).

SensorKit places a 24-hour holding period on newly recorded data before an app can access it. This gives the user an opportunity to delete any data they don’t want to share with the app. A fetch request doesn’t return any results if its time range overlaps this holding period.

## Topics

### Selecting the Device
- [var device: SRDevice](./srfetchrequest/device.md)
  The device to query for sample data.
- [class SRDevice](./srdevice.md)
  A representation of a device that provides sample data.
### Defining the Time Range
- [var from: SRAbsoluteTime](./srfetchrequest/from.md)
  Fetches sample information that occurs after this time.
- [var to: SRAbsoluteTime](./srfetchrequest/to.md)
  Fetches sample information that occurs before this time.
- [struct SRAbsoluteTime](./srabsolutetime.md)
  A value that describes when the system records the data.
- [static func current() -> SRAbsoluteTime](./srabsolutetime/current%28%29.md)
  Provides the current absolute time.
- [func toCFAbsoluteTime() -> CFAbsoluteTime](./srabsolutetime/tocfabsolutetime%28%29.md)
  Converts an absolute time to a core-foundation absolute time.
- [SRAbsoluteTimeFromCFAbsoluteTime](./srabsolutetimefromcfabsolutetime.md)
  Provides an absolute time equivalent to the argument core-foundation absolute time.
- [SRAbsoluteTimeFromContinuousTime](./srabsolutetimefromcontinuoustime.md)
  Provides an absolute time equivalent to the argument continuous time.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Querying data
- [class SRFetchResult](./srfetchresult.md)
  Recorded data that a sensor reader fetches.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/srfetchrequest)*