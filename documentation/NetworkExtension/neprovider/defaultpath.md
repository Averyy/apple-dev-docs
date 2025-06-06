# defaultPath

**Framework**: Network Extension  
**Kind**: property

The current default network path used for connections created by the provider.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var defaultPath: NWPath? { get }
```

#### Discussion

This NWPath object contains information about which physical network interface will be used by connections opened by the Network Extension provider. You can determine when this physical interface changes by observing this property using KVO.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neprovider/defaultpath)*