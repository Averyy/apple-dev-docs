# defaultPath

**Framework**: Network Extension  
**Kind**: property  
**Role**: Instance Property

The current default network path used for connections created by the provider.

**Availability**:
- iOS 9.0+ - Deprecated in 18.0
- iPadOS 9.0+ - Deprecated in 18.0
- Mac Catalyst 13.1+ - Deprecated in 18.0
- macOS 10.11+ - Deprecated in 15.0
- tvOS 17.0+ - Deprecated in 18.0
- visionOS 1.0+ - Deprecated in 2.0

> **Deprecated**: Use the [`nw_path_monitor_t`](../../Network/nw_path_monitor_t.md) type from the [Network](../../Network/Network.md) framework instead.

## Declaration

```swift
var defaultPath: NWPath? { get }
```

```objc
@property (readonly, nullable) NWPath * defaultPath;
```

## Discussion

This NWPath object contains information about which physical network interface will be used by connections opened by the Network Extension provider. You can determine when this physical interface changes by observing this property using KVO.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neprovider/defaultpath)*