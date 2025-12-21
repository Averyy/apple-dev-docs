# matterStartupParametersXPCConnectBlock

**Framework**: HomeKit  
**Kind**: property

**Availability**:
- iOS 18.2+
- iPadOS 18.2+
- Mac Catalyst 18.2+
- tvOS 18.2+
- visionOS 2.2+
- watchOS 11.2+

## Declaration

```swift
var matterStartupParametersXPCConnectBlock: () -> NSXPCConnection { get }
```

#### Discussion

Block generating XPC connection on demand through which to access the Matter controller associated with this home. This property can be passed as part of an MTRXPCDeviceControllerParameters to create an MTRDeviceController that will have access to the Apple Home Fabric.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmhome/matterstartupparametersxpcconnectblock)*