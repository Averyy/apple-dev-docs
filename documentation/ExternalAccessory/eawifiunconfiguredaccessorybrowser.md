# EAWiFiUnconfiguredAccessoryBrowser

**Framework**: External Accessory  
**Kind**: class  
**Role**: Class

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

```objc
@interface EAWiFiUnconfiguredAccessoryBrowser : NSObject
```

#### Overview

The [`EAWiFiUnconfiguredAccessoryBrowser`](./eawifiunconfiguredaccessorybrowser.md) class gives your app access to the MFi Wireless Accessory Configuration process. You use a browser object to scan for unconfigured accessories, connect them to the user’s Wi-Fi infrastructure, and configure attributes of the accessories. An accessory is represented by an instance of [`EAWiFiUnconfiguredAccessory`](./eawifiunconfiguredaccessory.md).

## Topics

### Creating the Browser Object
- [init(delegate: (any EAWiFiUnconfiguredAccessoryBrowserDelegate)?, queue: dispatch_queue_t?)](./eawifiunconfiguredaccessorybrowser/init%28delegate,queue%29.md)
  Creates a browser object that scans for unconfigured accessories.
### Managing Browser Interactions
- [var delegate: (any EAWiFiUnconfiguredAccessoryBrowserDelegate)?](./eawifiunconfiguredaccessorybrowser/delegate.md)
  The object that acts as the delegate of the browser and receives browser events.
- [protocol EAWiFiUnconfiguredAccessoryBrowserDelegate](./eawifiunconfiguredaccessorybrowserdelegate.md)
  A protocol you use to manage the search and configuration processes for an unconfigured accessory browser.
### Finding and Configuring Accessories
- [func configureAccessory(EAWiFiUnconfiguredAccessory, withConfigurationUIOn: UIViewController)](./eawifiunconfiguredaccessorybrowser/configureaccessory%28_,withconfigurationuion%29.md)
  Begins the configuration process for the specified accessory.
- [func startSearchingForUnconfiguredAccessories(matching: NSPredicate?)](./eawifiunconfiguredaccessorybrowser/startsearchingforunconfiguredaccessories%28matching%29.md)
  Starts the search for unconfigured accessories that match the specified predicate.
- [func stopSearchingForUnconfiguredAccessories()](./eawifiunconfiguredaccessorybrowser/stopsearchingforunconfiguredaccessories%28%29.md)
  Stops the search for unconfigured accessories.
- [var unconfiguredAccessories: Set<EAWiFiUnconfiguredAccessory>](./eawifiunconfiguredaccessorybrowser/unconfiguredaccessories.md)
  The set of unconfigured accessories that have been discovered.

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

## See Also

### Wi-Fi Accessory Configuration
- [Wireless Accessory Configuration Entitlement](../BundleResources/entitlements/com.apple.external-accessory.wireless-configuration.md)
  A Boolean value that indicates whether your app may configure MFi Wi-Fi accessories.
- [class EAWiFiUnconfiguredAccessory](./eawifiunconfiguredaccessory.md)
  An object that provides information about an unconfigured MFi Wireless Accessory Configuration accessory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/externalaccessory/eawifiunconfiguredaccessorybrowser)*