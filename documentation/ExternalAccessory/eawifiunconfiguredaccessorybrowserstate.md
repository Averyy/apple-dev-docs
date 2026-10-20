# EAWiFiUnconfiguredAccessoryBrowserState

**Framework**: External Accessory  
**Kind**: enum  
**Role**: Enumeration

The possible states of an accessory browser.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
enum EAWiFiUnconfiguredAccessoryBrowserState
```

```c
enum EAWiFiUnconfiguredAccessoryBrowserState : NSInteger;
```

## Topics

### States
- [EAWiFiUnconfiguredAccessoryBrowserState.wiFiUnavailable](./eawifiunconfiguredaccessorybrowserstate/wifiunavailable.md)
  Wi-Fi is unavailable, typically because the user has placed the device in Airplane Mode or explicitly turned off Wi-Fi.
- [EAWiFiUnconfiguredAccessoryBrowserState.stopped](./eawifiunconfiguredaccessorybrowserstate/stopped.md)
  The browser is not actively searching for unconfigured accessories.
- [EAWiFiUnconfiguredAccessoryBrowserState.searching](./eawifiunconfiguredaccessorybrowserstate/searching.md)
  The browser is actively searching for unconfigured accessory.
- [EAWiFiUnconfiguredAccessoryBrowserState.configuring](./eawifiunconfiguredaccessorybrowserstate/configuring.md)
  The browser is actively configuring an accessory.
### Initializers
- [init?(rawValue: Int)](./eawifiunconfiguredaccessorybrowserstate/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Getting Updates About Browser State
- [func accessoryBrowser(EAWiFiUnconfiguredAccessoryBrowser, didUpdate: EAWiFiUnconfiguredAccessoryBrowserState)](./eawifiunconfiguredaccessorybrowserdelegate/accessorybrowser%28_,didupdate%29.md)
  Indicates that the browser’s state has changed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/externalaccessory/eawifiunconfiguredaccessorybrowserstate)*