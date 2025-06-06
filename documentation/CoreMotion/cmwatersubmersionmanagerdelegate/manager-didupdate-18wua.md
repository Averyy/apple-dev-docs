# manager(_:didUpdate:)

**Framework**: Core Motion  
**Kind**: method  
**Required**: Yes

Provides the delegate with updated water temperature data.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
func manager(_ manager: CMWaterSubmersionManager, didUpdate measurement: CMWaterTemperature)
```

#### Discussion

Implement this method to receive water temperature updates. The system sends temperature updates three times a second while submerged. When on the surface, the system provides updates at a slower rate, and may stop providing updates if the device isn’t moving.

```swift
nonisolated func manager(_ manager: CMWaterSubmersionManager, didUpdate measurement: CMWaterTemperature) {
    let temp = measurement.temperature
    let uncertainty = measurement.temperatureUncertainty
    let currentTemperature = "\(temp.value) +/- \(uncertainty.value) \(temp.unit)"

    logger.info(("*** \(currentTemperature) ***"))

    Task {
        await myAdd(temperature:measurement)
    }
}
```

## Parameters

- `manager`: The manager for water submersion data.
- `measurement`: A data object that contains information about the water temperature and the measurement’s uncertainty.

## See Also

- [func manager(CMWaterSubmersionManager, didUpdate: CMWaterSubmersionEvent)](cmwatersubmersionmanagerdelegate/manager(_:didupdate:)-6qux6.md)
  Tells the delegate when a water submersion event occurs.
- [func manager(CMWaterSubmersionManager, didUpdate: CMWaterSubmersionMeasurement)](cmwatersubmersionmanagerdelegate/manager(_:didupdate:)-7nhjb.md)
  Provides the delegate with a new set of pressure and depth measurements.
- [func manager(CMWaterSubmersionManager, errorOccurred: any Error)](cmwatersubmersionmanagerdelegate/manager(_:erroroccurred:).md)
  Tells the delegate when an error occurs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmwatersubmersionmanagerdelegate/manager(_:didupdate:)-18wua)*