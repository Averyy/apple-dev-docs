# removeAccessory(_:completionHandler:)

**Framework**: HomeKit  
**Kind**: method

Removes an accessory from the home.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 14.0+
- visionOS 1.0+

## Declaration

```swift
func removeAccessory(_ accessory: HMAccessory) async throws
```

## Parameters

- `accessory`: The accessory to remove.
- `completion`: The block executed after the request is processed.

## See Also

- [var accessories: [HMAccessory]](hmhome/accessories.md)
  The collection of accessories that are part of the home.
- [func addAndSetupAccessories(completionHandler: ((any Error)?) -> Void)](hmhome/addandsetupaccessories(completionhandler:).md)
  Finds and adds nearby accessories to the home.
- [func addAndSetupAccessories(with: HMAccessorySetupPayload, completionHandler: ([HMAccessory]?, (any Error)?) -> Void)](hmhome/addandsetupaccessories(with:completionhandler:).md)
  Finds and adds nearby accessories to the home using a HomeKit code provided by your app.
- [func addAccessory(HMAccessory, completionHandler: ((any Error)?) -> Void)](hmhome/addaccessory(_:completionhandler:).md)
  Adds a new accessory to the home.
- [func assignAccessory(HMAccessory, to: HMRoom, completionHandler: ((any Error)?) -> Void)](hmhome/assignaccessory(_:to:completionhandler:).md)
  Assigns an accessory to a different room.
- [var supportsAddingNetworkRouter: Bool](hmhome/supportsaddingnetworkrouter.md)
  A Boolean that indicates whether a home supports all of the requirements for adding a network router.
- [func unblockAccessory(HMAccessory, completionHandler: ((any Error)?) -> Void)](hmhome/unblockaccessory(_:completionhandler:).md)
  Unblocks a blocked accessory.
- [class HMAccessory](hmaccessory.md)
  A home automation accessory, like a garage door opener or a thermostat.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmhome/removeaccessory(_:completionhandler:))*