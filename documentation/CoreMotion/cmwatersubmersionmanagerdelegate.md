# CMWaterSubmersionManagerDelegate

**Framework**: Core Motion  
**Kind**: protocol

A delegate that receives updates about ambient pressure, water pressure, water temperature, and submersion events.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
protocol CMWaterSubmersionManagerDelegate : NSObjectProtocol
```

## Mentions

- [Accessing submersion data](accessing-submersion-data.md)

#### Overview

The system calls your delegate’s methods to provide updated data to your app. When the watch isn’t submerged, your app receives event, measurement, and error messages. However, the measurement updates include only surface pressure and submersion state data. After submersion, the measurement updates include depth and water pressure data. The watch also begins receiving water temperature updates.

> **Note**:  The system calls all the delegate’s methods on an anonymous background queue. Typically, you need to dispatch this data to the main queue or pass it to a [`MainActor`](https://developer.apple.com/documentation/Swift/MainActor) object before updating the user interface.

 The system calls all the delegate’s methods on an anonymous background queue. Typically, you need to dispatch this data to the main queue or pass it to a [`MainActor`](https://developer.apple.com/documentation/Swift/MainActor) object before updating the user interface.

The system sends measurement and temperature updates three times a second while the watch is submerged. When the watch is on the surface, the system provides updates at a slower rate, and may stop providing updates if the watch isn’t moving.

## Topics

### Receiving updates
- [func manager(CMWaterSubmersionManager, didUpdate: CMWaterSubmersionEvent)](cmwatersubmersionmanagerdelegate/manager(_:didupdate:)-6qux6.md)
  Tells the delegate when a water submersion event occurs.
- [func manager(CMWaterSubmersionManager, didUpdate: CMWaterSubmersionMeasurement)](cmwatersubmersionmanagerdelegate/manager(_:didupdate:)-7nhjb.md)
  Provides the delegate with a new set of pressure and depth measurements.
- [func manager(CMWaterSubmersionManager, didUpdate: CMWaterTemperature)](cmwatersubmersionmanagerdelegate/manager(_:didupdate:)-18wua.md)
  Provides the delegate with updated water temperature data.
- [func manager(CMWaterSubmersionManager, errorOccurred: any Error)](cmwatersubmersionmanagerdelegate/manager(_:erroroccurred:).md)
  Tells the delegate when an error occurs.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [Accessing submersion data](accessing-submersion-data.md)
  Use a water-submersion manager to receive water pressure, temperature, and depth data on Apple Watch Ultra.
- [class CMWaterSubmersionManager](cmwatersubmersionmanager.md)
  An object for managing the collection of pressure and temperature data during submersion.
- [class CMWaterSubmersionEvent](cmwatersubmersionevent.md)
  An event indicating that the device’s submersion state has changed.
- [class CMWaterSubmersionMeasurement](cmwatersubmersionmeasurement.md)
  An update that contains data about the pressure and depth.
- [class CMWaterTemperature](cmwatertemperature.md)
  An update that contains data about the water temperature.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmwatersubmersionmanagerdelegate)*