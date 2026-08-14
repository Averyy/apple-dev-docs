# MTRControllerFactory

**Framework**: Matter  
**Kind**: class

**Availability**:
- iOS 16.1+
- iPadOS 16.1+
- Mac Catalyst 16.1+
- macOS 13.0+
- tvOS 16.1+
- visionOS 1.0+
- watchOS 9.1+

## Declaration

```swift
class MTRControllerFactory
```

## Topics

### Instance Properties
- [var isRunning: Bool](mtrcontrollerfactory/isrunning.md)
### Instance Methods
- [func shutdown()](mtrcontrollerfactory/shutdown.md)
- [func startController(onExistingFabric: MTRDeviceControllerStartupParams) -> MTRDeviceController?](mtrcontrollerfactory/startcontroller(onexistingfabric:).md)
- [func startController(onNewFabric: MTRDeviceControllerStartupParams) -> MTRDeviceController?](mtrcontrollerfactory/startcontroller(onnewfabric:).md)
- [func startup(MTRControllerFactoryParams) -> Bool](mtrcontrollerfactory/startup(_:).md)
### Type Methods
- [class func sharedInstance() -> MTRControllerFactory](mtrcontrollerfactory/sharedinstance.md)

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrcontrollerfactory)*