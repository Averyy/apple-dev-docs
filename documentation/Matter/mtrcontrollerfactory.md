# MTRControllerFactory

**Framework**: Matter  
**Kind**: class  
**Role**: Class

**Availability**:
- iOS 16.1+ - Deprecated in 16.4
- iPadOS 16.1+ - Deprecated in 16.4
- Mac Catalyst 16.1+ - Deprecated in 16.4
- macOS 13.0+ - Deprecated in 13.3
- tvOS 16.1+ - Deprecated in 16.4
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 9.1+ - Deprecated in 9.4

> **Deprecated**: Please use MTRDeviceControllerFactory

## Declaration

```swift
class MTRControllerFactory
```

```objc
@interface MTRControllerFactory : NSObject
```

## Topics

### Instance Properties
- [var isRunning: Bool](./mtrcontrollerfactory/isrunning.md)
### Instance Methods
- [func shutdown()](./mtrcontrollerfactory/shutdown%28%29.md)
- [func startController(onExistingFabric: MTRDeviceControllerStartupParams) -> MTRDeviceController?](./mtrcontrollerfactory/startcontroller%28onexistingfabric%29.md)
- [func startController(onNewFabric: MTRDeviceControllerStartupParams) -> MTRDeviceController?](./mtrcontrollerfactory/startcontroller%28onnewfabric%29.md)
- [func startup(MTRControllerFactoryParams) -> Bool](./mtrcontrollerfactory/startup%28_%29.md)
### Type Methods
- [class func sharedInstance() -> MTRControllerFactory](./mtrcontrollerfactory/sharedinstance%28%29.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrcontrollerfactory)*