# manager(_:didUpdate:)

**Framework**: Core Motion  
**Kind**: method  
**Required**: Yes

Tells the delegate when a water submersion event occurs.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
func manager(_ manager: CMWaterSubmersionManager, didUpdate event: CMWaterSubmersionEvent)
```

#### Discussion

Implement this method to respond to changes in the device’s submersion state.

```swift
nonisolated func manager(_ manager: CMWaterSubmersionManager, didUpdate event: CMWaterSubmersionEvent) {

    let submerged: Bool?
    switch event.state {
    case .unknown:
        logger.info("*** Received an unknown event ***")
        submerged = nil

    case .notSubmerged:
        logger.info("*** Not Submerged Event ***")
        submerged = false

    case .submerged:
        logger.info("*** Submerged Event ***")
        submerged = true

    @unknown default:
        fatalError("*** unknown event received: \(event.state) ***")
    }

    Task {
        await myAdd(event: event)
        if let submerged {
            await mySet(submerged: submerged)
        }
    }
}
```

## Parameters

- `manager`: The manager for water submersion data.
- `event`: An event indicating that the submersion state has changed.

## See Also

- [func manager(CMWaterSubmersionManager, didUpdate: CMWaterSubmersionMeasurement)](cmwatersubmersionmanagerdelegate/manager(_:didupdate:)-7nhjb.md)
  Provides the delegate with a new set of pressure and depth measurements.
- [func manager(CMWaterSubmersionManager, didUpdate: CMWaterTemperature)](cmwatersubmersionmanagerdelegate/manager(_:didupdate:)-18wua.md)
  Provides the delegate with updated water temperature data.
- [func manager(CMWaterSubmersionManager, errorOccurred: any Error)](cmwatersubmersionmanagerdelegate/manager(_:erroroccurred:).md)
  Tells the delegate when an error occurs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmwatersubmersionmanagerdelegate/manager(_:didupdate:)-6qux6)*