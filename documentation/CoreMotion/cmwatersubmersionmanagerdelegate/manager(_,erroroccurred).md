# manager(_:errorOccurred:)

**Framework**: Core Motion  
**Kind**: method  
**Role**: Instance Method

Tells the delegate when an error occurs.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
optional func manager(_ manager: CMWaterSubmersionManager, errorOccurred error: any Error)
```

```objc
- (void) manager:(CMWaterSubmersionManager *) manager errorOccurred:(NSError *) error;
```

## Mentions

- [Accessing submersion data](../accessing-submersion-data.md)

## Discussion

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

### Receiving updates
- [func manager(CMWaterSubmersionManager, didUpdate: CMWaterSubmersionEvent)](./manager%28_,didupdate%29-6qux6.md)
  Tells the delegate when a water submersion event occurs.
- [func manager(CMWaterSubmersionManager, didUpdate: CMWaterSubmersionMeasurement)](./manager%28_,didupdate%29-7nhjb.md)
  Provides the delegate with a new set of pressure and depth measurements.
- [func manager(CMWaterSubmersionManager, didUpdate: CMWaterTemperature)](./manager%28_,didupdate%29-18wua.md)
  Provides the delegate with updated water temperature data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmwatersubmersionmanagerdelegate/manager(_:erroroccurred:))*