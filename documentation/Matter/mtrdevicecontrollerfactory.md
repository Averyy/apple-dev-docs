# MTRDeviceControllerFactory

**Framework**: Matter  
**Kind**: class

**Availability**:
- iOS 16.4+
- iPadOS 16.4+
- Mac Catalyst 16.4+
- macOS 13.3+
- tvOS 16.4+
- visionOS 1.0+
- watchOS 9.4+

## Declaration

```swift
class MTRDeviceControllerFactory
```

## Mentions

- [Onboarding a Matter device](onboarding-a-matter-device.md)

## Topics

### Instance Properties
- [var isRunning: Bool](mtrdevicecontrollerfactory/isrunning.md)
- [var knownFabrics: [MTRFabricInfo]?](mtrdevicecontrollerfactory/knownfabrics.md)
### Instance Methods
- [func createController(onExistingFabric: MTRDeviceControllerStartupParams) throws -> MTRDeviceController](mtrdevicecontrollerfactory/createcontroller(onexistingfabric:).md)
- [func createController(onNewFabric: MTRDeviceControllerStartupParams) throws -> MTRDeviceController](mtrdevicecontrollerfactory/createcontroller(onnewfabric:).md)
- [func preWarmCommissioningSession()](mtrdevicecontrollerfactory/prewarmcommissioningsession.md)
- [func start(MTRDeviceControllerFactoryParams) throws](mtrdevicecontrollerfactory/start(_:).md)
- [func stop()](mtrdevicecontrollerfactory/stop.md)
### Type Methods
- [class func sharedInstance() -> MTRDeviceControllerFactory](mtrdevicecontrollerfactory/sharedinstance.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrdevicecontrollerfactory)*