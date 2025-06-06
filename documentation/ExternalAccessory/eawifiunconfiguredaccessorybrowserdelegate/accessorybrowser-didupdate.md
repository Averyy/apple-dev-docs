# accessoryBrowser(_:didUpdate:)

**Framework**: External Accessory  
**Kind**: method  
**Required**: Yes

Indicates that the browser’s state has changed.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
func accessoryBrowser(_ browser: EAWiFiUnconfiguredAccessoryBrowser, didUpdate state: EAWiFiUnconfiguredAccessoryBrowserState)
```

#### Discussion

When the browser state changes, the delegate typically provides feedback to users. For example, the delegate might show whether the scan is currently active or inactive, or it might indicate that Wi-Fi is unavailable if a user starts a scan while the device is in airplane mode.

## Parameters

- `browser`: The instance of   that is generating the event.
- `state`: The current state of the browser. See   for possible values.

## See Also

- [enum EAWiFiUnconfiguredAccessoryBrowserState](eawifiunconfiguredaccessorybrowserstate.md)
  The possible states of an accessory browser.


---

*[View on Apple Developer](https://developer.apple.com/documentation/externalaccessory/eawifiunconfiguredaccessorybrowserdelegate/accessorybrowser(_:didupdate:))*