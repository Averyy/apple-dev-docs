# accessoryBrowser(_:didFinishConfiguringAccessory:with:)

**Framework**: External Accessory  
**Kind**: method  
**Required**: Yes

Indicates that the browser has completed configuring the specified accessory.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
func accessoryBrowser(_ browser: EAWiFiUnconfiguredAccessoryBrowser, didFinishConfiguringAccessory accessory: EAWiFiUnconfiguredAccessory, with status: EAWiFiUnconfiguredAccessoryConfigurationStatus)
```

#### Discussion

This method is called when the system-provided configuration view has been dismissed, revealing the part of the app’s user interface that was visible before the configuration process began. If the configuration was successful, the app can begin communicating with the accessory.

## Parameters

- `browser`: The instance of   that is generating the event.
- `accessory`: The   object whose configuration process has completed.
- `status`: The status of the completed configuration process. See   for possible values.

## See Also

- [enum EAWiFiUnconfiguredAccessoryConfigurationStatus](eawifiunconfiguredaccessoryconfigurationstatus.md)
  Values that represent the state of the configuration process for an [`EAWiFiUnconfiguredAccessory`](eawifiunconfiguredaccessory.md) object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/externalaccessory/eawifiunconfiguredaccessorybrowserdelegate/accessorybrowser(_:didfinishconfiguringaccessory:with:))*