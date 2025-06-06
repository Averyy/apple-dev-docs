# EAWiFiUnconfiguredAccessoryBrowserDelegate

**Framework**: External Accessory  
**Kind**: protocol

A protocol you use to manage the search and configuration processes for an unconfigured accessory browser.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
protocol EAWiFiUnconfiguredAccessoryBrowserDelegate : NSObjectProtocol
```

## Topics

### Getting Updates About Browser State
- [func accessoryBrowser(EAWiFiUnconfiguredAccessoryBrowser, didUpdate: EAWiFiUnconfiguredAccessoryBrowserState)](eawifiunconfiguredaccessorybrowserdelegate/accessorybrowser(_:didupdate:).md)
  Indicates that the browser’s state has changed.
- [enum EAWiFiUnconfiguredAccessoryBrowserState](eawifiunconfiguredaccessorybrowserstate.md)
  The possible states of an accessory browser.
### Getting Updates About the Configuration Process
- [func accessoryBrowser(EAWiFiUnconfiguredAccessoryBrowser, didFinishConfiguringAccessory: EAWiFiUnconfiguredAccessory, with: EAWiFiUnconfiguredAccessoryConfigurationStatus)](eawifiunconfiguredaccessorybrowserdelegate/accessorybrowser(_:didfinishconfiguringaccessory:with:).md)
  Indicates that the browser has completed configuring the specified accessory.
- [enum EAWiFiUnconfiguredAccessoryConfigurationStatus](eawifiunconfiguredaccessoryconfigurationstatus.md)
  Values that represent the state of the configuration process for an [`EAWiFiUnconfiguredAccessory`](eawifiunconfiguredaccessory.md) object.
### Getting Updates About the Search Process
- [func accessoryBrowser(EAWiFiUnconfiguredAccessoryBrowser, didFindUnconfiguredAccessories: Set<EAWiFiUnconfiguredAccessory>)](eawifiunconfiguredaccessorybrowserdelegate/accessorybrowser(_:didfindunconfiguredaccessories:).md)
  Indicates that the browser found a new unconfigured accessory that matches the filter predicate defined at the start of the search.
- [func accessoryBrowser(EAWiFiUnconfiguredAccessoryBrowser, didRemoveUnconfiguredAccessories: Set<EAWiFiUnconfiguredAccessory>)](eawifiunconfiguredaccessorybrowserdelegate/accessorybrowser(_:didremoveunconfiguredaccessories:).md)
  Indicates that the browser removed an unconfigured accessory from the search results.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [var delegate: (any EAWiFiUnconfiguredAccessoryBrowserDelegate)?](eawifiunconfiguredaccessorybrowser/delegate.md)
  The object that acts as the delegate of the browser and receives browser events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/externalaccessory/eawifiunconfiguredaccessorybrowserdelegate)*