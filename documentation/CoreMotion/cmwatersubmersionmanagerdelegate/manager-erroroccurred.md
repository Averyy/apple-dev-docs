# manager(_:errorOccurred:)

**Framework**: Core Motion  
**Kind**: method  
**Required**: Yes

Tells the delegate when an error occurs.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
func manager(_ manager: CMWaterSubmersionManager, errorOccurred error: any Error)
```

## Mentions

- [Accessing submersion data](accessing-submersion-data.md)

#### Discussion

Implement this method to respond to errors.

```swift
// Respond to errors.
nonisolated func manager(_ manager: CMWaterSubmersionManager, errorOccurred error: Error) {
    logger.error("*** An error occurred: \(error.localizedDescription) ***")
}
```

## Parameters

- `manager`: The manager for water submersion data.
- `error`: An error object that contains information about the error.

## See Also

- [func manager(CMWaterSubmersionManager, didUpdate: CMWaterSubmersionEvent)](cmwatersubmersionmanagerdelegate/manager(_:didupdate:)-6qux6.md)
  Tells the delegate when a water submersion event occurs.
- [func manager(CMWaterSubmersionManager, didUpdate: CMWaterSubmersionMeasurement)](cmwatersubmersionmanagerdelegate/manager(_:didupdate:)-7nhjb.md)
  Provides the delegate with a new set of pressure and depth measurements.
- [func manager(CMWaterSubmersionManager, didUpdate: CMWaterTemperature)](cmwatersubmersionmanagerdelegate/manager(_:didupdate:)-18wua.md)
  Provides the delegate with updated water temperature data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmwatersubmersionmanagerdelegate/manager(_:erroroccurred:))*