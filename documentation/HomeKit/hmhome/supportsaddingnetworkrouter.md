# supportsAddingNetworkRouter

**Framework**: HomeKit  
**Kind**: property  
**Role**: Instance Property

A Boolean that indicates whether a home supports all of the requirements for adding a network router.

**Availability**:
- iOS 13.2+
- iPadOS 13.2+
- Mac Catalyst 13.2+
- tvOS 13.2+
- visionOS 1.0+
- watchOS 6.1+

## Declaration

```swift
var supportsAddingNetworkRouter: Bool { get }
```

```objc
@property (nonatomic, assign, readonly) BOOL supportsAddingNetworkRouter;
```

## See Also

### Managing accessories
- [var accessories: [HMAccessory]](./accessories.md)
  The collection of accessories that are part of the home.
- [func addAndSetupAccessories(completionHandler: ((any Error)?) -> Void)](./addandsetupaccessories%28completionhandler%29.md)
  Finds and adds nearby accessories to the home.
- [func addAndSetupAccessories(with: HMAccessorySetupPayload, completionHandler: ([HMAccessory]?, (any Error)?) -> Void)](./addandsetupaccessories%28with,completionhandler%29.md)
  Finds and adds nearby accessories to the home using a HomeKit code provided by your app.
- [func addAccessory(HMAccessory, completionHandler: ((any Error)?) -> Void)](./addaccessory%28_,completionhandler%29.md)
  Adds a new accessory to the home.
- [func assignAccessory(HMAccessory, to: HMRoom, completionHandler: ((any Error)?) -> Void)](./assignaccessory%28_,to,completionhandler%29.md)
  Assigns an accessory to a different room.
- [func removeAccessory(HMAccessory, completionHandler: ((any Error)?) -> Void)](./removeaccessory%28_,completionhandler%29.md)
  Removes an accessory from the home.
- [func unblockAccessory(HMAccessory, completionHandler: ((any Error)?) -> Void)](./unblockaccessory%28_,completionhandler%29.md)
  Unblocks a blocked accessory.
- [class HMAccessory](../hmaccessory.md)
  A home automation accessory, like a garage door opener or a thermostat.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmhome/supportsaddingnetworkrouter)*