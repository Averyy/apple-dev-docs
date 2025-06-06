# EAWiFiUnconfiguredAccessoryBrowser

**Framework**: External Accessory  
**Kind**: class

An object you use to scan for wireless accessories and configure them for use with the user’s app.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
class EAWiFiUnconfiguredAccessoryBrowser
```

#### Overview

The [`EAWiFiUnconfiguredAccessoryBrowser`](eawifiunconfiguredaccessorybrowser.md) class gives your app access to the MFi Wireless Accessory Configuration process. You use a browser object to scan for unconfigured accessories, connect them to the user’s Wi-Fi infrastructure, and configure attributes of the accessories. An accessory is represented by an instance of [`EAWiFiUnconfiguredAccessory`](eawifiunconfiguredaccessory.md).

## Topics

### Creating the Browser Object
- [init(delegate: (any EAWiFiUnconfiguredAccessoryBrowserDelegate)?, queue: dispatch_queue_t?)](eawifiunconfiguredaccessorybrowser/init(delegate:queue:).md)
  Creates a browser object that scans for unconfigured accessories.
### Managing Browser Interactions
- [var delegate: (any EAWiFiUnconfiguredAccessoryBrowserDelegate)?](eawifiunconfiguredaccessorybrowser/delegate.md)
  The object that acts as the delegate of the browser and receives browser events.
- [protocol EAWiFiUnconfiguredAccessoryBrowserDelegate](eawifiunconfiguredaccessorybrowserdelegate.md)
  A protocol you use to manage the search and configuration processes for an unconfigured accessory browser.
### Finding and Configuring Accessories
- [func configureAccessory(EAWiFiUnconfiguredAccessory, withConfigurationUIOn: UIViewController)](eawifiunconfiguredaccessorybrowser/configureaccessory(_:withconfigurationuion:).md)
  Begins the configuration process for the specified accessory.
- [func startSearchingForUnconfiguredAccessories(matching: NSPredicate?)](eawifiunconfiguredaccessorybrowser/startsearchingforunconfiguredaccessories(matching:).md)
  Starts the search for unconfigured accessories that match the specified predicate.
- [func stopSearchingForUnconfiguredAccessories()](eawifiunconfiguredaccessorybrowser/stopsearchingforunconfiguredaccessories.md)
  Stops the search for unconfigured accessories.
- [var unconfiguredAccessories: Set<EAWiFiUnconfiguredAccessory>](eawifiunconfiguredaccessorybrowser/unconfiguredaccessories.md)
  The set of unconfigured accessories that have been discovered.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [Wireless Accessory Configuration Entitlement](../BundleResources/Entitlements/com.apple.external-accessory.wireless-configuration.md)
  A Boolean value that indicates whether your app may configure MFi Wi-Fi accessories.
- [class EAWiFiUnconfiguredAccessory](eawifiunconfiguredaccessory.md)
  An object that provides information about an unconfigured MFi Wireless Accessory Configuration accessory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/externalaccessory/eawifiunconfiguredaccessorybrowser)*