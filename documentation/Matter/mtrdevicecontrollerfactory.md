# MTRDeviceControllerFactory

**Framework**: Matter  
**Kind**: class  
**Role**: Class

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

```objc
@interface MTRDeviceControllerFactory : NSObject
```

## Mentions

- [Onboarding a Matter device](./onboarding-a-matter-device.md)

## Topics

### Instance Properties
- [var isRunning: Bool](./mtrdevicecontrollerfactory/isrunning.md)
- [var knownFabrics: [MTRFabricInfo]?](./mtrdevicecontrollerfactory/knownfabrics.md)
### Instance Methods
- [func createController(onExistingFabric: MTRDeviceControllerStartupParams) throws -> MTRDeviceController](./mtrdevicecontrollerfactory/createcontroller%28onexistingfabric%29.md)
- [func createController(onNewFabric: MTRDeviceControllerStartupParams) throws -> MTRDeviceController](./mtrdevicecontrollerfactory/createcontroller%28onnewfabric%29.md)
- [func preWarmCommissioningSession()](./mtrdevicecontrollerfactory/prewarmcommissioningsession%28%29.md)
- [func start(MTRDeviceControllerFactoryParams) throws](./mtrdevicecontrollerfactory/start%28_%29.md)
- [func stop()](./mtrdevicecontrollerfactory/stop%28%29.md)
### Type Methods
- [class func sharedInstance() -> MTRDeviceControllerFactory](./mtrdevicecontrollerfactory/sharedinstance%28%29.md)

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrdevicecontrollerfactory)*