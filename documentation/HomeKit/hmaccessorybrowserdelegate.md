# HMAccessoryBrowserDelegate

**Framework**: HomeKit  
**Kind**: protocol

An interface used to notify an accessory browser delegate of new accessories.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- visionOS 1.0+

## Declaration

```swift
protocol HMAccessoryBrowserDelegate : NSObjectProtocol
```

#### Overview

> ❗ **Important**:  To enable a consistent user experience across HomeKit enabled apps, use either the [`addAndSetupAccessories(completionHandler:)`](hmhome/addandsetupaccessories(completionhandler:).md) or the [`addAndSetupAccessories(with:completionHandler:)`](hmhome/addandsetupaccessories(with:completionhandler:).md) method of the [`HMHome`](hmhome.md) class instead of an accessory browser. These calls manage all the details of the accessory search process for you.

## Topics

### Tracking new accessories
- [func accessoryBrowser(HMAccessoryBrowser, didFindNewAccessory: HMAccessory)](hmaccessorybrowserdelegate/accessorybrowser(_:didfindnewaccessory:).md)
  Tells the delegate that a new accessory has been discovered.
- [func accessoryBrowser(HMAccessoryBrowser, didRemoveNewAccessory: HMAccessory)](hmaccessorybrowserdelegate/accessorybrowser(_:didremovenewaccessory:).md)
  Tells the delegate that a new accessory is no longer available in the browser.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [var delegate: (any HMAccessoryBrowserDelegate)?](hmaccessorybrowser/delegate.md)
  A delegate that receives updates on the discovered accessories.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmaccessorybrowserdelegate)*