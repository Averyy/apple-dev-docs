# sharedController(withID:xpcConnect:)

**Framework**: Matter  
**Kind**: method  
**Role**: Type Method

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
class func sharedController(withID controllerID: (any NSCopying)?, xpcConnect xpcConnectBlock: @escaping MTRXPCConnectBlock) -> MTRDeviceController
```

```objc
+ (MTRDeviceController *) sharedControllerWithID:(id<NSCopying>) controllerID xpcConnectBlock:(MTRXPCConnectBlock) xpcConnectBlock;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrdevicecontroller/sharedcontroller(withid:xpcconnect:)-5yhq4)*